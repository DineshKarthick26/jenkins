from flask import Flask, render_template, url_for, jsonify
import os

app = Flask(__name__)

# Personal Portfolio Data
PORTFOLIO_OWNER = "Dinesh Karthick"
PORTFOLIO_TITLE = "DevOps Engineer"
PORTFOLIO_BIO = "DevOps and Cloud Security Enthusiast"

# Your Projects
PROJECTS = {
    "project1": {
        "title": "E-Commerce Platform",
        "slug": "ecommerce-platform",
        "gradient": "linear-gradient(135deg, #ff0844 0%, #ffb199 100%)",
        "description": "Full-stack e-commerce application with payment integration",
        "image": "🛍️",
        "tags": ["Python", "Flask", "React", "PostgreSQL", "Stripe"],
        "details": "Built a complete e-commerce platform with user authentication, product management, shopping cart, and secure payment processing. Features real-time inventory updates and order tracking.",
        "github": "https://github.com/yourusername/ecommerce-platform",
        "live": "https://yourlivesite.com",
        "features": [
            "User authentication and profiles",
            "Product catalog with search and filters",
            "Shopping cart and checkout",
            "Payment integration with Stripe",
            "Order management system",
            "Admin dashboard"
        ]
    },
    "project2": {
        "title": "Task Management App",
        "slug": "task-management",
        "gradient": "linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)",
        "description": "Collaborative task management with real-time updates",
        "image": "✅",
        "tags": ["React", "Node.js", "MongoDB", "WebSocket", "Docker"],
        "details": "A real-time collaborative task management application allowing teams to organize work, track progress, and communicate effectively.",
        "github": "https://github.com/yourusername/task-management",
        "live": "https://yourtaskapp.com",
        "features": [
            "Real-time task updates",
            "Team collaboration",
            "Priority and status tracking",
            "File attachments",
            "Comment and discussion",
            "Mobile responsive"
        ]
    },
    "project3": {
        "title": "AI Chat Assistant",
        "slug": "ai-chat-assistant",
        "gradient": "linear-gradient(135deg, #8e2de2 0%, #4a00e0 100%)",
        "description": "Intelligent chatbot with NLP capabilities",
        "image": "🤖",
        "tags": ["Python", "TensorFlow", "FastAPI", "React", "WebSocket"],
        "details": "An AI-powered chatbot using natural language processing to understand and respond to user queries intelligently.",
        "github": "https://github.com/yourusername/ai-chat",
        "live": "https://yourchatapp.com",
        "features": [
            "Natural language understanding",
            "Machine learning model",
            "Conversation history",
            "Multi-language support",
            "Learning from interactions",
            "Real-time responses"
        ]
    },
    "project4": {
        "title": "Analytics Dashboard",
        "slug": "analytics-dashboard",
        "gradient": "linear-gradient(135deg, #f7971e 0%, #ffd200 100%)",
        "description": "Real-time data visualization and analytics",
        "image": "📊",
        "tags": ["React", "D3.js", "Node.js", "PostgreSQL", "AWS"],
        "details": "A comprehensive analytics dashboard for visualizing business metrics and generating actionable insights from complex data.",
        "github": "https://github.com/yourusername/analytics",
        "live": "https://youranalytics.com",
        "features": [
            "Real-time data updates",
            "Interactive charts and graphs",
            "Custom report generation",
            "Data export functionality",
            "User role management",
            "Performance optimization"
        ]
    }
}

# Your Skills
SKILLS = {
    "Frontend": ["React", "Vue.js", "JavaScript", "HTML5", "CSS3", "Tailwind CSS"],
    "Backend": ["Python", "Flask", "Node.js", "Express", "Django", "FastAPI"],
    "Database": ["PostgreSQL", "MongoDB", "Redis", "MySQL", "Firebase"],
    "Tools & DevOps": ["Git", "Docker", "Kubernetes", "CI/CD", "AWS", "Linux"]
}

# Contact Information
CONTACT = {
    "email": "your.email@example.com",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "github": "https://github.com/yourusername",
    "twitter": "https://twitter.com/yourhandle",
    "location": "Your City, Country"
}

@app.context_processor
def inject_globals():
    return {
        "PORTFOLIO_OWNER": PORTFOLIO_OWNER,
        "PORTFOLIO_TITLE": PORTFOLIO_TITLE,
        "CONTACT": CONTACT,
        "PROJECTS": PROJECTS,
        "SKILLS": SKILLS
    }

@app.route("/")
def index():
    """Home page with portfolio overview"""
    projects = [
        {
            "key": k,
            "title": v["title"],
            "description": v["description"],
            "image": v["image"],
            "url": f"/project/{v['slug']}",
            "gradient": v["gradient"],
            "tags": v["tags"][:3]
        }
        for k, v in PROJECTS.items()
    ]
    return render_template("index.html", projects=projects)

@app.route("/project/<project_slug>")
def project_detail(project_slug):
    """Display individual project details"""
    project_data = None
    for key, project in PROJECTS.items():
        if project["slug"] == project_slug:
            project_data = project
            break
    
    if not project_data:
        return render_template("404.html"), 404
    
    return render_template(
        "project.html",
        project=project_data,
        project_slug=project_slug
    )

@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Contact page"""
    return render_template("contact.html")

@app.route("/api/projects")
def api_projects():
    """API endpoint to get all projects"""
    return jsonify(PROJECTS)

@app.route("/api/project/<project_slug>")
def api_project(project_slug):
    """API endpoint for specific project"""
    for key, project in PROJECTS.items():
        if project["slug"] == project_slug:
            return jsonify(project)
    return jsonify({"error": "Project not found"}), 404

@app.route("/api/skills")
def api_skills():
    """API endpoint to get skills"""
    return jsonify(SKILLS)

@app.route("/api/contact")
def api_contact():
    """API endpoint to get contact info"""
    return jsonify(CONTACT)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

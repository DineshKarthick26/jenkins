# 🎨 Flask Portfolio Web App

This repository contains a modern, responsive **Flask-based web portfolio** project   
It is built to showcase Flask web development with a professional DevOps-themed UI.

---

## 🚀 Features
- Flask-powered backend
- Beautiful responsive dark neon UI
- Sections: Hero, Who I Am, Life at Shubham Gour Tech, Playlists
- Smooth animations and glowing theme
- CI/CD ready with Docker and Jenkins

---

## 🧠 Tech Stack
- **Flask (Python)** — Backend Framework  
- **HTML, CSS** — Frontend Design  
- **Docker** — Containerization  
- **Jenkins** — CI/CD Pipeline

---

## ⚙️ Run Locally
```bash
pip install -r requirements.txt
python app.py
```

Then open [http://localhost:5000](http://localhost:5000)

---


## 🐳 Run with Docker
```bash
docker build -t theshubhamgour/flask-portfolio .
docker run -p 5000:5000 theshubhamgour/flask-portfolio
```

---
## 📁 Folder Structure
```
flask-portfolio/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── playlist.html
│
└── static/
    ├── style.css
    ├── favicon.ico
    └── img/    # Add your photos here
'''

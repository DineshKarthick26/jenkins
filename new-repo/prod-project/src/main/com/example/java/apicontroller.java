package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
public class ApiController {

    @GetMapping("/")
    public String home() {
        return "<h1>🚀 Spring Boot DevOps App Running</h1>";
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "healthy");
    }

    @GetMapping("/api")
    public Map<String, Object> api() {
        return Map.of(
                "app", "Spring Boot DevOps App",
                "status", "running"
        );
    }

    @PostMapping("/data")
    public Map<String, Object> data(@RequestBody Map<String, Object> body) {
        return Map.of(
                "received", body,
                "status", "success"
        );
    }
}
# Prompt Injection Firewall

A lightweight Prompt Injection Firewall built with **FastAPI** that detects, sanitizes, and logs potentially malicious prompts before forwarding them to a Large Language Model (LLM).

The project combines **pattern-based detection**, **heuristic analysis**, **prompt sanitization** for monitoring security events.

## Features

- Pattern-based prompt injection detection using regular expressions
- Heuristic analysis for suspicious prompt behavior
- Automatic prompt sanitization
- Risk scoring and severity classification
- Block / Sanitize / Allow decision engine
- Unique Event ID generated for every request
- Processing time logging
- Audit logging for every prompt
- Dashboard with security statistics
- Pie chart visualization using Chart.js
- Search incidents by Event ID
- Responsive dark-themed dashboard

## Architecture

```
                User Prompt
                     │
                     ▼
          Pattern Detection Engine
                     │
                     ▼
          Heuristic Analysis Engine
                     │
                     ▼
             Risk Score Engine
                     │
                     ▼
           Prompt Sanitization
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     Block Request         Forward to LLM
          │                     │
          └──────────┬──────────┘
                     ▼
              Audit Logger
                     │
                     ▼
          Dashboard & Analytics
```



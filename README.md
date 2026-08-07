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

## Project Structure
```
Prompt-Injection-Firewall/
│
├── app.py
├── proxy.py
├── detector/
│   └── patterns.py
├── heuristic/
│   └── analyzer.py
├── scoring/
│   └── engine.py
├── sanitizer/
│   └── clean.py
├── logger/
│   └── audit.py
├── dashboard/
│   ├── dashboard.py
│   └── parser.py
├── templates/
│   └── dashboard.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
├── logs/
│   └── firewall.log
├── requirements.txt
└── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/shivani-netsec/Prompt-Injection-Firewall.git
```

Move into the project

```bash
cd Prompt-Injection-Firewall
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

Dashboard

```
http://127.0.0.1:8000/dashboard
```

## Dashboard

The dashboard provides:

- Total Requests
- Allowed Requests
- Sanitized Requests
- Blocked Requests
- Request Distribution Pie Chart
- Incident Search by Event ID
- Security Event Table

## Audit Log

Every request is recorded with:

- Event ID
- Timestamp
- Original Prompt
- Sanitized Prompt
- Risk Score
- Severity
- Decision
- Matched Patterns
- Heuristic Reasons
- Removed Phrases
- Processing Time


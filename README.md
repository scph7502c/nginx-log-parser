# Nginx Log Parser (WIP)

This repository is a **work in progress** project focused on parsing and analyzing server logs with Python.  
The first script included here works with **Nginx access logs**, but the repository will be extended with additional
tools and parsers in the future.

---

## 🚀 Current Features

- Read Nginx access log line by line
- Extract basic fields:
    - **IP address**
    - **HTTP status code**
- Load configuration from a `.env` file (e.g., log file path)

---

## 🛠️ Technologies

- **Python 3.x**
- Built-in modules: `os`, `pathlib`
- Optional: [`python-dotenv`](https://pypi.org/project/python-dotenv/) – for loading `.env` files

---

## 📂 Repository Structure

```text
.
├── nginx_log_parser.py   # current script (WIP)
├── .env                  # config file with log file path (example only)
├── sample.access.log     # sample Nginx log file (for testing)
└── README.md             # documentation
```

---

## ⚙️ Setup

1. Create a `.env` file:
   ```env
   NGINX_LOG_FILE=./sample.access.log

2. Install dependencies:

python nginx_log_parser.py

3. Run the script:
   python nginx_log_parser.py

Example Output
IP: 182.44.67.97, Status: 301
IP: 43.157.179.227, Status: 200
...

🎯 Project Goal

The purpose of this repository is to:

Practice Python file handling, text processing, and regex

Build tools for log parsing and analysis

Expand into a collection of scripts that demonstrate real-world Python use cases for system administration and
cybersecurity

📌 Roadmap

Basic Nginx log reader (current)

Extend parsing (date, request, user agent, referrer, etc.)

Add filtering and statistics (e.g., 404 errors, most common IPs)

Implement support for other log formats (Apache, system logs, etc.)

Provide CSV/JSON export functionality
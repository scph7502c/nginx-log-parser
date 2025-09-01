import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

NGINX_LOG_FILE = os.environ.get("NGINX_LOG_FILE")
log_line = []
log_list = []


def read_whole_log_file(filename):
    contents = path.read_text()
    contents = contents.rstrip()
    print(contents)


def sanitize_line(line):
    line = line.strip()
    line = line.split(" ")
    return line


def read_line_by_line_log_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            sanitized_line = sanitize_line(line)
            log_line.append(sanitized_line)
            print(f"IP: {line[0]}, status code: {line[8]}")
            log_list.append(sanitized_line)
            log_line.clear()
    for line in log_list:
        print(line)


if __name__ == "__main__":
    path = Path(NGINX_LOG_FILE)
    read_line_by_line_log_file(path)

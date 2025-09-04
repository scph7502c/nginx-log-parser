import os
import re
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# to do: create function to get names ov various nginx log files, fe. my-website.access.log, some-website.access.log, my-website.error.log etc.
NGINX_ACCESS_LOG_FILE = os.environ.get("NGINX_ACCESS_LOG_FILE")
NGINX_ERROR_LOG_FILE = os.environ.get("NGINX_ERROR_LOG_FILE")
log_files = (NGINX_ACCESS_LOG_FILE, NGINX_ERROR_LOG_FILE)
log_line = []
log_list = []

log_pattern = re.compile(
    r"^(?P<ip>\S+) (?P<identd>\S+) (?P<user>\S+) (\[(?P<time_local>[^]]+)]) \"(?P<request>[^\"]*)\""
)

today_date = datetime.today().strftime("%Y-%m-%d")
print(today_date)


def print_nginx_log_dir_content(nginx_log_dir):
    # curr_working_dir = os.getcwd()
    try:
        log_files_in_dir = os.listdir(nginx_log_dir)
        print(log_files_in_dir)
        for l in log_files_in_dir:
            print(l)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except NotADirectoryError:
        print("Not a directory!")


def read_whole_log_file(filename):
    contents = path.read_text()
    contents = contents.rstrip()
    return contents


def create_log_list_of_lists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            log_list.append(create_log_dict_of_lists(line, log_pattern))
    for l in log_list:
        print(l)
    return log_list


def create_log_dict_of_lists(log_lists_line, pattern):

    match = log_pattern.match(log_lists_line)
    return match.groupdict()


def main():
    while True:
        print("****NGINX LOG PARSER****")

        log_dir = input("Enter log files path: ")
        print("1. Analyze chosen log file")
        print("2. Exit")

        user_choice = input("Choose your option: ")

        if user_choice == "1":
            if log_dir != "":
                print(log_dir)
                print_nginx_log_dir_content(log_dir)
            else:
                print("You have to enter log file path!")
        elif user_choice == "2":
            print("Bye!")
            exit(0)


if __name__ == "__main__":
    path = Path(NGINX_ACCESS_LOG_FILE)
    create_log_list_of_lists(path)
    # print_current_dir()
    # main()

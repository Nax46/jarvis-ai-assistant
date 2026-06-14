from datetime import datetime


class Logger:

    @staticmethod
    def info(message):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[INFO] [{current_time}] {message}")

    @staticmethod
    def error(message):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[ERROR] [{current_time}] {message}")
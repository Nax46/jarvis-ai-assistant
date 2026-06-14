import webbrowser
from utils.logger import Logger


class BrowserControl:

    @staticmethod
    def open_youtube():
        Logger.info("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    @staticmethod
    def open_google():
        Logger.info("Opening Google")
        webbrowser.open("https://www.google.com")

    @staticmethod
    def open_github():
        Logger.info("Opening GitHub")
        webbrowser.open("https://github.com")

    @staticmethod
    def open_chatgpt():
        Logger.info("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")
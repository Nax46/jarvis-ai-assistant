from utils.logger import Logger
from core.command_router import CommandRouter


class Jarvis:

    def __init__(self):
        self.name = "Jarvis"
        self.router = CommandRouter()

    def start(self):
        Logger.info("Jarvis Started")

        print(f"{self.name} Initialized Successfully")
        print(f"{self.name} is Ready")
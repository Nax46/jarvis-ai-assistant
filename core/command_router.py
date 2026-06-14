from automation.app_control import AppControl
from automation.browser_control import BrowserControl


class CommandRouter:

    def __init__(self):
        print("Command Router Ready")

    def route(self, command):

        command = command.lower()

        if "chrome" in command:
            AppControl.open_chrome()

        elif "notepad" in command:
            AppControl.open_notepad()

        elif "calculator" in command or "calc" in command:
            AppControl.open_calculator()

        elif "vscode" in command or "vs code" in command:
            AppControl.open_vscode()
            
        elif "youtube" in command:
            BrowserControl.open_youtube()

        elif "google" in command:
            BrowserControl.open_google()

        elif "github" in command:
            BrowserControl.open_github()

        elif "chatgpt" in command:
            BrowserControl.open_chatgpt()   

        else:
            print("Unknown command")
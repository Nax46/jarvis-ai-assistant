from automation.app_control import AppControl


class CommandRouter:

    def __init__(self):
        print("Command Router Ready")

    def route(self, command):

        command = command.lower()

        if "chrome" in command:
            print("Chrome command detected")
            AppControl.open_chrome()

        elif "youtube" in command:
            print("YouTube command detected")

        else:
            print("Unknown command")
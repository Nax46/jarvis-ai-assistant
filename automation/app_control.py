import subprocess


class AppControl:

    @staticmethod
    def open_chrome():
        subprocess.Popen("start chrome", shell=True)
        print("Opening Chrome...")

    @staticmethod
    def open_notepad():
        subprocess.Popen("notepad")
        print("Opening Notepad...")

    @staticmethod
    def open_calculator():
        subprocess.Popen("calc")
        print("Opening Calculator...")

    @staticmethod
    def open_vscode():
        subprocess.Popen("code", shell=True)
        print("Opening VS Code...")
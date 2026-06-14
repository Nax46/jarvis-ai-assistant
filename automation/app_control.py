import subprocess
from voice.speaker import Speaker


class AppControl:

    @staticmethod
    def open_chrome():

        Speaker.speak("Opening Chrome Sir")

        subprocess.Popen(
            "start chrome",
            shell=True
    )

    @staticmethod
    def open_notepad():
        Speaker.speak("Opening Notepad Sir")

        subprocess.Popen("notepad")

    @staticmethod
    def open_calculator():
        Speaker.speak("Opening Calculator Sir")

        subprocess.Popen("calc")

    @staticmethod
    def open_vscode():
        Speaker.speak("Opening Visual Studio Code Sir")

        subprocess.Popen(
            "code",
            shell=True
    )
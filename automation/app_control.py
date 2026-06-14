import subprocess


class AppControl:

    @staticmethod
    def open_chrome():
        try:
            subprocess.Popen("start chrome", shell=True)
            print("Opening Chrome...")

        except Exception as e:
            print(f"Error: {e}")
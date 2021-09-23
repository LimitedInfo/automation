import webbrowser
import os
import subprocess
import pyperclip


def main():

    os.system(r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.2\bin\pycharm64.exe")
    # out = os.system(r"cd C:\Users\Andrew\PycharmProjects\personalWebsite")
    # out = subprocess.Popen(["set", "FLASK_ENV=development"])
    # out = subprocess.Popen(["flask", "run"])
    pyperclip.copy('set FLASK_ENV=development\nflask run')
    webbrowser.open('http://127.0.0.1:5000/')
    webbrowser.open('https://www.nickderobertis.com/', new=2)


if __name__ == '__main__':
    main()


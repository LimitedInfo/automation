# This is a sample Python script.
import webbrowser
import os
import subprocess
import pyperclip
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    os.system(r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.2\bin\pycharm64.exe")
    # out = os.system(r"cd C:\Users\Andrew\PycharmProjects\personalWebsite")
    # out = subprocess.Popen(["set", "FLASK_ENV=development"])
    # out = subprocess.Popen(["flask", "run"])
    pyperclip.copy('set FLASK_ENV=development\nflask run')
    webbrowser.open('http://127.0.0.1:5000/')
    webbrowser.open('https://www.nickderobertis.com/', new=2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

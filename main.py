import pyperclip
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import pygetwindow as gw
import keyboard
import pyautogui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 250)  # 设置界面大小
        self.setWindowTitle("Process String from Youdao Dict")

        # 创建按钮
        button = QPushButton("Process String", self)
        button.setGeometry(100, 100, 200, 50)  # 设置按钮位置和大小
        button.clicked.connect(processStr)  # 绑定按钮点击事件

        self.show()


def processStr():
    text = pyperclip.paste()
    if isinstance(text, str):
        components = text.split()
        num = len(components)
        res = ""
        if num > 0:
            for i in range(0, num - 1, 2):
                if (i < num) and (i + 1 < num):
                    res += components[i] + components[i + 1] + "\n"
        if len(res) > 0 and res.endswith("\n"):
            res = res[:-1]
        pyperclip.copy(res)


def getActiveWindowTitle():
    # 获取当前活跃窗口
    active_window = gw.getActiveWindow()
    if hasattr(active_window, "title"):
        return active_window.title
    else:
        return ""


def on_ctrl_c():
    # print("Ctrl+C was pressed!")
    # 因为前一次Ctrl+C已经用于触发，所以现在再向机器输入一次Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    doProcessStr()


def doProcessStr():
    # print(pyperclip.paste())
    # print(getActiveWindowTitle())
    if getActiveWindowTitle() == "网易有道翻译":
        processStr()


def main():
    # app = QApplication([])
    # ui = MainWindow()
    # sys.exit(app.exec_())

    keyboard.add_hotkey('ctrl+c', on_ctrl_c)
    while True:
        keyboard.wait('ctrl+c') # 单次Ctrl+C会起到触发的作用，但是不会具有复制的作用（因为Ctrl+C已经用掉了，用于触发了），这里存在冒险竞争


if __name__ == "__main__":
    main()

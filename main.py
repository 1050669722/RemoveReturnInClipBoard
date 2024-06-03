import pyperclip
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


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


def main():
    app = QApplication([])
    ui = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

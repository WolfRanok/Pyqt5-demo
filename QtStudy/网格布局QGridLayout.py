from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计算器")

        # 整体的布局器
        layout = QVBoxLayout()

        edit = QLineEdit()  # 文本输入框
        edit.setPlaceholderText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    app.exec_()

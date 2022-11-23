from PyQt5.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QWidget窗体展示')
        self.resize(290,50)
        label = QLabel('hello，PyQt5！', self)  # 设置父窗体
        label.setStyleSheet("font-size:30px;color:red")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

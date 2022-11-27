import sys
from PyQt5.QtWidgets import *
from threading import Thread
import time


class MyThread(Thread):
    num = 1

    def run(self):
        self.t = MyThread.num
        MyThread.num += 1
        for _ in range(5):
            print(self.t, '线程正在工作')
            time.sleep(0.5)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.my_theard = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        lineEdit = QLineEdit()
        layout.addWidget(lineEdit)

        bnt = QPushButton()
        bnt.clicked.connect(self.clicked_fun)
        layout.addWidget(bnt)

    def clicked_fun(self):
        self.my_theard.append(MyThread())  # 创建多线程
        self.my_theard[-1].start()  # 开始线程


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

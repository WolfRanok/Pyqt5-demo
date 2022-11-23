from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    # 自定义信号必须放在函数的外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout()
        self.resize(150, 100)
        bnt = QPushButton('测试按钮', self)

        # 将按钮的点击信号绑定函数
        bnt.clicked.connect(self.fun1)

        # 将槽函数与自定义信号链接
        self.my_signal.connect(self.fun2)


    def fun2(self, name):
        print("这里是与my_signal绑定的函数" + name)

    def fun1(self):
        # 触发该函数
        self.my_signal.emit('function1')
        self.my_signal.emit('function2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

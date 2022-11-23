from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout()
        self.resize(300, 200)
        bnt = QPushButton('测试按钮', self)
        bnt.clicked.connect(self.bnt_my_clicked)
        self.setLayout(self.layout)

    def bnt_my_clicked(self):
        label = QLabel('已点击一次按钮',self)
        self.layout.addWidget(label)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

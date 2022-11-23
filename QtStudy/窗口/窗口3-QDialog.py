import sys
from PyQt5.QtWidgets import *


# 对话框窗口
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_bnt = QPushButton("确定",self)
        ok_bnt.setGeometry(50,20,100,200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyDialog()
    w.show()
    app.exec_()
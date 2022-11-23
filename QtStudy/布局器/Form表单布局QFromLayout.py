from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 外层容器使用纵向的布局
        layout = QVBoxLayout()

        # 表单容器
        form_layout = QFormLayout()

        edit = QLineEdit()
        edit.setPlaceholderText('账号注册')
        form_layout.addRow('账号',edit)

        edit2 = QLineEdit()
        edit.setPlaceholderText('密码')
        form_layout.addRow('账号',edit2)

        layout.addLayout(form_layout)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    app.exec_()

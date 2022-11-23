from PyQt5.QtWidgets import *
import sys


## 模拟计算机的ui
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计算器")

        # 整体的布局器
        layout = QVBoxLayout()

        edit = QLineEdit()  # 文本输入框
        edit.setPlaceholderText('请输入内容')
        layout.addWidget(edit)

        # 网格布局
        grid = QGridLayout()
        data = (
            ('7', '8', '9', '+', '-'),
            ('4', '5', '6', '*', '/'),
            ('1', '2', '3', '(', ')'),
            ('0', '.', '=', '/', 'C')
        )

        for i, a in enumerate(data):
            for j, ch in enumerate(a):
                bnt = QPushButton(ch)
                grid.addWidget(bnt, i + 1, j + 1)  # 按行列添加按钮

        layout.addLayout(grid)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    app.exec_()

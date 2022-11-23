from PyQt5.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口大小
        self.init_ui()

    def init_ui(self):
        self.resize(500, 500)
        self.setWindowTitle('布局器样式展示')

        # 创建垂直布局器
        layout = QVBoxLayout()
        # 设置第一个组
        group1 = QGroupBox("语言")

        hobby_box = QVBoxLayout()
        hobby_box.addWidget(QRadioButton("python"))
        hobby_box.addWidget(QRadioButton("C++"))
        hobby_box.addWidget(QRadioButton("Java"))

        group1.setLayout(hobby_box)
        layout.addWidget(group1)

        # 设计第二个组
        group2 = QGroupBox("选择")
        hobby_box2 = QHBoxLayout()
        hobby_box2.addWidget(QRadioButton("学"))
        hobby_box2.addWidget(QRadioButton("不学"))

        group2.setLayout(hobby_box2)
        layout.addWidget(group2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    app.exec_()

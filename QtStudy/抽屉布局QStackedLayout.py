from PyQt5.QtWidgets import *
import sys


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        QLabel('hi，Python', self)
        # 设置背景颜色
        self.setStyleSheet("background-color:green;")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        QLabel('hi，C++', self)
        # 设置背景颜色
        self.setStyleSheet("background-color:red;")


# 类似于在主窗口中的子窗口（像电视机）点击不同
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        self.stacked_loyout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()

        # 将两个窗体放入到抽屉中
        self.stacked_loyout.addWidget(win1)
        self.stacked_loyout.addWidget(win2)

    # 设置整体窗口界面
    def init_ui(self):
        # 创建一个整体的布局器
        self.resize(200, 300)
        container = QVBoxLayout()

        # 抽屉显示的机界面并调整背景
        widget = QWidget()
        widget.setLayout(self.stacked_loyout)  # 这一步很关键
        widget.setStyleSheet("background-color:grey;")  # 设置样式

        btn_press1 = QPushButton('抽屉1')
        btn_press2 = QPushButton('抽屉2')

        # 为两个按钮绑定点击事件
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)

        # 将设置好的界面和两个按钮放入主界面中
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)
        self.setLayout(container)

    def btn_press1_clicked(self):
        self.stacked_loyout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        self.stacked_loyout.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()
    app.exec_()

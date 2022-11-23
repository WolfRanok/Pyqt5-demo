import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt


class MyWindow(QWidget):
    # 声明信号 只能放在函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.text_lest = []  # 用于之后存放文字
        self.init_ui()

    def init_ui(self):
        self.resize(440, 300)
        # 创建建一个整体布局器
        container = QVBoxLayout()

        # 用于显示信息
        self.msg = QLabel("")
        self.msg.resize(400, 15)
        self.msg.setWordWrap(True)  # 自动换行
        self.msg.setAlignment(Qt.AlignTop)  # 靠上
        self.msg.setStyleSheet("color:black;font-size:20px")

        # 设置滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局器，用于添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 添加水平布局器用于存放按钮
        h_layout = QVBoxLayout()
        bnt = QPushButton("添加文本", self)
        # 绑定点击事件，点击测开始添加文本
        bnt.clicked.connect(self.check)
        h_layout.addStretch(1)  # 伸缩器
        h_layout.addWidget(bnt)
        h_layout.addStretch(1)

        # 将布局器添加到总体的布局器中
        container.addLayout(v_layout)
        container.addLayout(h_layout)
        self.setLayout(container)

        # 绑定信号与槽
        self.my_signal.connect(self.my_slot)
    def my_slot(self, smg):
        self.text_lest.append(smg)
        # 更新内容
        self.msg.setText('<br>'.join(self.text_lest))
        self.msg.resize(400, self.msg.frameSize().height() + 15)  # 动态改变label的高度
        self.msg.repaint()  # 更新内容

    def check(self):
        for _ in range(10):
            self.my_signal.emit("hello" + random.choice(['c', 'c++', 'java', 'python', 'go']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

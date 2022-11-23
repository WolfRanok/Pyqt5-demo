from PyQt5.QtWidgets import *
import sys


# 不常用
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QMainWindow')
        self.resize(290, 50)

        label = QLabel('hello,python')
        label.setStyleSheet('font-size:30px;color:red')

        menu = self.menuBar()
        # 在窗口中显示菜单栏
        menu.setNativeMenuBar(False)

        # 添加菜单栏的第一个内容‘文件’
        file_menu = menu.addMenu('文件')
        # 添加选项
        file_menu.addAction('新建')
        file_menu.addAction('打开')
        file_menu.addAction('保存')

        # 菜单栏中添加第二个内容‘编辑’
        edit_menu = menu.addMenu('编辑')
        edit_menu.addAction('复制')
        edit_menu.addAction('粘贴')
        edit_menu.addAction('剪切')

        # 设置中心显示
        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

import json
import sys
import time
import requests
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import *
from MyUi import Ui_Form


class LoginThread(QThread):
    # 在此处创建一个自定义信号
    start_login_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def login_by_requests(self,user_password_json):
        # 将字符串对象转换为json格式的对象
        user_password_json = json.loads(user_password_json)
        print("已发送登录请求",user_password_json)
        # 这里发送一个requests请求，使用爬虫技术实现
        resource = requests.post(url=" https://1hew6hzryk65t.cfc-execute.bj.baidubce.com/ranok",json={"body":{"user_name":"ranok","password":"ranok666"}})
        print("接收到的百度服务器响应：",resource.content.decode())


    def run(self):
        # 这里是一直在运行的子线程
        while True:
            print("线程正在工作~~")
            time.sleep(1)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 利用.ui文件生成的类对象，来创建窗口对象
        self.ui = QWidget()
        Ui_Form().setupUi(self.ui)

        # 根据id查找对应的控件
        self.pushButton = self.ui.findChild(QPushButton, 'pushButton')
        self.login_edit = self.ui.findChild(QLineEdit, 'lineEdit')
        self.password_edit = self.ui.findChild(QLineEdit, 'lineEdit_2')

        # 新建进程对象
        self.login_thread = LoginThread()
        # 让线程开始工作
        self.login_thread.start()

        self.init_ui()

    def init_ui(self):
        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.login)

        # 为自定义信号绑定槽函数
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)


    def login(self):
        # 获取用户的账号和密码
        user_name = self.login_edit.text()
        password = self.password_edit.text()

        # 触发信号，并传递参数
        self.login_thread.start_login_signal.emit(json.dumps({"user_name": user_name, "password": password}))

        print(user_name, password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()

    w.ui.show()
    app.exec_()

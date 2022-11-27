import json
import sys
import time
import requests
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import *
from MyUi import Ui_Form


class LoginThread(QThread):
    # 在此处创建一个自定义信号
    start_login_signal = None

    def __init__(self, signal):
        super().__init__()
        self.start_login_signal = signal

    def login_by_requests(self, user_password_json):
        # 将字符串对象转换为json格式的对象
        user_password_json = json.loads(user_password_json)
        print("已发送登录请求", user_password_json)
        # 这里发送一个requests请求，使用爬虫技术实现
        # 这里使用json，会使得传入的参数保持json的格式转为字符串例如
        # 如果是data则会将参数以&串联例如“user_name=ranok&password=ranok666”
        resource = requests.post(url="https://1hew6hzryk65t.cfc-execute.bj.baidubce.com/ranok",
                                 json=user_password_json)
        resource = resource.json()
        print(resource)
        self.start_login_signal.emit(json.dumps(resource))

    def run(self):
        # 这里是一直在运行的子线程
        while True:
            print("线程正在工作~~")
            time.sleep(1)


class MyWindow(QWidget):
    login_status_signal = pyqtSignal(str)  # 用于接收返回的信号请求
    login_send_out = pyqtSignal(str)  # 用于发送请求的信号

    def __init__(self):
        super().__init__()
        # 利用.ui文件生成的类对象，来创建窗口对象
        self.ui = QWidget()
        Ui_Form().setupUi(self.ui)

        # 根据id查找对应的控件
        self.pushButton = self.ui.findChild(QPushButton, 'pushButton')
        self.login_edit = self.ui.findChild(QLineEdit, 'lineEdit')
        self.password_edit = self.ui.findChild(QLineEdit, 'lineEdit_2')
        self.textBrowser = self.ui.findChild(QTextBrowser, "textBrowser")
        # self.textBrowser.setText("登陆成功")

        # 新建进程对象，并将信号传入
        self.login_thread = LoginThread(self.login_status_signal)

        # 让线程开始工作
        self.login_thread.start()

        self.init_ui()

    def login_status(self, status):
        """
        专门用来处理服务器返回请求
        :param status:
        :return:
        """
        status = json.loads(status)
        data = status['body']
        print("接收到的百度服务器响应：", data['return'])
        self.textBrowser.setText(data['return'])  # 将对应文本显示在textBrowser对象中
        # self.textBrowser.repaint()  # 刷新界面

    def init_ui(self):
        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.login)

        # 绑定槽函数
        self.login_send_out.connect(self.login_thread.login_by_requests)  # 处理发送请求的函数
        self.login_status_signal.connect(self.login_status)  # 处理客户端接收服务器返回的数据函数

    def login(self):
        # 获取用户的账号和密码
        user_name = self.login_edit.text()
        password = self.password_edit.text()

        # 触发信号，并传递参数
        self.login_send_out.emit(json.dumps({"user_name": user_name, "password": password}))

        print(user_name, password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()

    w.ui.show()
    app.exec_()

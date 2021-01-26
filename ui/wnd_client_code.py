from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QLabel, QMessageBox
import socket

from ui.wnd_client import Ui_WndClient
from res import qres
import mf

class WndClient(QMainWindow, Ui_WndClient):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_status_bar()
        self.init_all_controls()
        self.init_all_sig_slot()
        if self.init_tcp_client():
            self.show_info("窗口初始化成功")
        else:
            self.show_info("窗口初始化失败")

    def init_status_bar(self):
        self.lbe_info = QLabel()
        self.status_bar.addWidget(self.lbe_info)

    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/login.png"), "登录")
        self.tool_bar.addAction(QIcon(":/register.png"), "注册")
        self.tool_bar.addAction(QIcon(":/pay.png"), "充值")
        self.tool_bar.addAction(QIcon(":/modify.png"), "改密")

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_login.clicked.connect(self.on_btn_login_clicked)

    def init_tcp_client(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.show_info("正在连接服务器...")
        self.err_no = self.tcp_socket.connect_ex((mf.server_ip, mf.server_port))
        if self.err_no != 0:
            self.show_info(f"连接服务器失败, 错误码: {self.err_no}")
            return False
        self.show_info(f"连接服务器成功")
        return True

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        if action_name == "登录":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "注册":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "充值":
            self.stack_widget.setCurrentIndex(2)
        elif action_name == "改密":
            self.stack_widget.setCurrentIndex(3)

    def on_btn_login_clicked(self):
        if self.err_no != 0:
            QMessageBox.information(self, "错误", f"连接服务器失败:{self.err_no}")
            return
        account = self.edt_account.text()
        pwd = self.edt_pwd.text()
        send_data = account.encode()
        self.tcp_socket.send(send_data)
        self.show_info("客户端发送数据成功")

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        print(text)


import sys
from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    wnd_client = WndClient()
    wnd_client.show()

    sys.exit(app.exec_())
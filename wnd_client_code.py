from PySide2.QtGui import QIcon, QCloseEvent, QRegExpValidator
from PySide2.QtWidgets import QMainWindow, QLabel, QMessageBox
from PySide2.QtCore import QRegExp
import socket
from threading import Thread
import json
import hashlib

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
        self.move(1130, 300)
        self.show_info("窗口初始化成功")

    def closeEvent(self, event: QCloseEvent):
        tcp_socket.close()

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        print(text)

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
        # 正则表达式
        reg_exp_acount_pwd = QRegExp("[a-zA-Z0-9]+")
        reg_exp_qq_number = QRegExp("\d+")
        # 登录页
        self.edt_login_account.setValidator(QRegExpValidator(reg_exp_acount_pwd))
        self.edt_login_pwd.setValidator(QRegExpValidator(reg_exp_acount_pwd))
        # 注册页
        self.edt_reg_account.setValidator(QRegExpValidator(reg_exp_acount_pwd))
        self.edt_reg_pwd.setValidator(QRegExpValidator(reg_exp_acount_pwd))
        self.edt_reg_qq.setValidator(QRegExpValidator(reg_exp_qq_number))

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_login.clicked.connect(self.on_btn_login_clicked)
        self.btn_reg.clicked.connect(self.on_btn_reg_clicked)

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
        login_account = self.edt_login_account.text()
        login_pwd = self.edt_login_pwd.text()
        bool_list = [
            len(login_account) in range(6, 13),
            len(login_pwd) in range(6, 13),
        ]
        if False in bool_list:
            self.show_info("登录失败, 账号密码长度不符合要求")
            return
        # 把客户端信息整理成字典, 发送给服务器
        login_pwd = mf.get_encrypted_str(login_pwd.encode())
        client_info_dict = {
            "msg_type": "login",
            "account": login_account,
            "pwd": login_pwd,
        }
        send_to_server(client_info_dict)

    def on_btn_reg_clicked(self):
        # 判断注册信息是否符合要求
        reg_account = self.edt_reg_account.text()
        reg_pwd = self.edt_reg_pwd.text()
        reg_qq = self.edt_reg_qq.text()
        bool_list = [
            len(reg_account) in range(6,13),
            len(reg_pwd) in range(6, 13),
            len(reg_qq) in range(5, 11)
        ]
        if False in bool_list:
            self.show_info("注册失败, 账号密码6-12位, QQ号5-10位")
            return
        # 把客户端信息整理成字典
        reg_pwd = mf.get_encrypted_str(reg_pwd.encode())
        reg_qq = mf.get_encrypted_str(reg_pwd.encode())
        client_info_dict = {
            "msg_type": "reg",
            "account": reg_account,
            "pwd": reg_pwd,
            "qq": reg_qq,
            "machine_code": machine_code,
            "reg_ip": reg_ip,
        }
        send_to_server(client_info_dict)

def send_to_server(client_info_dict: dict):
    # py字典 转 json字符串
    json_str = json.dumps(client_info_dict, ensure_ascii=False)
    # 发送客户端注册信息到服务器
    try:
        tcp_socket.send(json_str.encode())
        wnd_client.show_info("发送客户端注册信息成功")
    except Exception as e:
        wnd_client.show_info(f"发送客户端注册信息失败: {e}")

def thd_recv_server():
    while True:
        print("等待服务端发出消息中...")
        try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
            recv_bytes = tcp_socket.recv(1024)
        except:
            recv_bytes = ""
        if not recv_bytes:  # 若客户端退出,会收到一个空str
            break
        # json字符串 转 py字典
        json_str = recv_bytes.decode()
        server_info_dict = json.loads(json_str)
        print(f"收到服务端的消息: {server_info_dict}")
        # 客户端消息处理
        msg_type = server_info_dict["msg_type"]
        if msg_type == "reg":
            wnd_client.show_info(server_info_dict["detail"])
        elif msg_type == "login":
            wnd_client.show_info(server_info_dict["detail"])
            login_ret = server_info_dict["login_ret"]
            if login_ret:
                wnd_client.close()  # 关闭登录界面
                wnd_client_main = WndClientMain()
                wnd_client_main.show()  # 显示主界面

    wnd_client.show_info("服务端已断开连接...")



import sys
from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt
from wnd_client_main_code import WndClientMain

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    wnd_client = WndClient()
    wnd_client.show()

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("正在连接服务器...")
    err_no = tcp_socket.connect_ex((mf.server_ip, mf.server_port))
    if err_no != 0:
        QMessageBox.critical(wnd_client, "错误", f"连接服务器失败, 错误码: {err_no}")
        sys.exit(-1)
    print(f"连接服务器成功, 开始接收数据...")
    Thread(target=thd_recv_server).start()

    machine_code = mf.get_machine_code()
    reg_ip = mf.get_outer_ip()

    sys.exit(app.exec_())
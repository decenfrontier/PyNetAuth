import sys
import socket
from threading import Thread, Lock
import json
import base64
import time
import webbrowser

from PySide2.QtGui import QIcon, QCloseEvent, QRegExpValidator, QPixmap, \
    QMouseEvent, QPaintEvent, QPainter, QBitmap
from PySide2.QtWidgets import QDialog, QLabel, QMessageBox, QToolBar, QVBoxLayout, \
    QStatusBar, QApplication, QStyleFactory
from PySide2.QtCore import Qt, QRegExp, QSize, QPoint, Signal

from client.qtres import qres
from client.ui.wnd_client_login import Ui_WndClientLogin
from wnd_client_main_code import WndClientMain
from client import mf, my_crypto
from client import cfg

class WndClientLogin(QDialog, Ui_WndClientLogin):
    sig_accept = Signal()
    sig_reject = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_wnd()
        self.init_status_bar()
        if self.init_net_auth():
            self.init_all_controls()
            self.init_all_sig_slot()
            self.show_info("初始化登录窗口成功")
        else:
            self.show_info("初始化登录窗口失败")
            self.close()

    def closeEvent(self, event: QCloseEvent):
        print("登录窗口即将关闭")

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        mf.log_info(text)

    # 初始化网络验证
    def init_net_auth(self):
        if not self.send_recv_init():
            return False
        if not self.send_recv_proj():
            return False
        return True

    def init_wnd(self):
        self.setAttribute(Qt.WA_DeleteOnClose)  # 窗口关闭时删除对象
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框, 但任务栏有图标
        self.start_point = QPoint(0, 0)  # 使窗口支持拖动移动

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_point = self.frameGeometry().topLeft() - event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent):
        self.move(event.globalPos() + self.start_point)

    def paintEvent(self, event: QPaintEvent):
        # 背景
        pix_map = QPixmap(":/back1.jpg").scaled(self.size())
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(self.rect(), pix_map)
        # 圆角
        bmp = QBitmap(self.size())
        bmp.fill()
        painter = QPainter(bmp)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(bmp.rect(), 8, 8)
        self.setMask(bmp)

    def init_status_bar(self):
        # 添加一个statusbar
        self.status_bar = QStatusBar()
        # 添加标签
        self.lbe_info = QLabel()
        self.status_bar.addWidget(self.lbe_info)


    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # ----------------- 工具栏 -------------------
        # 添加工具栏
        self.tool_bar = QToolBar()
        self.tool_bar.setIconSize(QSize(28, 28))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/login.png"), "登录")
        self.tool_bar.addAction(QIcon(":/register.png"), "注册")
        self.tool_bar.addAction(QIcon(":/pay.png"), "充值")
        self.tool_bar.addAction(QIcon(":/modify.png"), "改密")
        self.tool_bar.addAction(QIcon(":/notice.png"), "公告")
        # 布局
        vbox_layout = QVBoxLayout()
        vbox_layout.setMargin(4)
        vbox_layout.addWidget(self.tool_bar)
        vbox_layout.addWidget(self.stack_widget)
        vbox_layout.addWidget(self.status_bar)
        self.setLayout(vbox_layout)
        # ------------------ 设置编辑框格式 -----------------
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
        # ------------------ 设置标签格式 -----------------
        # 充值页
        self.lbe_pay_key.setText(f"<a href={mf.url_card}>充值卡号: </a>")
        self.lbe_pay_key.setOpenExternalLinks(True)
        self.lbe_pay_key.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        # 公告页
        self.lbe_notice_text.setText(f"{mf.notice}")
        # 弹出更新网址
        if mf.client_ver != mf.latest_ver:
            ret = QMessageBox.information(self, "提示", "发现新版本, 是否前往下载?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if ret == QMessageBox.Yes:
                webbrowser.open(mf.url_update)
        # ------------------ 设置按钮状态 -----------------
        self.btn_login.setEnabled(mf.allow_login)
        self.btn_reg.setEnabled(mf.allow_reg)
        self.btn_unbind.setEnabled(mf.allow_unbind)

    def init_all_sig_slot(self):
        self.sig_accept.connect(self.accept)
        self.sig_reject.connect(self.reject)
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_login.clicked.connect(self.on_btn_login_clicked)
        self.btn_reg.clicked.connect(self.on_btn_reg_clicked)
        self.btn_exit.clicked.connect(self.on_btn_exit_clicked)
        self.btn_pay.clicked.connect(self.on_btn_pay_clicked)
        self.btn_unbind.clicked.connect(self.on_btn_unbind_clicked)
        self.btn_modify.clicked.connect(self.on_btn_modify_clicked)

    def send_recv_init(self):
        client_info_dict = {"消息类型": "初始",
                            "内容": {"通信密钥": mf.aes_key}}
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 1")
            return False
        if msg_type == "初始":
            if server_content_dict["结果"]:
                enc_aes_key = server_content_dict["详情"]
                # 重新构造新的aes密钥
                mf.aes_key = my_crypto.decrypt_rsa(my_crypto.private_key_client, enc_aes_key)
                mf.aes = my_crypto.AesEncryption(mf.aes_key)
                return True
            else:
                detail = server_content_dict["详情"]
                QMessageBox.information(self, "错误", detail)
        return False

    def send_recv_proj(self):
        client_info_dict = {"消息类型": "锟斤拷",
                            "内容": {"版本号": mf.client_ver}}
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 2")
            return False
        if msg_type == "锟斤拷":
            if server_content_dict["结果"]:
                detail_dict = server_content_dict["详情"]
                mf.notice = detail_dict["客户端公告"]
                mf.url_update = detail_dict["更新网址"]
                mf.url_card = detail_dict["发卡网址"]
                mf.allow_login = detail_dict["允许登录"]
                mf.allow_reg = detail_dict["允许注册"]
                mf.allow_unbind = detail_dict["允许解绑"]
                mf.latest_ver = detail_dict["最新版本"]
                return True
            else:
                detail = server_content_dict["详情"]
                QMessageBox.information(self, "错误", detail)
        return False

    def send_recv_custom1(self):
        client_info_dict = {"消息类型": "烫烫烫",
                            "内容": {"烫烫烫": "烫烫烫"}}
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 3")
            return False
        if msg_type == "烫烫烫":
            detail_dict = server_content_dict["详情"]
            mf.pwd_pic = mf.aes.decrypt(detail_dict["pic"])
            mf.pwd_zk = mf.aes.decrypt(detail_dict["zk"])
            return True
        return False

    def send_recv_custom2(self):
        client_info_dict = {"消息类型": "屯屯屯",
                            "内容": {"屯屯屯": "屯屯屯"}}
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 4")
            return False
        if msg_type == "屯屯屯":
            detail_dict = server_content_dict["详情"]
            mf.addr_crack = mf.aes.decrypt(detail_dict["crk"])
            return True
        return False

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
        elif action_name == "公告":
            self.stack_widget.setCurrentIndex(4)

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
        login_pwd = my_crypto.get_encrypted_str(login_pwd.encode())
        login_system = mf.get_operation_system()
        # 把客户端信息整理成字典, 发送给服务器
        client_info_dict = {
            "消息类型": "登录",
            "内容": {
                "账号": login_account,
                "密码": login_pwd,
                "机器码": mf.machine_code,
                "操作系统": login_system,
            }
        }
        # 发送客户端消息
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if msg_type == "登录":
            self.show_info(server_content_dict["详情"])
            if server_content_dict["结果"]:
                mf.user_account = server_content_dict["账号"]
                if self.send_recv_custom1() and self.send_recv_custom2():
                    self.sig_accept.emit()  # 登录界面接受
                else:
                    self.sig_reject.emit()  # 登录界面拒绝

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
        reg_pwd = my_crypto.get_encrypted_str(reg_pwd.encode())
        client_info_dict = {
            "消息类型": "注册",
            "内容": {
                "账号": reg_account,
                "密码": reg_pwd,
                "QQ": reg_qq,
            }
        }
        # 发送客户端消息
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if msg_type == "注册":
            self.show_info(server_content_dict["详情"])

    def on_btn_exit_clicked(self):
        self.close()

    def on_btn_pay_clicked(self):
        account = self.edt_pay_account.text()
        card_key = self.edt_pay_key.text()
        if len(card_key) != 30 or len(account) not in range(6,13):
            self.show_info("账号或卡密错误, 请检查无误后再试")
            return
        client_info_dict = {
            "消息类型": "充值",
            "内容": {
                "账号": account,
                "卡号": card_key,
            }
        }
        ret = QMessageBox.information(self, "提示", f"是否确定充值到以下账号: \n{account}",
                                      QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        # 发送客户端消息
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if msg_type == "充值":
            self.show_info(server_content_dict["详情"])

    def on_btn_unbind_clicked(self):
        account = self.edt_login_account.text()
        pwd = self.edt_login_pwd.text()
        bool_list = [
            len(account) in range(6, 13),
            len(pwd) in range(6, 13),
        ]
        if False in bool_list:
            self.show_info("解绑失败, 请先确保账号密码输入正确")
            return
        pwd = my_crypto.get_encrypted_str(pwd.encode())
        # 允许异地解绑. 不用发机器码
        client_info_dict = {
            "消息类型": "解绑",
            "内容": {
                "账号": account,
                "密码": pwd,
            }
        }
        # 发送客户端消息
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if msg_type == "解绑":
            self.show_info(server_content_dict["详情"])

    def on_btn_modify_clicked(self):
        account = self.edt_modify_account.text()
        qq = self.edt_modify_qq.text()
        new_pwd = self.edt_modify_new_pwd.text()
        bool_list = [
            len(account) in range(6, 13),
            len(new_pwd) in range(6, 13),
            len(qq) in range(5, 10),
        ]
        if False in bool_list:
            self.show_info("改密失败, 请确保数据有效")
            return
        new_pwd = my_crypto.get_encrypted_str(new_pwd.encode())
        client_info_dict = {
            "消息类型": "改密",
            "内容": {
                "账号": account,
                "QQ": qq,
                "密码": new_pwd,
            }
        }
        # 发送客户端消息
        tcp_socket = self.connect_server_tcp()
        self.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = self.recv_from_server(tcp_socket)
        if msg_type == "改密":
            self.show_info(server_content_dict["详情"])

    # 连接服务端tcp
    def connect_server_tcp(self):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        err_no = tcp_socket.connect_ex((mf.server_ip, mf.server_port))
        if err_no != 0:
            QMessageBox.critical(self, "错误", f"连接服务器失败, 错误码: {err_no}")
            raise Exception(f"连接服务器失败, 错误码: {err_no}")
        return tcp_socket

    # 发送数据给服务端
    def send_to_server(self, tcp_socket: socket.socket, client_info_dict: dict):
        # 内容 转 json字符串
        client_info_dict["内容"] = json.dumps(client_info_dict["内容"], ensure_ascii=False)
        # 根据消息类型决定是否对内容aes加密
        if client_info_dict["消息类型"] != "初始":
            # 对json内容进行aes加密
            client_info_dict["内容"] = mf.aes.encrypt(client_info_dict["内容"])
        # 把整个客户端信息字典 转 json字符串
        json_str = json.dumps(client_info_dict, ensure_ascii=False)
        # json字符串 base85编码
        send_bytes = base64.b85encode(json_str.encode())
        try:
            tcp_socket.send(send_bytes)
            print(f"客户端数据, 发送成功: {json_str}")
        except Exception as e:
            mf.log_info(f"客户端数据, 发送失败: {e}")

    # 从服务端接收数据
    def recv_from_server(self, tcp_socket: socket.socket):
        mf.log_info("等待服务端发出消息中...")
        tcp_socket.settimeout(5)  # 设置为非阻塞接收, 只等5秒
        recv_bytes = ""
        try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
            recv_bytes = tcp_socket.recv(4096)
        except:
            ...
        tcp_socket.settimeout(None)  # 重新设置为阻塞模式
        if not recv_bytes:  # 若客户端退出,会收到一个空str
            self.show_info("服务器繁忙, 请稍后再试")
            return "", {}
        # base85解码
        json_str = base64.b85decode(recv_bytes).decode()
        print(f"收到服务端的消息: {json_str}")
        # json字符串 转 py字典
        server_info_dict = json.loads(json_str)
        msg_type = server_info_dict["消息类型"]
        server_content_str = server_info_dict["内容"]
        # 把内容json字符串 转 py字典
        if msg_type != "初始":  # 若不为初始类型的消息, 要先aes解密
            # 先aes解密, 获取json字符串
            server_content_str = mf.aes.decrypt(server_content_str)
        # json字符串 转 py字典
        server_content_dict = json.loads(server_content_str)
        return msg_type, server_content_dict




if __name__ == '__main__':
    # 初始化日志模块
    mf.init_logging()

    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)
    log_info("初始化界面样式完成")

    # 初始化登录窗口
    wnd_client_login = WndClientLogin()
    wnd_client_login.show()
    log_info("初始化登录窗口完成")

    # 初始化json文件
    if not os.path.exists(mf.PATH_GNRL_JSON):
        mf.log_info("自动创建登录界面配置文件")
        mf.py_to_json({"登录界面": cfg.default_login_dict}, mf.PATH_LOGIN_JSON)
    log_info("初始化配置文件完成")

    # 读取配置文件


    if wnd_client_login.exec_() == QDialog.Accepted:
        wnd_client_main = WndClientMain()
        wnd_client_main.show()
        wnd_client_main.start_heart_beat()
        sys.exit(app.exec_())
    sys.exit(0)
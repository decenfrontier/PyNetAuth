import sys, os
import socket
import webbrowser

from PySide2.QtGui import QIcon, QCloseEvent, QRegExpValidator, QPixmap, \
    QMouseEvent, QPaintEvent, QPainter, QBitmap
from PySide2.QtWidgets import QDialog, QLabel, QMessageBox, QToolBar, QVBoxLayout, \
    QStatusBar, QApplication, QStyleFactory
from PySide2.QtCore import Qt, QRegExp, QSize, QPoint, Signal

from client.qtres import qrc_wnd_login
from client.ui.wnd_login import Ui_WndLogin
from client.ui.wnd_main_code import WndMain
from client import mf, my_crypto
from client import cfg

class WndLogin(QDialog, Ui_WndLogin):
    sig_accept = Signal()
    sig_reject = Signal()
    sig_info = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_wnd()
        self.init_status_bar()
        self.init_custom_sig_slot()
        if self.init_net_auth():
            self.init_controls()
            self.init_sig_slot()
            mf.log_info("登录窗口初始化成功")
        else:
            mf.log_info("登录窗口初始化失败")
            self.close()

    def closeEvent(self, event: QCloseEvent):
        self.show_info("登录窗口正在退出...")

    def init_wnd(self):
        self.setAttribute(Qt.WA_DeleteOnClose)  # 窗口关闭时删除对象
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框, 但任务栏有图标
        self.start_point = QPoint(0, 0)  # 使窗口支持拖动移动

    def init_status_bar(self):
        # 添加一个statusbar
        self.status_bar = QStatusBar()
        # 添加标签
        self.lbe_1 = QLabel("<提示> : ")
        self.status_bar.addWidget(self.lbe_1)
        self.lbe_info = QLabel("登录窗口初始化成功")
        self.status_bar.addWidget(self.lbe_info)

    def init_custom_sig_slot(self):
        self.sig_accept.connect(self.accept)
        self.sig_reject.connect(self.reject)
        self.sig_info.connect(lambda text: self.lbe_info.setText(text))

    def show_info(self, text):
        self.sig_info.emit(text)  # 信号槽, 防逆向跟踪
        mf.log_info(text)

    # 初始化网络验证
    def init_net_auth(self):
        tcp_socket = mf.connect_server_tcp()
        if not tcp_socket:
            mf.log_info("服务器繁忙, 请稍后再试")
            QMessageBox.information(self, "错误", "服务器繁忙, 请稍后再试")
            return False
        if self.send_recv_init(tcp_socket) and self.send_recv_proj(tcp_socket):
            return True
        return False



    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_point = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.start_point != QPoint(0, 0):
            self.move(event.globalPos() - self.start_point)

    def paintEvent(self, event: QPaintEvent):
        # 背景
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pix_map = QPixmap(":/back1.jpg").scaled(self.size())
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



    def init_controls(self):
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

    def init_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_login.clicked.connect(self.on_btn_login_clicked)
        self.btn_reg.clicked.connect(self.on_btn_reg_clicked)
        self.btn_exit.clicked.connect(self.on_btn_exit_clicked)
        self.btn_pay.clicked.connect(self.on_btn_pay_clicked)
        self.btn_unbind.clicked.connect(self.on_btn_unbind_clicked)
        self.btn_modify.clicked.connect(self.on_btn_modify_clicked)

    # 发送接收初始消息
    def send_recv_init(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "初始",
                            "内容": {"通信密钥": mf.aes_key}}
        mf.send_to_server(tcp_socket, client_info_dict)
        # 等待服务端响应初始消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
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

    # 发送接收项目消息
    def send_recv_proj(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "锟斤拷",
                            "内容": {"版本号": mf.client_ver}}
        mf.send_to_server(tcp_socket, client_info_dict)
        # 等待服务端响应项目消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
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

    def send_recv_custom1(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "烫烫烫",
                            "内容": {"烫烫烫": "烫烫烫"}}
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 3")
            return False
        if msg_type == "烫烫烫":
            detail_dict = server_content_dict["详情"]
            mf.pwd_pic = mf.aes.decrypt(detail_dict["pic"])
            mf.pwd_zk = mf.aes.decrypt(detail_dict["zk"])
            return True
        return False

    def send_recv_custom2(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "屯屯屯",
                            "内容": {"屯屯屯": "屯屯屯"}}
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
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
        # 把控件信息保存到配置文件
        cfg.cfg_login.controls_to_file()
        # 读取登录账号密码
        login_account = cfg.cfg_login.edt_login_account
        login_pwd = cfg.cfg_login.edt_login_pwd
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
        tcp_socket = mf.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
        if msg_type == "登录":
            self.show_info(server_content_dict["详情"])
            if server_content_dict["结果"]:
                mf.user_account = server_content_dict["账号"]
                if self.send_recv_custom1(tcp_socket) and self.send_recv_custom2(tcp_socket):
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
                "机器码": mf.machine_code,
            }
        }
        # 发送客户端消息
        tcp_socket = mf.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
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
        # 连接服务端
        tcp_socket = mf.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        # 发送客户端消息
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
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
        # 连接服务端
        tcp_socket = mf.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        # 发送客户端消息
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
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
        # 连接服务端
        tcp_socket = mf.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        # 发送客户端消息
        mf.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
        if msg_type == "改密":
            self.show_info(server_content_dict["详情"])




if __name__ == '__main__':
    # 初始化日志模块
    mf.init_logging()
    mf.log_info("初始化日志模块成功")

    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)
    mf.log_info("初始化界面样式完成")

    # 初始化json文件
    if not os.path.exists(mf.PATH_LOGIN_JSON):
        mf.log_info("自动创建登录界面配置文件")
        mf.py_to_json(cfg.default_login_dict, mf.PATH_LOGIN_JSON)
    mf.log_info("初始化配置文件完成")

    # 初始化登录窗口
    mf.wnd_login = WndLogin()
    mf.wnd_login.show()
    mf.log_info("初始化登录窗口完成")

    # 读取登录窗口配置
    cfg.cfg_login.file_to_controls()

    if mf.wnd_login.exec_() == QDialog.Accepted:
        mf.wnd_main = WndMain()
        mf.wnd_main.show()
        mf.wnd_main.start_heart_beat()
        sys.exit(app.exec_())
    sys.exit(0)
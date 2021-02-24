import sys, os
import socket
import webbrowser

from PySide2.QtGui import QIcon, QCloseEvent, QRegExpValidator, QPixmap, \
    QMouseEvent, QPaintEvent, QPainter, QBitmap
from PySide2.QtWidgets import QDialog, QLabel, QMessageBox, QToolBar, QVBoxLayout, \
    QStatusBar, QApplication, QStyleFactory, QLineEdit, QPushButton
from PySide2.QtCore import Qt, QRegExp, QSize, QPoint, Signal

import wnd_login_rc
from ui.wnd_login import Ui_WndLogin
from wnd_main_code import WndMain
import lib_, crypto_

class WndLogin(QDialog, Ui_WndLogin):
    sig_accept = Signal()
    sig_reject = Signal()
    sig_info = Signal(str)
    sig_pass = Signal(bool)
    sig_close = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_instance_field()
        self.init_wnd()
        self.init_status_bar()
        self.init_custom_sig_slot()
        self.show()
        if self.init_net_auth():
            self.init_widgets()
            self.cfg_read()
            self.init_sig_slot()
            self.popup_update_msg()
            self.on_init_success()
            lib_.log_info("登录窗口初始化成功")
        else:
            lib_.log_info("登录窗口初始化失败")
            self.sig_close.emit()

    def closeEvent(self, event: QCloseEvent):
        self.show_info("登录窗口关闭")

    # 读取配置
    def cfg_read(self):
        cfg_load = lib_.json_file_to_dict(lib_.PATH_JSON_LOGIN, lib_.cfg_login)
        lib_.cfg_login.update(cfg_load)

        self.edt_login_account.setText(lib_.cfg_login["账号"])
        self.edt_login_pwd.setText(lib_.cfg_login["密码"])
        self.chk_login_remember.setChecked(lib_.cfg_login["记住账号密码"])
        self.chk_login_update.setChecked(lib_.cfg_login["提示更新版本"])

    # 写入配置
    def cfg_write(self):
        lib_.cfg_login["账号"] = self.edt_login_account.text()
        lib_.cfg_login["密码"] = self.edt_login_pwd.text()
        lib_.cfg_login["记住账号密码"] = self.chk_login_remember.isChecked()
        lib_.cfg_login["提示更新版本"] = self.chk_login_update.isChecked()

        lib_.dict_to_json_file(lib_.cfg_login, lib_.PATH_JSON_LOGIN)

    # 初始化实例属性
    def init_instance_field(self):
        # ---------------------- 状态栏 ----------------------
        self.status_bar = QStatusBar()
        self.lbe_1 = QLabel("<提示> : ")
        self.lbe_info = QLabel("登录窗口初始化成功")
        # ---------------------- 验证窗口 ----------------------
        self.wnd_captcha = QDialog(self)
        self.lbe_captcha_pic = QLabel("图片验证码", self.wnd_captcha)
        self.edt_captcha_answer = QLineEdit(self.wnd_captcha)
        self.btn_captcha_commit = QPushButton("提交", self.wnd_captcha)
        self.path_captcha = "\\".join([lib_.PATH_TEMP, "captcha.bmp"])  # 验证码图片保存路径
        self.captcha_ret = 999  # 验证码图片答案
        self.captcha_btn_text = ""  # 记录弹出验证窗口时点的是哪一个按钮

    def init_wnd(self):
        self.setAttribute(Qt.WA_DeleteOnClose)  # 窗口关闭时删除对象
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框, 但任务栏有图标
        self.start_point = QPoint(0, 0)  # 使窗口支持拖动移动

    def init_status_bar(self):
        self.status_bar.addWidget(self.lbe_1)
        self.status_bar.addWidget(self.lbe_info)

    def show_info(self, text):
        self.sig_info.emit(text)  # 信号槽, 防逆向跟踪
        lib_.log_info(text)

    # 初始化网络验证
    def init_net_auth(self):
        # 检测全局变量是否被修改
        if [lib_.aes_key, lib_.user_account, lib_.pwd_pic, lib_.pwd_zk, lib_.addr_crack] != \
                ["*d#f1Il@34rt7%gh.", "aaa", "1234", "5678", "0x8CFF98"]:
            lib_.client_comment = lib_.user_comment["检测到改数据"]
        # 与服务端连接
        tcp_socket = lib_.connect_server_tcp()
        if not tcp_socket:
            lib_.log_info("服务器繁忙, 请稍后再试")
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

    def init_widgets(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # ------------------ 验证窗口 -----------------
        self.wnd_captcha.setWindowTitle("运算结果")
        self.captcha_vlayout = QVBoxLayout(self.wnd_captcha)
        self.captcha_vlayout.addWidget(self.lbe_captcha_pic)
        self.captcha_vlayout.addWidget(self.edt_captcha_answer)
        self.captcha_vlayout.addWidget(self.btn_captcha_commit)
        self.wnd_captcha.setLayout(self.captcha_vlayout)
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
        self.lbe_pay_key.setText("<a href={}>充值卡号: </a>".format(lib_.url_card))
        # 公告页
        self.lbe_notice.setText("<a href={}>公 告</a>".format(lib_.url_update))
        self.lbe_notice_text.setText(lib_.notice)
        # ------------------ 设置按钮状态 -----------------
        self.btn_login.setEnabled(lib_.allow_login)
        self.btn_reg.setEnabled(lib_.allow_reg)
        self.btn_unbind.setEnabled(lib_.allow_unbind)

    def init_custom_sig_slot(self):
        self.sig_accept.connect(self.accept)
        self.sig_reject.connect(self.reject)
        self.sig_info.connect(lambda text: self.lbe_info.setText(text))
        self.sig_pass.connect(self.on_sig_pass)
        self.sig_close.connect(self.close)

    def init_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_login.clicked.connect(self.on_btn_login_clicked)
        self.btn_reg.clicked.connect(self.on_btn_reg_clicked)
        self.btn_exit.clicked.connect(lambda : self.sig_close.emit())
        self.btn_pay.clicked.connect(self.on_btn_pay_clicked)
        self.btn_unbind.clicked.connect(self.on_btn_unbind_clicked)
        self.btn_modify.clicked.connect(self.on_btn_modify_clicked)
        self.btn_captcha_commit.clicked.connect(self.on_btn_captcha_commit_clicked)

    def popup_captcha_wnd(self):
        # 显示验证窗口
        self.wnd_captcha.show()
        # 刷新验证码
        tr = lib_.create_com_obj(lib_.COM_NAME_TR)
        self.captcha_ret = tr.Draw_CAPTCHA()
        tr.SaveImageData(self.path_captcha)
        self.lbe_captcha_pic.setPixmap(QPixmap(self.path_captcha))

    def popup_update_msg(self):
        if not lib_.cfg_login["提示更新版本"]:
            return
        # 弹出更新网址
        if lib_.client_ver != lib_.latest_ver:
            ret = QMessageBox.information(self, "提示", "发现新版本, 是否前往下载?", QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.Yes)
            if ret == QMessageBox.Yes:
                webbrowser.open(lib_.url_update)

    # 发送接收初始消息
    def send_recv_init(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "初始",
                            "内容": {"备注": lib_.client_comment, "机器码": lib_.machine_code}}
        lib_.send_to_server(tcp_socket, client_info_dict)
        # 等待服务端响应初始消息
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 1")
            return False
        if msg_type == "初始":
            if server_content_dict["结果"]:
                enc_aes_key = server_content_dict["详情"]
                # 重新构造新的aes密钥
                lib_.aes_key = crypto_.decrypt_rsa(crypto_.private_key_client, enc_aes_key)
                lib_.aes = crypto_.AesEncryption(lib_.aes_key)
                return True
            else:
                detail = server_content_dict["详情"]
                QMessageBox.information(self, "错误", detail)
        return False

    # 发送接收项目消息
    def send_recv_proj(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "锟斤拷",
                            "内容": {"版本号": lib_.client_ver}}
        lib_.send_to_server(tcp_socket, client_info_dict)
        # 等待服务端响应项目消息
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 2")
            return False
        if msg_type == "锟斤拷":
            if server_content_dict["结果"]:
                detail_dict = server_content_dict["详情"]
                lib_.notice = detail_dict["客户端公告"]
                lib_.url_update = detail_dict["更新网址"]
                lib_.url_card = detail_dict["发卡网址"]
                lib_.allow_login = detail_dict["允许登录"]
                lib_.allow_reg = detail_dict["允许注册"]
                lib_.allow_unbind = detail_dict["允许解绑"]
                lib_.latest_ver = detail_dict["最新版本"]
                return True
            else:
                detail = server_content_dict["详情"]
                ret = QMessageBox.information(self, "错误", detail, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if ret == QMessageBox.Yes:
                    webbrowser.open(lib_.url_update)
        return False

    def send_recv_custom1(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "烫烫烫",
                            "内容": {"烫烫烫": "烫烫烫"}}
        lib_.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 3")
            return False
        if msg_type == "烫烫烫":
            detail_dict = server_content_dict["详情"]
            lib_.pwd_pic = lib_.aes.decrypt(detail_dict["pic"])
            lib_.pwd_zk = lib_.aes.decrypt(detail_dict["zk"])
            return True
        return False

    def send_recv_custom2(self, tcp_socket: socket.socket):
        client_info_dict = {"消息类型": "屯屯屯",
                            "内容": {"屯屯屯": "屯屯屯"}}
        lib_.send_to_server(tcp_socket, client_info_dict)
        # 处理服务端响应消息
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if not msg_type:
            self.show_info("服务器繁忙, 请稍后再试, 错误码: 4")
            return False
        if msg_type == "屯屯屯":
            detail_dict = server_content_dict["详情"]
            lib_.addr_crack = lib_.aes.decrypt(detail_dict["crk"])
            return True
        return False

    def send_recv_login(self):
        # ----------------- 发送数据给服务器 -----------------
        login_account = lib_.cfg_login["账号"]
        login_pwd = lib_.cfg_login["密码"]
        login_pwd = crypto_.get_encrypted_str(login_pwd.encode())
        login_system = lib_.get_operation_system()
        # 把客户端信息整理成字典
        client_info_dict = {
            "消息类型": "登录",
            "内容": {
                "账号": login_account,
                "密码": login_pwd,
                "机器码": lib_.machine_code,
                "操作系统": login_system,
                "备注": lib_.client_comment,
            }
        }
        # 发送客户端消息
        tcp_socket = lib_.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        lib_.send_to_server(tcp_socket, client_info_dict)
        # ----------------- 接收并处理服务端响应消息 ------------
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if msg_type == "登录":
            self.show_info(server_content_dict["详情"])
            if server_content_dict["结果"]:
                lib_.user_account = server_content_dict["账号"]
                if self.send_recv_custom1(tcp_socket) and self.send_recv_custom2(tcp_socket):
                    self.sig_accept.emit()  # 登录界面接受
                else:
                    self.sig_reject.emit()  # 登录界面拒绝

    def send_recv_reg(self):
        # ----------------- 发送数据给服务器 -----------------
        reg_account = self.edt_reg_account.text()
        reg_pwd = self.edt_reg_pwd.text()
        reg_qq = self.edt_reg_qq.text()
        # 把客户端信息整理成字典
        reg_pwd = crypto_.get_encrypted_str(reg_pwd.encode())
        client_info_dict = {
            "消息类型": "注册",
            "内容": {
                "账号": reg_account,
                "密码": reg_pwd,
                "QQ": reg_qq,
                "机器码": lib_.machine_code,
            }
        }
        # 发送客户端消息
        tcp_socket = lib_.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        lib_.send_to_server(tcp_socket, client_info_dict)
        # ----------------- 接收并处理服务端响应消息 ------------
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if msg_type == "注册":
            self.show_info(server_content_dict["详情"])

    def send_recv_pay(self):
        # ----------------- 发送数据给服务器 -----------------
        account = self.edt_pay_account.text()
        card_key = self.edt_pay_key.text()
        # 把客户端信息整理成字典
        client_info_dict = {
            "消息类型": "充值",
            "内容": {"账号": account, "卡号": card_key},
        }
        # 连接服务端
        tcp_socket = lib_.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        # 发送客户端消息
        lib_.send_to_server(tcp_socket, client_info_dict)
        # ----------------- 接收并处理服务端响应消息 ------------
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if msg_type == "充值":
            self.show_info(server_content_dict["详情"])

    def send_recv_unbind(self):
        # ----------------- 发送数据给服务器 -----------------
        account = self.edt_login_account.text()
        pwd = self.edt_login_pwd.text()
        pwd = crypto_.get_encrypted_str(pwd.encode())
        # 允许异地解绑. 不用发机器码
        client_info_dict = {
            "消息类型": "解绑",
            "内容": {"账号": account, "密码": pwd},
        }
        # 连接服务端
        tcp_socket = lib_.connect_server_tcp()
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        # 发送客户端消息
        lib_.send_to_server(tcp_socket, client_info_dict)
        # ----------------- 接收并处理服务端响应消息 ------------
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if msg_type == "解绑":
            self.show_info(server_content_dict["详情"])

    def send_recv_modify(self):
        # ----------------- 发送数据给服务器 -----------------
        account = self.edt_modify_account.text()
        qq = self.edt_modify_qq.text()
        new_pwd = self.edt_modify_new_pwd.text()
        new_pwd = crypto_.get_encrypted_str(new_pwd.encode())
        client_info_dict = {
            "消息类型": "改密",
            "内容": {
                "账号": account,
                "QQ": qq,
                "密码": new_pwd,
            }
        }
        tcp_socket = lib_.connect_server_tcp()  # 连接服务端
        if not tcp_socket:
            self.show_info("服务器繁忙, 请稍后再试")
            return
        # 发送客户端消息
        lib_.send_to_server(tcp_socket, client_info_dict)
        # ----------------- 接收并处理服务端响应消息 ------------
        msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
        if msg_type == "改密":
            self.show_info(server_content_dict["详情"])

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
        self.captcha_btn_text = "登录"
        # 把控件信息保存到配置文件
        self.cfg_write()
        # 读取登录账号密码, 判断是否符合要求
        login_account = lib_.cfg_login["账号"]
        login_pwd = lib_.cfg_login["密码"]
        bool_list = [
            len(login_account) in range(6, 13),
            len(login_pwd) in range(6, 13),
        ]
        if False in bool_list:
            self.show_info("登录失败, 账号密码长度不符合要求")
            return
        # 弹出验证窗口, 输对验证码才发送给服务端
        self.popup_captcha_wnd()

    def on_btn_reg_clicked(self):
        self.captcha_btn_text = "注册"
        # 判断注册信息是否符合要求
        reg_account = self.edt_reg_account.text()
        reg_pwd = self.edt_reg_pwd.text()
        reg_qq = self.edt_reg_qq.text()
        bool_list = [
            len(reg_account) in range(6, 13),
            len(reg_pwd) in range(6, 13),
            len(reg_qq) in range(5, 11)
        ]
        if False in bool_list:
            self.show_info("注册失败, 账号密码6-12位, QQ号5-10位")
            return
        self.popup_captcha_wnd()

    def on_btn_pay_clicked(self):
        self.captcha_btn_text = "充值"
        account = self.edt_pay_account.text()
        card_key = self.edt_pay_key.text()
        if len(card_key) != 30 or len(account) not in range(6, 13):
            self.show_info("账号或卡密错误, 请检查无误后再试")
            return
        self.popup_captcha_wnd()


    def on_btn_unbind_clicked(self):
        self.captcha_btn_text = "解绑"
        account = self.edt_login_account.text()
        pwd = self.edt_login_pwd.text()
        bool_list = [
            len(account) in range(6, 13),
            len(pwd) in range(6, 13),
        ]
        if False in bool_list:
            self.show_info("解绑失败, 请先确保账号密码输入正确")
            return
        self.popup_captcha_wnd()

    def on_btn_modify_clicked(self):
        self.captcha_btn_text = "改密"
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
        self.popup_captcha_wnd()

    def on_btn_captcha_commit_clicked(self):
        if self.edt_captcha_answer.text() == str(self.captcha_ret):
            self.sig_pass.emit(True)
        else:
            self.sig_pass.emit(False)
        self.edt_captcha_answer.setText("")
        self.wnd_captcha.close()

    def on_sig_pass(self, is_pass: bool):
        if is_pass:
            if self.captcha_btn_text == "登录":
                self.send_recv_login()
            elif self.captcha_btn_text == "注册":
                self.send_recv_reg()
            elif self.captcha_btn_text == "充值":
                self.send_recv_pay()
            elif self.captcha_btn_text == "解绑":
                self.send_recv_unbind()
            elif self.captcha_btn_text == "改密":
                self.send_recv_modify()
        else:
            self.show_info("验证码输入错误")

    # 初始化成功后的操作
    def on_init_success(self):
        # 初始化json文件
        if not os.path.exists(lib_.PATH_JSON_LOGIN):
            lib_.log_info("自动创建登录界面配置文件")
            lib_.dict_to_json_file(lib_.cfg_login, lib_.PATH_JSON_LOGIN)
        lib_.log_info("初始化配置文件完成")

        # 注册组件到系统
        ret = lib_.reg_com_to_system(lib_.COM_NAME_TR)
        print("注册组件到系统:", ret)


if __name__ == '__main__':
    # 初始化日志模块
    lib_.init_logging()
    lib_.log_info("初始化日志模块成功")

    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    lib_.log_info("初始化界面样式完成")

    # 初始化登录窗口
    lib_.wnd_login = WndLogin()
    if lib_.wnd_login.exec_() == QDialog.Accepted:
        lib_.wnd_main = WndMain()
        lib_.wnd_main.show()
        lib_.wnd_main.start_heart_beat()
        sys.exit(app.exec_())
    sys.exit(0)
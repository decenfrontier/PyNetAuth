import sys
import socket
from threading import Thread, Lock
import json
import time

from PySide2.QtGui import QIcon, QCloseEvent, QRegExpValidator, QPixmap, \
    QMouseEvent, QPaintEvent, QPainter, QBitmap
from PySide2.QtWidgets import QDialog, QLabel, QMessageBox, QToolBar, QVBoxLayout, \
    QStatusBar, QApplication, QStyleFactory
from PySide2.QtCore import Qt, QRegExp, QSize, QPoint, Signal

from client.res import qres
from client.ui.wnd_client_login import Ui_WndClientLogin
from wnd_client_main_code import WndClientMain
from client import mf

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
machine_code = ""
login_ip = ""
lock = Lock()

# 线程_获取全局变量
def thd_get_global_var():
    global login_ip, machine_code
    machine_code = mf.get_machine_code()
    login_ip = mf.get_outer_ip()
    print("线程_获取全局变量 执行完成")

class WndClientLogin(QDialog, Ui_WndClientLogin):
    login = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        thd1 = Thread(target=thd_get_global_var, daemon=True)
        thd1.start()
        self.init_wnd()
        self.init_status_bar()
        self.init_net_auth()
        self.init_all_controls()
        self.init_all_sig_slot()
        Thread(target=self.thd_close_login, daemon=True).start()
        thd1.join(1)
        self.show_info("窗口初始化成功")

    def closeEvent(self, event: QCloseEvent):
        tcp_socket.close()

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        mf.log_info(text)

    # 初始化网络验证
    def init_net_auth(self):
        self.show_info("正在连接服务器...")
        err_no = tcp_socket.connect_ex((mf.server_ip, mf.server_port))
        if err_no != 0:
            QMessageBox.critical(self, "错误", f"连接服务器失败, 错误码: {err_no}")
            self.close()
        self.show_info(f"连接服务器成功, 开始接收数据...")
        Thread(target=self.thd_recv_server, daemon=True).start()

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
        with lock:
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
        # 充值页
        self.lbe_pay_key.setText("""<a href="https://www.baidu.com">充值卡号: </a>""")
        self.lbe_pay_key.setOpenExternalLinks(True)
        self.lbe_pay_key.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

    def init_all_sig_slot(self):
        self.login.connect(self.accept)
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_login.clicked.connect(self.on_btn_login_clicked)
        self.btn_reg.clicked.connect(self.on_btn_reg_clicked)
        self.btn_exit.clicked.connect(self.on_btn_exit_clicked)
        self.btn_pay.clicked.connect(self.on_btn_pay_clicked)
        self.btn_unbind.clicked.connect(self.on_btn_unbind_clicked)
        self.btn_modify.clicked.connect(self.on_btn_modify_clicked)

    def thd_close_login(self):
        time.sleep(60*3)  # 3分钟
        self.show_info("长时间未操作, 已自动关闭")
        self.close()

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
        login_pwd = mf.get_encrypted_str(login_pwd.encode())
        login_time = mf.cur_time_format
        login_system = mf.get_operation_system()
        # 把客户端信息整理成字典, 发送给服务器
        client_info_dict = {
            "消息类型": "登录",
            "账号": login_account,
            "密码": login_pwd,
            "机器码": machine_code,
            "上次登录时间": login_time,
            "上次登录IP": login_ip,
            "操作系统": login_system,
        }
        self.send_to_server(tcp_socket, client_info_dict)

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
        client_info_dict = {
            "消息类型": "注册",
            "账号": reg_account,
            "密码": reg_pwd,
            "QQ": reg_qq,
        }
        self.send_to_server(tcp_socket, client_info_dict)

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
            "账号": account,
            "卡号": card_key,
        }
        ret = QMessageBox.information(self, "提示", f"是否确定充值到以下账号: \n{account}",
                                      QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            self.send_to_server(tcp_socket, client_info_dict)

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
        pwd = mf.get_encrypted_str(pwd.encode())
        # 允许异地解绑. 不用发机器码
        client_info_dict = {
            "消息类型": "解绑",
            "账号": account,
            "密码": pwd,
        }
        self.send_to_server(tcp_socket, client_info_dict)

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
        new_pwd = mf.get_encrypted_str(new_pwd.encode())
        client_info_dict = {
            "消息类型": "改密",
            "账号": account,
            "QQ": qq,
            "密码": new_pwd,
        }
        self.send_to_server(tcp_socket, client_info_dict)

    # 发送数据给服务端
    def send_to_server(self, tcp_socket: socket.socket, client_info_dict: dict):
        # py字典 转 json字符串
        json_str = json.dumps(client_info_dict, ensure_ascii=False)
        # 发送客户端注册信息到服务器
        try:
            tcp_socket.send(json_str.encode())
            mf.log_info(f"客户端数据, 发送成功: {json_str}")
        except Exception as e:
            mf.log_info(f"客户端数据, 发送失败: {e}")

    # 线程_接收服务端消息
    def thd_recv_server(self):
        while True:
            mf.log_info("等待服务端发出消息中...")
            try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
                recv_bytes = tcp_socket.recv(1024)
            except:
                recv_bytes = ""
            if not recv_bytes:  # 若客户端退出,会收到一个空str
                break
            # json字符串 转 py字典
            json_str = recv_bytes.decode()
            server_info_dict = json.loads(json_str)
            mf.log_info(f"收到服务端的消息: {json_str}")
            # 客户端消息处理
            msg_type = server_info_dict["消息类型"]
            if msg_type in ("注册", "充值", "解绑", "改密"):
                self.show_info(server_info_dict["详情"])
            elif msg_type == "登录":
                self.show_info(server_info_dict["详情"])
                if server_info_dict["结果"]:
                    mf.client_account = server_info_dict["账号"]
                    print(mf.client_account)
                    tcp_socket.close()  # 先关闭套接字
                    with lock:
                        self.login.emit()
                        return
        self.show_info("与服务器断开连接...")


if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    mf.init_logging()
    wnd_client_login = WndClientLogin()
    wnd_client_login.show()

    if wnd_client_login.exec_() == QDialog.Accepted:
        wnd_client_main = WndClientMain()
        wnd_client_main.show()
        wnd_client_main.start_heart_beat()
        sys.exit(app.exec_())
    sys.exit(0)
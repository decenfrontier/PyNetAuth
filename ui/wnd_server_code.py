from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtCore import QTimer
import pymysql
import socket
from threading import Thread
import time

from ui.wnd_server import Ui_WndServer
from res import qres
import mf

class WndServer(QMainWindow, Ui_WndServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_status_bar()
        self.init_timer()
        self.init_all_controls()
        self.init_all_sig_slot()
        self.init_mysql()
        self.init_tcp_server()
        self.show_info("窗口初始化完成")

    def closeEvent(self, event: QCloseEvent):
        self.tcp_socket.close()
        self.crsr.close()
        self.conn.close()

    def init_status_bar(self):
        self.lbe_info = QLabel()
        self.status_bar.addWidget(self.lbe_info)

    def init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)
        ...

    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/users.png"), "全部用户")
        self.tool_bar.addAction(QIcon(":/user.png"), "在线用户")
        self.tool_bar.addAction(QIcon(":/card.png"), "卡密管理")
        self.tool_bar.addAction(QIcon(":/log.png"), "执行日志")
        # 所有表头可视化
        self.tbe_all_user.horizontalHeader().setVisible(True)
        self.tbe_online_user.horizontalHeader().setVisible(True)
        self.tbe_card_manage.horizontalHeader().setVisible(True)
        # 全部用户表
        account, pwd, email, machine_code, reg_ip, reg_time, due_time, is_forbid = [i for i in range(8)]
        self.tbe_all_user.setColumnWidth(account, 100)
        self.tbe_all_user.setColumnWidth(pwd, 100)
        self.tbe_all_user.setColumnWidth(email, 100)
        self.tbe_all_user.setColumnWidth(machine_code, 90)
        self.tbe_all_user.setColumnWidth(reg_ip, 100)
        self.tbe_all_user.setColumnWidth(reg_time, 120)
        self.tbe_all_user.setColumnWidth(due_time, 120)
        self.tbe_all_user.setColumnWidth(is_forbid, 70)
        # 卡密管理表
        card_key, state, type, gen_time, use_time = [i for i in range(5)]
        self.tbe_card_manage.setColumnWidth(card_key, 340)
        self.tbe_card_manage.setColumnWidth(state, 80)
        self.tbe_card_manage.setColumnWidth(type, 80)
        self.tbe_card_manage.setColumnWidth(gen_time, 150)
        self.tbe_card_manage.setColumnWidth(use_time, 150)

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)



    def init_mysql(self):
        # 创建连接对象
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="mysql",
            database="network_auth"
        )
        # 创建游标对象
        self.crsr = self.conn.cursor()

    def init_tcp_server(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.bind(("", 47123))  # 主机号+端口号
        self.tcp_socket.listen(128)  # 允许同时有XX个客户端连接此服务器, 排队等待被服务
        # Thread(target=self.thd_receive_client).start()

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        self.tbr_log.append(f"{mf.cur_time_format}  {text}")

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        self.show_info(f"切换到 {action_name} 页")
        if action_name == "全部用户":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "在线用户":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "卡密管理":
            self.stack_widget.setCurrentIndex(2)
        elif action_name == "执行日志":
            self.stack_widget.setCurrentIndex(3)

    def on_timer_timeout(self):
        mf.cur_time_stamp += 1
        mf.cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")

    def thd_receive_client(self):
        print("服务器开始接受客户请求...")
        while True:
            print("接受客户端请求,分配一个客服套接字...")
            client_socket, client_addr = self.tcp_socket.accept()

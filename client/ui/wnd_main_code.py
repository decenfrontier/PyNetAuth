import time
import socket
import json
import base64

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtCore import QTimer
from threading import Thread

from client.ui.wnd_main import Ui_WndMain
from client import mf

class WndMain(QMainWindow, Ui_WndMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_instance_field()
        self.init_status_bar()

    def closeEvent(self, event: QCloseEvent):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        err_no = tcp_socket.connect_ex((mf.server_ip, mf.server_port))
        if err_no == 0:
            client_info_dict = {
                "消息类型": "离线",
                "内容": {
                    "账号": mf.user_account,
                    "备注": mf.client_comment,
                }
            }
            mf.send_to_server(tcp_socket, client_info_dict)

    # 初始化实例属性
    def init_instance_field(self):
        self.error_count = 0  # 网络通信失败次数
        self.last_heart_stamp = mf.cur_time_stamp  # 上次心跳时间点
        self.lbe_info = QLabel(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

    def init_status_bar(self):
        self.status_bar.addWidget(self.lbe_info)

    def show_info(self, info):
        self.lbe_info.setText(f"<提示> : {info}")
        mf.log_info(info)

    def start_heart_beat(self):
        self.error_count = 0
        Thread(target=self.thd_heart_beat, daemon=True).start()

    def thd_heart_beat(self):
        while True:
            # 每一轮循环错误次数+1, 初始化等待时间
            self.error_count += 1
            sleep_time = 10  # todo

            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            err_no = tcp_socket.connect_ex((mf.server_ip, mf.server_port))
            if err_no == 0:
                client_info_dict = {
                    "消息类型": "心跳",
                    "内容": {
                        "账号": mf.user_account,
                        "机器码": mf.machine_code,
                        "备注": mf.client_comment,
                    }
                }
                mf.send_to_server(tcp_socket, client_info_dict)
                msg_type, server_content_dict = mf.recv_from_server(tcp_socket)
                if msg_type == "心跳":
                    heart_ret = server_content_dict["结果"]
                    if heart_ret == "正常":
                        self.error_count = 0
                        self.last_heart_stamp = mf.cur_time_stamp
                        sleep_time = 12  # 60*10, todo
                    elif heart_ret == "下线":
                        self.error_count = 10
                        self.show_info(server_content_dict["详情"])
            tcp_socket.close()  # 发送接收完立刻断开
            if self.error_count >= 5:
                break
            print("等待时间:", sleep_time)
            time.sleep(sleep_time)
        self.show_info("与服务器断开连接...")
        self.close()

    def on_timer_timeout(self):
        mf.cur_time_str = time.strftime("%H:%M:%S")
        mf.cur_time_stamp += 1
        if mf.time_diff(self.last_heart_stamp, mf.cur_time_stamp) >= 15:
            self.show_info("与服务器断开连接...")
            self.close()


from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt
import sys

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    wnd_client_main = WndMain()
    wnd_client_main.show()

    sys.exit(app.exec_())

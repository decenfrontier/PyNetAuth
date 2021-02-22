import time
import socket
import json
import base64

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtCore import QTimer, Signal
from threading import Thread

from ui.wnd_main import Ui_WndMain
import lib_

class WndMain(QMainWindow, Ui_WndMain):
    sig_info = Signal(str)
    sig_close = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_instance_field()
        self.init_status_bar()
        self.init_custom_sig_slot()

    def closeEvent(self, event: QCloseEvent):
        tcp_socket = lib_.connect_server_tcp()
        if not tcp_socket:
            lib_.log_info("服务器繁忙, 请稍后再试")
            return
        client_info_dict = {"消息类型": "离线",
            "内容": {"账号": lib_.user_account, "备注": lib_.client_comment}}
        lib_.send_to_server(tcp_socket, client_info_dict)

    # 初始化实例属性
    def init_instance_field(self):
        self.lbe_1 = QLabel("<提示> : ")
        self.lbe_info = QLabel("窗口初始化成功")

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

        self.error_count = 0  # 网络通信失败次数
        self.last_heart_stamp = lib_.cur_time_stamp  # 上次心跳时间点

    def init_status_bar(self):
        self.status_bar.addWidget(self.lbe_1)
        self.status_bar.addWidget(self.lbe_info)

    def init_custom_sig_slot(self):
        self.sig_info.connect(lambda text: self.lbe_info.setText(text))
        self.sig_close.connect(self.close)

    def show_info(self, text):
        self.sig_info.emit(text)  # 信号槽, 防逆向跟踪
        lib_.log_info(text)

    def start_heart_beat(self):
        self.error_count = 0
        Thread(target=self.thd_heart_beat, daemon=True).start()

    def thd_heart_beat(self):
        while True:
            tcp_socket = lib_.connect_server_tcp()
            if not tcp_socket:
                lib_.log_info("与服务器连接异常...")
            else:
                client_info_dict = {"消息类型": "心跳",
                    "内容": {"账号": lib_.user_account, "机器码": lib_.machine_code, "备注": lib_.client_comment}}
                lib_.send_to_server(tcp_socket, client_info_dict)
                msg_type, server_content_dict = lib_.recv_from_server(tcp_socket)
                if msg_type == "心跳":
                    heart_ret = server_content_dict["结果"]
                    if heart_ret == "正常":
                        self.error_count = 0
                        self.last_heart_stamp = lib_.cur_time_stamp
                        sleep_time = 12  # 60*10, todo
                    elif heart_ret == "下线":
                        self.error_count = 10
                        self.show_info(server_content_dict["详情"])
                tcp_socket.close()  # 发送接收完立刻断开
            # 每一轮循环错误次数+1, 失败则每隔20秒连接一次
            self.error_count += 1
            sleep_time = 20
            # 超过5次没连上, 跳出心跳循环, 关闭窗口
            if self.error_count > 5:
                break
            print("等待时间:", sleep_time)
            time.sleep(sleep_time)
        self.show_info("与服务器断开连接1...")
        self.sig_close.emit()

    def on_timer_timeout(self):
        lib_.cur_time_str = time.strftime("%H:%M:%S")
        lib_.cur_time_stamp += 1
        if lib_.time_diff(self.last_heart_stamp, lib_.cur_time_stamp) >= 15:  # 防止心跳线程被干掉
            self.show_info("与服务器断开连接2...")
            self.sig_close.emit()


from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt
import sys

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))

    wnd_client_main = WndMain()
    wnd_client_main.show()

    sys.exit(app.exec_())

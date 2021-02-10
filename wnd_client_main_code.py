import time
import socket
import json

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtCore import QTimer
from threading import Thread

from ui.wnd_client_main import Ui_WndClientMain
import mf

class WndClientMain(QMainWindow, Ui_WndClientMain):
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
                "账号": mf.client_account,
                "备注": mf.client_comment,
            }
            self.send_to_server(tcp_socket, client_info_dict)

    # 初始化实例属性
    def init_instance_field(self):
        self.error_count = 0  # 网络通信失败次数
        self.last_heart_time = mf.cur_time_stamp  # 上次心跳时间点
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
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            err_no = tcp_socket.connect_ex((mf.server_ip, mf.server_port))
            if err_no == 0:
                client_info_dict = {
                    "消息类型": "心跳",
                    "账号": mf.client_account,
                    "备注": mf.client_comment,
                }
                self.send_to_server(tcp_socket, client_info_dict)
                self.recv_from_server(tcp_socket)
                sleep_time = 12 # 60*10, todo
            else:
                self.error_count += 1
                sleep_time = 10
            tcp_socket.close()  # 发送接收完立刻断开
            if self.error_count >= 5:
                break
            print("等待时间:", sleep_time)
            time.sleep(sleep_time)
        self.show_info("与服务器断开连接...")
        self.close()

    # 线程_获取服务端自定义数据(防山寨)
    def thd_get_server_custom_data(self):
        # RSA获取 通信密钥,
        #
        # 对称加密算法获取 字库密码, 图片密码, 大漠破解地址, 标志位基址

        ...

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

    # 接收来自服务端的数据
    def recv_from_server(self, tcp_socket: socket.socket):
        tcp_socket.settimeout(5)  # 设置为非阻塞接收, 只等5秒
        try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
            recv_bytes = tcp_socket.recv(1024)
        except:
            recv_bytes = ""
        tcp_socket.settimeout(None)  # 重新设置为阻塞模式
        if not recv_bytes:  # 若客户端退出,会收到一个空str
            return
        json_str = recv_bytes.decode()
        # json字符串 转 py字典
        json_str = recv_bytes.decode()
        server_info_dict = json.loads(json_str)
        mf.log_info(f"收到服务端的消息: {json_str}")
        msg_type = server_info_dict.get("消息类型")
        if msg_type != "心跳":
            return
        heart_ret = server_info_dict["结果"]
        if heart_ret == "正常":
            self.error_count = 0
            self.last_heart_time = mf.cur_time_stamp
        elif heart_ret == "下线":
            self.error_count = 10
            self.show_info(server_info_dict["详情"])
        else:
            self.error_count += 1

    def on_timer_timeout(self):
        mf.cur_time_str = time.strftime("%H:%M:%S")
        mf.cur_time_stamp += 1
        if mf.time_diff(self.last_heart_time, mf.cur_time_stamp) >= 15:
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

    wnd_client_main = WndClientMain()
    wnd_client_main.show()

    sys.exit(app.exec_())

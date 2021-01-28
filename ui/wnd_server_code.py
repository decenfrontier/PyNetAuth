from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtWidgets import QMainWindow, QLabel, QMessageBox
from PySide2.QtCore import QTimer
import pymysql
import socket
from threading import Thread
import time
import json

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
        self.move(0, 160)
        self.show_info("窗口初始化成功")

    def closeEvent(self, event: QCloseEvent):
        tcp_socket.close()
        cursor.close()
        db.close()

    def init_status_bar(self):
        self.lbe_info = QLabel()
        self.status_bar.addWidget(self.lbe_info)

    def init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

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

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        self.tbr_log.append(f"{mf.cur_time_format}  {text}")
        print(text)

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        self.show_info(f"切换到 {action_name}")
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


def thd_accept_client():
    wnd_server.show_info("服务器已开启, 准备接受客户请求...")
    while True:
        wnd_server.show_info("正在等待客户端发出连接请求...")
        try:
            client_socket, client_addr = tcp_socket.accept()
        except:
            break
        wnd_server.show_info(f"客户端IP地址及端口: {client_addr}, 已分配客服套接字")
        Thread(target=thd_serve_client, args=(client_socket, client_addr), daemon=True).start()
    wnd_server.show_info("服务端已关闭, 停止接受客户端请求...")


def thd_serve_client(client_socket: socket.socket, client_addr: tuple):
    while True:
        wnd_server.show_info("等待客户端发出消息中...")
        try:  # 若任务消息都没收到, 客户端直接退出, 会抛出异常
            recv_bytes = client_socket.recv(1024)
        except:
            recv_bytes = ""
        if not recv_bytes:  # 若客户端退出,会收到一个空str
            break
        recv_str = recv_bytes.decode()
        wnd_server.show_info(f"收到客户端的消息: {recv_str}")
        # json字符串 转 py字典
        client_info_dict = json.loads(recv_str)
        msg_type = client_info_dict["msg_type"]
        client_info_dict.pop("msg_type")
        if msg_type == "reg":
            deal_reg(client_info_dict)

    wnd_server.show_info(f"客户端{client_addr}, 已退出, 服务结束")
    client_socket.close()


# 处理-注册
def deal_reg(client_info_dict: dict):
    client_info_dict["reg_time"] = mf.cur_time_format
    account = client_info_dict["account"]

    if table_query("all_user", "account", account):  # 查询账号是否存在
        reg_ret = False
        wnd_server.show_info(f"错误, 账号{account}已被注册!")
    else:  # 插入表
        reg_ret = table_insert("all_user", client_info_dict)
        wnd_server.show_info(f"账号{account}注册结果: {reg_ret}")
    # 把注册结果整理成py字典
    server_info_dict = {"msg_type": "reg_ret", "reg_ret": reg_ret}
    # py字典 转 json字符串
    json_str = json.dumps(server_info_dict, ensure_ascii=False)
    # 向客户端回复注册结果
    try:
        tcp_socket.send(json_str.encode())
        self.show_info("注册结果向客户端回复成功")
    except Exception as e:
        self.show_info(f"注册结果向客户端回复失败: {e}")


# 表-插入, 成功返回True, 否则返回False
def table_insert(table_name: str, val_dict: dict):
    # keys = "account, pwd,qq, machine_code, reg_ip"
    keys = ", ".join(val_dict.keys())
    # values = "%s, %s, %s,%s,%s,%s"
    values = ", ".join(["%s"] * len(val_dict))
    # 准备SQL语句
    sql = f"insert {table_name}({keys}) values({values});"
    ret = False
    try:
        # 执行SQL语句
        ret = cursor.execute(sql, tuple(val_dict.values()))
        if ret:
            db.commit()
        else:
            raise Exception("执行SQL语句失败")
    except:
        # 对修改的数据进行撤销
        db.rollback()
    wnd_server.show_info(f"table_insert: {ret}")
    return ret

# 表-查询, 成功返回True, 否则返回False
def table_query(table_name: str, field: str, val: str):
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    sql = f"select * from {table_name} where {field}=%s;"
    try:
        # 执行SQL语句
        cursor.execute(sql, (val,))
        # 获取查询, 没查到返回空元组
        ret = cursor.fetchall()
        # 提交到数据库
        db.commit()
    except:
        # 数据库回滚
        db.rollback()
        ret = ()
    wnd_server.show_info(f"table_query: {ret}")
    ret = True if ret else False
    return ret


import sys
from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 应用程序
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)
    # 窗口
    wnd_server = WndServer()
    wnd_server.show()
    # 初始化mysql
    try:
        # 创建数据库对象
        db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="mysql",
            database="network_auth"
        )
        # 创建游标对象, pymysql.cursors.DictCursor指定 返回的结果类型 为字典  默认是元祖类型
        cursor = db.cursor(pymysql.cursors.DictCursor)
        wnd_server.show_info("连接数据库成功")
    except Exception as e:
        QMessageBox.critical(wnd_server, "错误", f"mysql连接失败: {e}")
        sys.exit(-1)
    # 初始化tcp连接
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((mf.server_ip, mf.server_port))  # 主机号+端口号
        tcp_socket.listen(128)  # 允许同时有XX个客户端连接此服务器, 排队等待被服务
        Thread(target=thd_accept_client, daemon=True).start()
    except Exception as e:
        QMessageBox.critical(wnd_server, "错误", f"tcp连接失败: {e}")
        sys.exit(-1)
    # 消息循环
    sys.exit(app.exec_())

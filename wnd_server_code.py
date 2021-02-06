import sys
import time, datetime
import json
from threading import Thread, Lock
from random import randint

from PySide2.QtGui import QIcon, QCloseEvent, QTextCursor, QCursor, QIntValidator
from PySide2.QtWidgets import QApplication, QStyleFactory, QMainWindow, QLabel, \
    QMessageBox, QTableWidgetItem, QMenu, QAction
from PySide2.QtCore import Qt, QTimer
import pymysql
import socket

from ui.wnd_server import Ui_WndServer
from res import qres

lock = Lock()
cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")
today = cur_time_format[:10]
path_log = f"C:\\net_auth_{today}.log"
server_ip = "127.0.0.1"
server_port = 47123
qss_style = """
    * {
        font-size: 12px;
        font-family: "Microsoft YaHei";
    }
    QTableView {
        selection-color: #000000;
	    selection-background-color: #c4e1d2; 
    }
    QTableView::item:hover	{	
	    background-color: #a1b1c9;		
    }
"""

class WndServer(QMainWindow, Ui_WndServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_status_bar()
        self.init_mysql()
        self.init_net_auth()
        self.init_timer()
        self.init_all_controls()
        self.init_all_menu()
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

    def init_mysql(self):
        try:
            global db, cursor
            # 创建数据库对象
            db = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="mysql",
                database="net_auth"
            )
            # 创建游标对象, 指定返回一个字典列表, 获取的每条数据的类型为字典(默认是元组)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            log_append_content("连接数据库成功")
        except Exception as e:
            log_append_content(f"mysql连接失败: {e}")
            QMessageBox.critical(self, "错误", f"mysql连接失败: {e}")
            self.close()

    def init_net_auth(self):
        # 初始化tcp连接
        try:
            global tcp_socket
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.bind((server_ip, server_port))  # 主机号+端口号
            tcp_socket.listen(128)  # 允许同时有XX个客户端连接此服务器, 排队等待被服务
            Thread(target=self.thd_accept_client, daemon=True).start()
        except Exception as e:
            log_append_content(f"tcp连接失败: {e}")
            QMessageBox.critical(self, "错误", f"tcp连接失败: {e}")
            self.close()

    def init_timer(self):
        self.timer_sec = QTimer()
        self.timer_sec.timeout.connect(self.on_timer_sec_timeout)
        self.timer_sec.start(1000)
        self.timer_min = QTimer()
        self.timer_min.timeout.connect(self.on_timer_min_timeout)
        self.timer_min.start(1000*60*15)


    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/proj.png"), "项目管理")
        self.tool_bar.addAction(QIcon(":/users.png"), "用户管理")
        self.tool_bar.addAction(QIcon(":/card.png"), "卡密管理")
        self.tool_bar.addAction(QIcon(":/log.png"), "执行日志")
        # ------------------ 设置编辑框格式 -----------------
        self.edt_user_gift_day.setValidator(QIntValidator(0, 99))
        # 所有表头可视化
        self.tbe_proj.horizontalHeader().setVisible(True)
        self.tbe_user.horizontalHeader().setVisible(True)
        self.tbe_card.horizontalHeader().setVisible(True)
        # 所有表格设置不可编辑
        # self.tbe_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tbe_online_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tbe_card.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 项目管理表
        id, ver, pub_notice, url_update, url_card = [i for i in range(5)]
        self.tbe_proj.setColumnWidth(id, 40)
        self.tbe_proj.setColumnWidth(ver, 100)
        self.tbe_proj.setColumnWidth(pub_notice, 160)
        self.tbe_proj.setColumnWidth(url_update, 120)
        self.tbe_proj.setColumnWidth(url_card, 120)
        # 用户管理表
        id, account, pwd, qq, state, heart_time, due_time, last_login_time, last_login_ip,\
        last_login_place, today_login_count, today_unbind_count, machine_code, reg_time, \
        opration_system, comment= [i for i in range(16)]
        self.tbe_user.setColumnWidth(id, 40)
        self.tbe_user.setColumnWidth(account, 70)
        self.tbe_user.setColumnWidth(pwd, 40)
        self.tbe_user.setColumnWidth(qq, 70)
        self.tbe_user.setColumnWidth(state, 50)
        self.tbe_user.setColumnWidth(heart_time, 130)
        self.tbe_user.setColumnWidth(due_time, 130)
        self.tbe_user.setColumnWidth(last_login_time, 130)
        self.tbe_user.setColumnWidth(reg_time, 130)
        self.tbe_user.setColumnWidth(opration_system, 130)
        # 卡密管理表
        id, card_key, type, gen_time, sale_time, use_time = [i for i in range(6)]
        self.tbe_card.setColumnWidth(id, 40)
        self.tbe_card.setColumnWidth(card_key, 260)
        self.tbe_card.setColumnWidth(type, 60)
        self.tbe_card.setColumnWidth(gen_time, 145)
        self.tbe_card.setColumnWidth(sale_time, 145)
        # 自定义数据表
        id, key, val, en_val = [i for i in range(4)]
        self.tbe_custom.setColumnWidth(id, 40)
        self.tbe_custom.setColumnWidth(key, 100)
        self.tbe_custom.setColumnWidth(val, 120)
        self.tbe_custom.setColumnWidth(en_val, 200)

    def init_all_menu(self):
        # 项目管理表
        self.tbe_proj.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_proj = QMenu()
        self.action_proj_show_all = QAction("显示全部项目信息")
        self.action_proj_del = QAction("删除此记录")
        self.menu_tbe_proj.addAction(self.action_proj_show_all)
        self.menu_tbe_proj.addAction(self.action_proj_del)
        self.action_proj_del.triggered.connect(self.on_action_proj_del_record_triggered)
        self.action_proj_show_all.triggered.connect(self.show_all_tbe_proj)
        self.tbe_proj.customContextMenuRequested.connect(
            lambda : self.menu_tbe_proj.exec_(QCursor.pos())
        )
        # 用户管理表
        self.tbe_user.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_user = QMenu()
        self.action_user_show_all = QAction("显示全部用户信息")
        self.menu_tbe_user.addAction(self.action_user_show_all)
        self.action_user_show_all.triggered.connect(self.show_all_tbe_user)
        self.tbe_user.customContextMenuRequested.connect(
            lambda : self.menu_tbe_user.exec_(QCursor.pos())
        )
        # 卡密管理表
        self.tbe_card.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_card = QMenu()
        self.action_card_show_all = QAction("显示全部卡密信息")
        self.action_card_show_unuse = QAction("显示未使用卡密")
        self.action_card_show_sale = QAction("显示销售中卡密")
        self.action_card_del_used = QAction("删除已使用卡密")
        self.menu_tbe_card.addAction(self.action_card_show_all)
        self.menu_tbe_card.addAction(self.action_card_show_unuse)
        self.menu_tbe_card.addAction(self.action_card_show_sale)
        self.menu_tbe_card.addAction(self.action_card_del_used)
        self.action_card_show_all.triggered.connect(self.show_all_tbe_card)
        self.action_card_show_unuse.triggered.connect(self.on_action_card_show_unuse_triggered)
        self.action_card_show_sale.triggered.connect(self.on_action_card_show_sale_triggered)
        self.action_card_del_used.triggered.connect(self.on_action_card_del_used_triggered)
        self.tbe_card.customContextMenuRequested.connect(
            lambda : self.menu_tbe_card.exec_(QCursor.pos())
        )

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        # 按钮相关
        self.btn_proj_confirm.clicked.connect(self.on_btn_proj_confirm_clicked)

        self.btn_user_query.clicked.connect(self.on_btn_user_query_clicked)
        self.btn_user_gift_day.clicked.connect(self.on_btn_user_gift_day_clicked)

        self.btn_card_gen.clicked.connect(self.on_btn_card_gen_clicked)

        # 表格相关
        self.tbe_proj.cellClicked.connect(self.on_tbe_proj_cellClicked)


    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        log_append_content(text)

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        if action_name == "项目管理":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "用户管理":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "卡密管理":
            self.stack_widget.setCurrentIndex(2)
        elif action_name == "执行日志":
            self.stack_widget.setCurrentIndex(3)
            self.tbr_log.setText(log_read_content())
            self.tbr_log.moveCursor(QTextCursor.End)

    def on_btn_proj_confirm_clicked(self):
        client_ver = self.edt_proj_client_ver.text()
        reg_gift_day = self.edt_proj_reg_gift_day.text()
        url_card = self.edt_proj_url_card.text()
        url_update = self.edt_proj_url_update.text()
        pub_notice = self.pedt_proj_public_notice.toPlainText()
        val_dict = {
            "客户端版本": client_ver,
            "客户端公告": pub_notice,
            "更新地址": url_update,
            "发卡地址": url_card,
            "注册赠送天数": reg_gift_day,
        }
        if sql_table_query("1项目管理", {"客户端版本": client_ver}):
            sql_table_update("1项目管理", val_dict, {"客户端版本": client_ver})
            self.show_info("已更新项目记录")
        else:
            sql_table_insert("1项目管理", val_dict)
            self.show_info("已插入项目新记录")
        self.show_all_tbe_proj()

    def on_btn_user_query_clicked(self):
        field = self.cmb_user_field.currentText()
        operator = self.cmb_user_operator.currentText()
        value = self.edt_user_value.text()
        condition = f"{field} {operator} {value}"
        query_user_list = sql_table_query_ex("2用户管理", condition)
        if self.refresh_tbe_user(query_user_list):
            self.show_info("用户记录查询成功")
        else:
            self.show_info("用户记录查询失败")

    def on_btn_user_gift_day_clicked(self):
        gift_day = self.edt_user_gift_day.text()
        gift_day = 0 if gift_day == "" else int(gift_day)
        ret = QMessageBox.information(self, "提示", f"所有用户续费{gift_day}天?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        # todo: 已到期的用户不要加时间
        sql_table_update_ex("2用户管理", f"到期时间 = date_add(到期时间, interval {gift_day} day)",
                            "状态 in ('在线', '离线')")

    def on_btn_card_gen_clicked(self):
        gen_time = cur_time_format
        card_type = self.cmb_card_type.currentText()
        card_num = int(self.edt_card_num.text())
        for i in range(card_num):
            card_key = gen_rnd_card_key()
            val_dict = {
                "卡号": card_key,
                "卡类型": card_type,
                "制卡时间": gen_time
            }
            if sql_table_insert("3卡密管理", val_dict):
                self.show_info(f"生成{card_type}{card_key}成功")
            else:
                self.show_info(f"生成{card_type}{card_key}失败")
        self.show_all_tbe_card()

    def on_tbe_proj_cellClicked(self, row: int, col: int):
        client_ver = self.tbe_proj.item(row, 1).text()
        pub_notice = self.tbe_proj.item(row, 2).text()
        url_update = self.tbe_proj.item(row, 3).text()
        url_card = self.tbe_proj.item(row, 4).text()
        reg_gift_day = self.tbe_proj.item(row, 5).text()

        self.edt_proj_client_ver.setText(client_ver)
        self.pedt_proj_public_notice.setPlainText(pub_notice)
        self.edt_proj_url_update.setText(url_update)
        self.edt_proj_url_card.setText(url_card)
        self.edt_proj_reg_gift_day.setText(reg_gift_day)

    def on_action_proj_del_record_triggered(self):
        row = self.tbe_proj.currentRow()  # 若不在行内点, 则默认返回0
        client_ver = self.tbe_proj.item(row, 1).text()
        ret = QMessageBox.information(self, "提示", f"是否确定删除以下客户端版本: \n{client_ver}",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        if sql_table_del("1项目管理", {"客户端版本": client_ver}):
            self.show_info(f"删除项目表记录: {client_ver}成功")
        else:
            self.show_info(f"删除项目表记录: {client_ver}失败")
        self.show_all_tbe_proj()

    def on_action_card_show_unuse_triggered(self):
        query_card_list = sql_table_query_ex("3卡密管理", "使用时间 is null")
        if self.refresh_tbe_card(query_card_list):
            self.show_info("显示未使用卡密成功")
        else:
            self.show_info("显示未使用卡密失败")

    def on_action_card_show_sale_triggered(self):
        query_card_list = sql_table_query_ex("3卡密管理", "销售时间 is not null")
        if self.refresh_tbe_card(query_card_list):
            self.show_info("显示销售中卡密成功")
        else:
            self.show_info("显示销售中卡密失败")

    def on_action_card_del_used_triggered(self):
        ret = QMessageBox.information(self, "提示", "是否确定删除已使用的卡号?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        if sql_table_del_ex("3卡密管理", "使用时间 is not null"):
            self.show_info("删除已使用的卡号成功")
        else:
            self.show_info("删除已使用的卡号失败")
        self.show_all_tbe_card()

    def show_all_tbe_proj(self):
        query_proj_list = sql_table_query("1项目管理")
        if self.refresh_tbe_proj(query_proj_list):
            self.show_info("显示所有项目成功")
        else:
            self.show_info("显示所有项目失败")

    def show_all_tbe_user(self):
        query_user_list = sql_table_query("2用户管理")
        if self.refresh_tbe_user(query_user_list):
            self.show_info("显示所有用户成功")
        else:
            self.show_info("显示所有用户失败")

    def show_all_tbe_card(self):
        query_card_list = sql_table_query("3卡密管理")
        if self.refresh_tbe_card(query_card_list):
            self.show_info("显示所有卡密成功")
        else:
            self.show_info("显示所有卡密失败")

    def refresh_tbe_proj(self, query_proj_list):
        self.tbe_proj.setRowCount(len(query_proj_list))
        for row, query_proj in enumerate(query_proj_list):
            id = QTableWidgetItem(str(query_proj["ID"]))
            client_ver = QTableWidgetItem(query_proj["客户端版本"])
            pub_notice = QTableWidgetItem(query_proj["客户端公告"])
            url_update = QTableWidgetItem(query_proj["更新地址"])
            url_card = QTableWidgetItem(query_proj["发卡地址"])
            reg_gift_day = QTableWidgetItem(str(query_proj["注册赠送天数"]))
            self.tbe_proj.setItem(row, 0, id)
            self.tbe_proj.setItem(row, 1, client_ver)
            self.tbe_proj.setItem(row, 2, pub_notice)
            self.tbe_proj.setItem(row, 3, url_update)
            self.tbe_proj.setItem(row, 4, url_card)
            self.tbe_proj.setItem(row, 5, reg_gift_day)

    def refresh_tbe_user(self, query_user_list):
        if not query_user_list:
            return False
        self.tbe_user.setRowCount(len(query_user_list))
        for row, query_user in enumerate(query_user_list):
            heart_time = "" if query_user["心跳时间"] is None else str(query_user["心跳时间"])
            due_time = "" if query_user["到期时间"] is None else str(query_user["到期时间"])
            last_login_time = "" if query_user["上次登录时间"] is None else str(query_user["上次登录时间"])
            reg_time = "" if query_user["注册时间"] is None else str(query_user["注册时间"])
            id = QTableWidgetItem(str(query_user["ID"]))
            account = QTableWidgetItem(query_user["账号"])
            pwd = QTableWidgetItem("***")
            qq = QTableWidgetItem(query_user["QQ"])
            state = QTableWidgetItem(query_user["状态"])
            heart_time = QTableWidgetItem(heart_time)
            due_time = QTableWidgetItem(due_time)
            last_login_time = QTableWidgetItem(last_login_time)
            last_login_ip = QTableWidgetItem(query_user["上次登录IP"])
            last_login_place = QTableWidgetItem(query_user["上次登录地"])
            today_login_count = QTableWidgetItem(query_user["今日登录次数"])
            today_unbind_count = QTableWidgetItem(query_user["今日解绑次数"])
            machine_code = QTableWidgetItem(query_user["机器码"])
            reg_time = QTableWidgetItem(reg_time)
            opration_system = QTableWidgetItem(query_user["操作系统"])
            comment = QTableWidgetItem(query_user["备注"])
            self.tbe_user.setItem(row, 0, id)
            self.tbe_user.setItem(row, 1, account)
            self.tbe_user.setItem(row, 2, pwd)
            self.tbe_user.setItem(row, 3, qq)
            self.tbe_user.setItem(row, 4, state)
            self.tbe_user.setItem(row, 5, heart_time)
            self.tbe_user.setItem(row, 6, due_time)
            self.tbe_user.setItem(row, 7, last_login_time)
            self.tbe_user.setItem(row, 8, last_login_ip)
            self.tbe_user.setItem(row, 9, last_login_place)
            self.tbe_user.setItem(row, 10, today_login_count)
            self.tbe_user.setItem(row, 11, today_unbind_count)
            self.tbe_user.setItem(row, 12, machine_code)
            self.tbe_user.setItem(row, 13, reg_time)
            self.tbe_user.setItem(row, 14, opration_system)
            self.tbe_user.setItem(row, 15, comment)
        return True

    def refresh_tbe_card(self, query_card_list):
        if not query_card_list:
            return False
        self.tbe_card.setRowCount(len(query_card_list))
        for row, query_card in enumerate(query_card_list):
            query_card["制卡时间"] = "" if query_card["制卡时间"] is None else str(query_card["制卡时间"])
            query_card["销售时间"] = "" if query_card["销售时间"] is None else str(query_card["销售时间"])
            query_card["使用时间"] = "" if query_card["使用时间"] is None else str(query_card["使用时间"])
            id = QTableWidgetItem(str(query_card["ID"]))
            card_key = QTableWidgetItem(query_card["卡号"])
            card_type = QTableWidgetItem(query_card["卡类型"])
            gen_time = QTableWidgetItem(query_card["制卡时间"])
            sale_time = QTableWidgetItem(query_card["销售时间"])
            use_time = QTableWidgetItem(query_card["使用时间"])
            self.tbe_card.setItem(row, 0, id)
            self.tbe_card.setItem(row, 1, card_key)
            self.tbe_card.setItem(row, 2, card_type)
            self.tbe_card.setItem(row, 3, gen_time)
            self.tbe_card.setItem(row, 4, sale_time)
            self.tbe_card.setItem(row, 5, use_time)
        return True

    def on_timer_sec_timeout(self):
        global cur_time_format
        cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")

    def on_timer_min_timeout(self):
        global today, path_log
        cur_day = cur_time_format[:10]
        # 1 检测日期改变
        if cur_day != today:
            today = cur_day
            path_log = f"C:\\net_auth_{today}.log"
            sql_table_update("2用户管理", {"今日登录次数": 0, "今日解绑次数": 0})
        # 2 刷新所有用户状态(状态为在线, 且心跳时间在15分钟前, 置为离线)
        now_date_time = datetime.datetime.strptime(cur_time_format, "%Y-%m-%d %H:%M:%S")
        offset_date_time = datetime.timedelta(minutes=-15)
        due_time = (now_date_time + offset_date_time).strftime("%Y-%m-%d %H:%M:%S")
        sql_table_update_ex("2用户管理", "状态='离线'", f"状态='在线' and 心跳时间<'{due_time}'")

    def thd_accept_client(self):
        log_append_content("服务端已开启, 准备接受客户请求...")
        while True:
            log_append_content("等待接收新客户端...")
            try:
                client_socket, client_addr = tcp_socket.accept()
            except:
                break
            log_append_content(f"客户端IP地址及端口: {client_addr}, 已分配客服套接字")
            Thread(target=self.thd_serve_client, args=(client_socket, client_addr), daemon=True).start()
        log_append_content("服务端已关闭, 停止接受客户端请求...")

    def thd_serve_client(self, client_socket: socket.socket, client_addr: tuple):
        while True:
            log_append_content("等待客户端发出消息中...")
            try:  # 若任务消息都没收到, 客户端直接退出, 会抛出异常
                recv_bytes = client_socket.recv(1024)
            except:
                recv_bytes = ""
            if not recv_bytes:  # 若客户端退出,会收到一个空str
                break
            # json字符串 转 py字典
            json_str = recv_bytes.decode()
            client_info_dict = json.loads(json_str)
            log_append_content(f"收到客户端的消息: {json_str}")
            # 服务端消息处理
            msg_type = client_info_dict["消息类型"]
            client_info_dict.pop("消息类型")
            msg_func_dict = {
                "注册": deal_reg,
                "登录": deal_login,
                "充值": deal_pay,
                "改密": deal_modify,
                "心跳": deal_heart,
                "离线": deal_offline,
                "解绑": deal_unbind,
            }
            func = msg_func_dict.get(msg_type)
            if func is None:
                log_append_content(f"消息类型不存在: {msg_type}")
            else:
                func(client_socket, client_info_dict)
        log_append_content(f"客户端{client_addr}已断开连接, 服务结束")
        client_socket.close()


# 处理_注册
def deal_reg(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[注册] 正在处理账号: {account}")
    reg_ret = False

    if sql_table_query("2用户管理", {"账号": account}):  # 查询账号是否存在
        detail = "注册失败, 此账号已被注册!"
    else:  # 不存在则插入记录
        client_info_dict["注册时间"] = cur_time_format
        client_info_dict["到期时间"] = cur_time_format
        reg_ret = sql_table_insert("2用户管理", client_info_dict)
        detail = "注册成功" if reg_ret else "注册失败, 数据库异常"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 把注册结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "注册", "结果": reg_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)


# 处理_登录
def deal_login(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[登录] 正在处理账号: {account}")
    pwd = client_info_dict["密码"]
    machine_code = client_info_dict["机器码"]
    login_ret, query_user = False, {}

    query_user_list = sql_table_query("2用户管理", {"账号": account})  # 判断账号是否存在
    if query_user_list:
        query_user = query_user_list[0]
        if query_user["状态"] == "冻结":
            detail = "登录失败, 此账号已冻结"
        elif query_user["状态"] == "在线":
            detail = "登录失败, 此账号在线中, 请15分钟后再试"
        elif cur_time_format > query_user["到期时间"]:
            detail = "登录失败, 此账号已到期"
        elif pwd == query_user["密码"]:  # 判断密码是否符合
            if query_user["机器码"] in (machine_code, ""):  # 判断机器码是否符合
                login_ret = True
                detail = "登录成功"
            else:
                detail = "登录失败, 异机登录请先解绑"
        else:
            detail = "登录失败, 密码错误"
    else:
        detail = "登录失败, 账号不存在"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 把登录结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "登录", "结果": login_ret, "详情": detail, "账号": account}
    send_to_client(client_socket, server_info_dict)
    # 把客户端发送过来的数据记录到数据库
    update_db_user_login_info(client_info_dict, query_user, login_ret)


# 处理_充值
def deal_pay(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[充值] 正在处理账号: {account}")
    card_key = client_info_dict["卡号"]
    pay_ret = False

    query_card_list = sql_table_query("3卡密管理", {"卡号": card_key})  # 查询数据库, 判断卡密是否存在
    if query_card_list:
        query_card = query_card_list[0]
        if not query_card["使用时间"]:  # 卡密未被使用
            query_user_list = sql_table_query("2用户管理", {"账号": account})  # 查找账号是否存在
            if query_user_list:  # 账号存在
                query_user = query_user_list[0]
                # 更新卡密的使用时间
                sql_table_update("3卡密管理", {"使用时间": cur_time_format}, {"卡号": card_key})
                # 更新账号到期时间
                type_time_dict = {"天卡": 1, "周卡": 7, "月卡": 30, "季卡": 120, "年卡": 365, "永久卡": 3650}
                card_type = query_card["卡类型"]
                delta_day = type_time_dict[card_type]
                pay_ret = sql_table_update_ex("2用户管理", f"到期时间 = date_add(到期时间, interval {delta_day} day)")
                detail = "充值成功" if pay_ret else "充值失败, 数据库异常"
            else:
                detail = "充值失败, 账号不存在"
        else:  # 卡密被使用
            detail = "充值失败, 此卡密已被使用"
    else:  # 没查到数据
        detail = "充值失败, 卡密不存在"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 把充值结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "充值", "结果": pay_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)

# 处理_改密
def deal_modify(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[改密] 正在处理账号: {account}")
    qq = client_info_dict["QQ"]
    new_pwd = client_info_dict["密码"]
    modify_ret = False

    # 查询数据库, 判断用户是否存在
    query_user_list = sql_table_query("2用户管理", {"账号": account})  # 查找账号是否存在
    if query_user_list:
        query_user = query_user_list[0]
        query_qq = query_user["QQ"]
        if qq == query_qq:
            modify_ret = sql_table_update("2用户管理", {"密码": new_pwd}, {"账号": account})
            detail = "改密成功" if modify_ret else "改密失败, 数据库异常"
        else:
            detail = "改密失败, QQ错误"
    else:
        detail = "改密失败, 账号不存在"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 把改密结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "改密", "结果": modify_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)


# 处理_心跳
def deal_heart(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[心跳] 正在处理账号: {account}")
    comment = client_info_dict["备注"]
    update_dict = {"心跳时间": cur_time_format, "备注": comment}
    query_user_list = sql_table_query("2用户管理", {"账号": account})  # 查找账号是否存在
    if query_user_list:
        query_user = query_user_list[0]
        if query_user["状态"] == "冻结":  # 服务端已冻结此账号, 则令其下线
            heart_ret, detail = "下线", "此账号已被冻结"
        elif cur_time_format > query_user["到期时间"]:
            heart_ret, detail = "下线", "此账号已到期"
        elif "发现" in comment:  # 发现客户危险行为
            heart_ret, detail = "下线", "检测到非法程序"
            update_dict["状态"] = "冻结"
        else:
            heart_ret, detail = "正常", ""
            update_dict["状态"] = "在线"
    else:
        heart_ret, detail = "下线", "此账号不存在"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 发送消息回客户端
    server_info_dict = {"消息类型": "心跳", "结果": heart_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)
    # 更新用户数据
    sql_table_update("2用户管理", update_dict, {"账号": account})


# 处理_离线
def deal_offline(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[离线] 正在处理账号: {account}")
    comment = client_info_dict["备注"]
    update_dict = {"心跳时间": cur_time_format, "备注": comment, "状态": "离线"}

    query_user_list = sql_table_query("2用户管理", {"账号": account})  # 查找账号是否存在
    if query_user_list:
        query_user = query_user_list[0]
        # 若账号在线时有非法操作, 服务端自动冻结其账号, 客户端离线时不要改变冻结状态
        if query_user["状态"] == "冻结":
            update_dict["状态"] = "冻结"
            detail = "此账号已冻结, 未设置离线状态"
        else:
            detail = "已设置为离线状态"
    else:
        detail = "此账号不存在"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 更新用户数据
    sql_table_update("2用户管理", update_dict, {"账号": account})


# 处理_解绑
def deal_unbind(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[解绑] 正在处理账号: {account}")
    pwd = client_info_dict["密码"]
    unbind_ret = False
    query_user_list = sql_table_query("2用户管理", {"账号": account})
    if query_user_list:  # 判断账号是否存在
        query_user = query_user_list[0]
        if query_user["机器码"] == "":  # 若原本就没绑定机器
            detail = "此账号未绑定机器, 无需解绑"
        elif query_user["状态"] == "在线":
            detail = "此账号在线中, 无法解绑, 请15分钟后再试"
        elif query_user["状态"] == "冻结":
            detail = "此账号已冻结, 无法解绑"
        elif pwd == query_user["密码"]:  # 密码正确, 把机器码置为空
            ori_unbind_count = int(query_user["今日解绑次数"])
            unbind_count = ori_unbind_count + 1
            unbind_ret = sql_table_update("2用户管理", {"机器码": "", "今日解绑次数": unbind_count}, {"账号": account})
            detail = "解绑成功" if unbind_ret else "解绑失败, 数据库异常"
        else:
            detail = "解绑失败, 密码错误"
    else:
        detail = "解绑失败, 账号不存在"
    # 记录到日志
    log_append_content(f"账号{account} {detail}")
    # 发送消息回客户端
    server_info_dict = {"消息类型": "解绑", "结果": unbind_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)


# 发送数据给客户端
def send_to_client(client_socket: socket.socket, server_info_dict: dict):
    # py字典 转 json字符串
    json_str = json.dumps(server_info_dict, ensure_ascii=False)
    # 向客户端回复注册结果
    try:
        client_socket.send(json_str.encode())
        log_append_content(f"向客户端回复成功: {json_str}")
    except Exception as e:
        log_append_content(f"向客户端回复失败: {e}")


# 更新数据库_用户登录数据
def update_db_user_login_info(client_info_dict: dict, query_user: dict, login_ret: bool):
    if not query_user:  # 若该账号不存在
        return
    account = query_user["账号"]
    # 无论是否登录成功, 登录次数+1
    update_dict = {"今日登录次数": query_user["今日登录次数"] + 1,
                   "操作系统": client_info_dict["操作系统"],
                   "备注": client_info_dict["备注"]}
    # 若登录成功, 才更新
    if login_ret:
        update_dict["机器码"] = client_info_dict["机器码"]
        update_dict["上次登录时间"] = client_info_dict["上次登录时间"]
        update_dict["上次登录IP"] = client_info_dict["上次登录IP"]
    sql_table_update("2用户管理", update_dict, {"账号": account})


# 表_插入, 成功返回True, 否则返回False
def sql_table_insert(table_name: str, val_dict: dict):
    # keys = "account, pwd,qq, machine_code, reg_ip"
    keys = ", ".join(val_dict.keys())
    vals = tuple(val_dict.values())
    # occupys = "%s, %s, %s, %s, %s, %s"
    occupys = ", ".join(["%s"] * len(val_dict))
    # 准备SQL语句
    sql = f"insert {table_name}({keys}) values({occupys});"
    ret = False
    try:
        ret = cursor.execute(sql, vals)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表插入异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表插入结果: {ret}")
    return ret


# 表_查询, 成功返回字典列表, 否则返回空列表
def sql_table_query(table_name: str, condition_dict={}):
    fields = condition_dict.keys()
    vals = tuple(condition_dict.values())
    condition = [f"{field}=%s" for field in fields]
    condition = " and ".join(condition)
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"select * from {table_name} where {condition};"
    else:
        sql = f"select * from {table_name};"
    ret = []
    try:
        cursor.execute(sql, vals)  # 执行SQL语句
        ret = cursor.fetchall()  # 获取查询结果, 没查到返回空列表
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表查询异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表查询结果: {ret}")
    return ret

# 表_查询, 成功返回字典列表, 否则返回空列表
def sql_table_query_ex(table_name: str, condition=""):
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"select * from {table_name} where {condition};"
    else:
        sql = f"select * from {table_name};"
    ret = []
    try:
        cursor.execute(sql)  # 执行SQL语句
        ret = cursor.fetchall()  # 获取查询结果, 没查到返回空列表
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表查询异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表查询结果: {ret}")
    return ret

# 表_更新, 成功返回True, 否则返回False
def sql_table_update(table_name: str, update_dict: dict, condition_dict={}):
    update_fields = update_dict.keys()
    update_vals = tuple(update_dict.values())
    update = [f"{field}=%s" for field in update_fields]
    update = ", ".join(update)

    condition_fields = condition_dict.keys()
    condition_vals = tuple(condition_dict.values())
    condition = [f"{field}=%s" for field in condition_fields]
    condition = " and ".join(condition)
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"update {table_name} set {update} where {condition};"
    else:
        sql = f"update {table_name} set {update};"
    ret = False
    try:
        ret = cursor.execute(sql, update_vals + condition_vals)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表更新异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表更新结果: {ret}")
    return ret

# 表_更新扩展, 成功返回True, 否则返回False
def sql_table_update_ex(table_name: str, update: str, condition=""):
    if condition:
        sql = f"update {table_name} set {update} where {condition};"
    else:
        sql = f"update {table_name} set {update};"
    ret = False
    try:
        ret = cursor.execute(sql)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表更新异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表更新结果: {ret}")
    return ret

# 表_删除
def sql_table_del(table_name: str, condition_dict: dict):
    fields = condition_dict.keys()
    vals = tuple(condition_dict.values())
    condition = [f"{field}=%s" for field in fields]
    condition = " and ".join(condition)
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"delete from {table_name} where {condition};"
    else:
        sql = f"delete from {table_name};"  # 全删
    ret = False
    try:
        ret = cursor.execute(sql, vals)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表删除异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表删除结果: {ret}")
    return ret

# 表_删除扩展
def sql_table_del_ex(table_name: str, condition: str):
    if condition:
        sql = f"delete from {table_name} where {condition};"
    else:
        sql = f"delete from {table_name};"  # 全删
    ret = False
    try:
        ret = cursor.execute(sql)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        log_append_content(f"表删除异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表删除结果: {ret}")
    return ret


# 生成随机卡密
def gen_rnd_card_key(lenth=30):
    char_list = "0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
    max_idx = len(char_list) - 1
    card_key = ""
    for _ in range(lenth):
        idx = randint(0, max_idx)
        char = char_list[idx]
        card_key += char
    return card_key


# 日志读内容
def log_read_content() -> str:
    # 读取文件内容
    content = ""
    # 读的时候, 若没有文件会报错
    try:
        with open(path_log, "r", encoding="utf8") as f:
            content = f.read()
    except:
        print(f"未找到文件:{path_log}")
    return content


# 日志添加内容
def log_append_content(content: str):
    with lock:
        with open(path_log, "a", encoding="utf8") as f:
            text = f"{cur_time_format} {content}\n"
            f.write(text)


if __name__ == '__main__':
    log_append_content("------------------------------------------------------------------")
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 应用程序
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(qss_style)
    # 窗口
    wnd_server = WndServer()
    wnd_server.show()
    # 消息循环
    sys.exit(app.exec_())

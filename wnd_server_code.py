import sys, os
import time, datetime
import json
from threading import Thread, Lock

from PySide2.QtGui import QIcon, QCloseEvent, QTextCursor
from PySide2.QtWidgets import QApplication, QStyleFactory, QMainWindow, QLabel, \
    QMessageBox, QAbstractItemView, QTableWidget, QTableWidgetItem, QSizePolicy, \
    QLayout
from PySide2.QtCore import Qt, QTimer
import pymysql
import socket

from ui.wnd_server import Ui_WndServer
from res import qres

lock = Lock()
cur_time_stamp = time.time()
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
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/proj.png"), "项目管理")
        self.tool_bar.addAction(QIcon(":/users.png"), "用户管理")
        self.tool_bar.addAction(QIcon(":/card.png"), "卡密管理")
        self.tool_bar.addAction(QIcon(":/log.png"), "执行日志")
        # 所有表头可视化
        self.tbe_proj.horizontalHeader().setVisible(True)
        self.tbe_user.horizontalHeader().setVisible(True)
        self.tbe_card.horizontalHeader().setVisible(True)
        # 所有表格设置不可编辑
        # self.tbe_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tbe_online_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tbe_card.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 项目管理表
        # self.tbe_proj
        # 用户管理表
        account, pwd, email, machine_code, reg_ip, reg_time, due_time, is_forbid = [i for i in range(8)]
        self.tbe_user.setColumnWidth(account, 100)
        self.tbe_user.setColumnWidth(pwd, 100)
        self.tbe_user.setColumnWidth(email, 100)
        self.tbe_user.setColumnWidth(machine_code, 90)
        self.tbe_user.setColumnWidth(reg_ip, 100)
        self.tbe_user.setColumnWidth(reg_time, 120)
        self.tbe_user.setColumnWidth(due_time, 120)
        self.tbe_user.setColumnWidth(is_forbid, 70)
        # 卡密管理表
        card_key, type, gen_time, use_time, proj_name = [i for i in range(5)]
        self.tbe_card.setColumnWidth(card_key, 260)
        self.tbe_card.setColumnWidth(type, 80)
        self.tbe_card.setColumnWidth(gen_time, 150)
        self.tbe_card.setColumnWidth(use_time, 150)
        self.tbe_card.setColumnWidth(proj_name, 150)

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_card_gen.clicked.connect(self.on_btn_card_gen_clicked)
        self.btn_card_refresh.clicked.connect(self.on_btn_card_refresh_clicked)

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
            sql_table_insert("3卡密管理", val_dict)
        self.show_info(f"已生成{card_num}张{card_type}")

    def on_btn_card_refresh_clicked(self):
        tbe = self.tbe_card
        dict_list = sql_table_query("3卡密管理")
        tbe.setRowCount(len(dict_list))
        for row, card_info in enumerate(dict_list):
            card_key = QTableWidgetItem(card_info["卡号"])
            card_type = QTableWidgetItem(card_info["卡类型"])
            gen_time = QTableWidgetItem(card_info["制卡时间"])
            use_time = QTableWidgetItem(card_info["使用时间"])
            self.tbe_card.setItem(row, 0, card_key)
            self.tbe_card.setItem(row, 1, card_type)
            self.tbe_card.setItem(row, 2, gen_time)
            self.tbe_card.setItem(row, 3, use_time)

    def on_timer_timeout(self):
        global cur_time_stamp, cur_time_format, today, path_log
        cur_time_stamp += 1
        cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")
        cur_day = cur_time_format[:10]
        if cur_day != today:  # 日期改变
            today = cur_day
            path_log = f"C:\\net_auth_{today}.log"
            update_dict = {"今日登录次数": 0, "今日换绑次数": 0}
            sql_table_update("2用户管理", update_dict)

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
                "心跳": deal_heart,
                "离线": deal_offline,
            }
            func = msg_func_dict.get(msg_type)
            if func is None:
                log_append_content(f"消息类型不存在: {msg_type}")
            else:
                func(client_socket, client_info_dict)
        log_append_content(f"客户端{client_addr}已断开连接, 服务结束")
        client_socket.close()


# 处理-注册
def deal_reg(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[注册] 正在处理账号: {account}")
    # 查询账号是否存在, 不存在则插入记录
    if sql_table_query("2用户管理", {"账号": account}):  # 若查到数据
        reg_ret = False
        detail = f"失败, 账号{account}已被注册!"
        log_append_content(detail)
    else:  # 表插入记录
        client_info_dict["注册时间"] = cur_time_format
        client_info_dict["到期时间"] = cur_time_format
        reg_ret = sql_table_insert("2用户管理", client_info_dict)
        detail = f"账号{account}注册成功!" if reg_ret else f"账号{account}注册失败!"
        log_append_content(detail)
    # 把注册结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "注册", "结果": reg_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)


# 处理-登录
def deal_login(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[登录] 正在处理账号: {account}")
    pwd = client_info_dict["密码"]
    machine_code = client_info_dict["机器码"]
    reason, login_ret, query_user = "原因未知", False, {}
    query_user_list = sql_table_query("2用户管理", {"账号": account})
    if query_user_list:  # 判断账号是否存在
        query_user = query_user_list[0]
        if query_user["状态"] == "冻结":
            reason = query_user["备注"]
        elif cur_time_format > query_user["到期时间"]:
            reason = "此账号已到期"
        elif pwd == query_user["密码"]:  # 判断密码是否符合
            if query_user["机器码"] in (machine_code, ""):  # 判断机器码是否符合
                login_ret = True
            else:
                reason = "异机登录, 请先换绑"
        else:
            reason = "密码错误"
    else:
        reason = "账号不存在"
    detail = f"登录成功" if login_ret else f"登录失败, {reason}"
    # 把登录结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "登录", "结果": login_ret, "详情": detail, "账号": account}
    send_to_client(client_socket, server_info_dict)
    # 把客户端发送过来的数据记录到数据库
    update_db_user_login_info(client_info_dict, query_user, login_ret)


# 处理-充值
def deal_pay(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["账号"]
    log_append_content(f"[充值] 正在处理账号: {account}")
    card_key = client_info_dict["卡号"]
    # 查询数据库, 判断卡密是否存在
    dict_list = sql_table_query("3卡密管理", {"卡号": card_key})
    pay_ret = False
    if dict_list:
        card_info = dict_list[0]
        if card_info["使用时间"] == "":  # 卡密未被使用
            query_user_list = sql_table_query("2用户管理", {"账号": account})  # 查找账号是否存在
            if query_user_list:  # 账号存在
                query_user = query_user_list[0]
                # 更新卡密的使用时间
                sql_table_update("3卡密管理", {"使用时间": cur_time_format}, {"卡号": card_key})
                # 更新账号到期时间
                type_time_dict = {"天卡": 1, "周卡": 7, "月卡": 30, "季卡": 120, "年卡": 365, "永久卡": 3650}
                card_type = card_info["卡类型"]
                delta_day = type_time_dict[card_type]
                pay_ret = update_db_user_due_time(query_user, delta_day)
                detail = "充值成功" if pay_ret else "充值失败"
            else:
                detail = "失败, 账号不存在"
        else:  # 卡密被使用
            detail = "失败, 此卡密已被使用"
    else:  # 没查到数据
        detail = "失败, 卡密不存在"
    # 把登录结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "充值", "结果": pay_ret, "详情": detail}
    send_to_client(client_socket, server_info_dict)

# 处理-心跳
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
    else:
        heart_ret, detail = "下线", "此账号不存在"
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
    # 更新用户数据
    sql_table_update("2用户管理", update_dict, {"账号": account})


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


# 更新数据库_用户到期时间
def update_db_user_due_time(query_user: dict, delta_day: int):
    account = query_user["账号"]
    if query_user["到期时间"] == "" or query_user["到期时间"] < cur_time_format:
        # 若所有用户表中此项记录没有到期时间, 或到期时间在今天以前, 则从当前时间开始加
        ori_time = cur_time_format
    else:  # 否则, 取记录上的到期时间
        ori_time = query_user["到期时间"]
    now_date_time = datetime.datetime.strptime(ori_time, "%Y-%m-%d %H:%M:%S")
    offset_date_time = datetime.timedelta(days=delta_day)
    due_time = (now_date_time + offset_date_time).strftime("%Y-%m-%d %H:%M:%S")
    ret = sql_table_update("2用户管理", {"到期时间": due_time}, {"账号": account})
    return ret


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
        update_dict["状态"] = "在线"
        update_dict["机器码"] = client_info_dict["机器码"]
        update_dict["上次登录时间"] = client_info_dict["上次登录时间"]
        update_dict["上次登录IP"] = client_info_dict["上次登录IP"]
    sql_table_update("2用户管理", update_dict, {"账号": account})


# 表-插入, 成功返回True, 否则返回False
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


# 表-查询, 成功返回字典列表, 否则返回空列表
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
    except:
        log_append_content(f"表查询异常: {e}")
        db.rollback()  # 数据库回滚
    log_append_content(f"表查询结果: {ret}")
    return ret


# 表-更新, 成功返回True, 否则返回False
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


# 生成随机卡密
def gen_rnd_card_key(lenth=30):
    char_list = "0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
    max_idx = len(char_list) - 1
    card_key = ""
    for _ in range(lenth):
        idx = rnd(0, max_idx)
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

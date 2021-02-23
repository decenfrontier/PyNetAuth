import sys, os
import time, datetime
import json
import base64
import urllib.request, ssl
from threading import Thread, Lock
from random import randint
import logging
from logging.handlers import TimedRotatingFileHandler

from PySide2.QtGui import QIcon, QCloseEvent, QTextCursor, QCursor
from PySide2.QtWidgets import QApplication, QStyleFactory, QMainWindow, QLabel, \
    QMessageBox, QTableWidgetItem, QMenu, QAction, QInputDialog, QLineEdit, QListWidgetItem
from PySide2.QtCore import Qt, QTimer
import pymysql
import socket

import wnd_server_rc
from ui.wnd_server import Ui_WndServer
import crypto_

lock = Lock()
cur_time_fmt = time.strftime("%Y-%m-%d %H:%M:%S")
today = cur_time_fmt[:10]
PATH_SAVE = "C:\\MyServer"
PATH_LOG = "\\".join([PATH_SAVE, "log"])
PATH_LOG_INFO = "\\".join([PATH_LOG, "info"])
PATH_LOG_WARN = "\\".join([PATH_LOG, "warn"])
PATH_JSON_SERVER = "\\".join([PATH_SAVE, "server.json"])
cfg_server = {"更新网址": "", "发卡网址": "", "注册赠送天数": 0, "免费解绑次数": 0, "解绑扣除小时": 0}

server_ip = "0.0.0.0"
server_port = 47123
server_ver = "2.3.5"
aes_key = "csbt34.ydhl12s"  # AES密钥
aes = crypto_.AesEncryption(aes_key)
enc_aes_key = crypto_.encrypt_rsa(crypto_.public_key_client, aes_key)

user_comment = {
    "正常": "*d#fl1I@34rt7%gh.",
    "危险": "*d#flI1@34rt7%gh.",
}


class Log():
    def __init__(self):
        dir_create(PATH_LOG)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 创建handler对象
        self.handler_info = TimedRotatingFileHandler(filename=PATH_LOG_INFO, when="midnight", interval=1, backupCount=7)
        self.handler_info.setFormatter(logging.Formatter("%(asctime)s  %(message)s"))
        self.handler_info.setLevel(logging.INFO)
        self.handler_warn = TimedRotatingFileHandler(filename=PATH_LOG_WARN, when="midnight", interval=1, backupCount=7)
        self.handler_warn.setFormatter(logging.Formatter("%(asctime)s  %(message)s"))
        self.handler_warn.setLevel(logging.WARNING)
        # 添加handler
        self.logger.addHandler(self.handler_info)
        self.logger.addHandler(self.handler_warn)

    def info(self, msg: str):
        self.logger.info(msg)

    def warn(self, msg: str):
        self.logger.warning(msg)


class WndServer(QMainWindow, Ui_WndServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_mysql()
        self.init_net_auth()
        self.init_instance_field()
        self.init_wnd()
        self.init_controls()
        self.init_menus()
        self.cfg_read()
        self.init_sig_slot()
        self.move(0, 160)

    # 关闭套接字和数据库
    def closeEvent(self, event: QCloseEvent):
        tcp_socket.close()
        cursor.close()
        db.close()

    # 读取配置
    def cfg_read(self):
        cfg_load = json_file_to_dict(PATH_JSON_SERVER, cfg_server)
        cfg_server.update(cfg_load)

        self.edt_proj_url_update.setText(cfg_server["更新网址"])
        self.edt_proj_url_card.setText(cfg_server["发卡网址"])
        self.edt_proj_unbind_sub_hour.setText(str(cfg_server["解绑扣除小时"]))
        self.edt_proj_reg_gift_day.setText(str(cfg_server["注册赠送天数"]))
        self.edt_proj_free_unbind_count.setText(str(cfg_server["免费解绑次数"]))

    # 写入配置
    def cfg_write(self):
        cfg_server["发卡网址"] = self.edt_proj_url_card.text()
        cfg_server["更新网址"] = self.edt_proj_url_update.text()
        cfg_server["免费解绑次数"] = int(self.edt_proj_free_unbind_count.text())
        cfg_server["注册赠送天数"] = int(self.edt_proj_reg_gift_day.text())
        cfg_server["解绑扣除小时"] = int(self.edt_proj_unbind_sub_hour.text())

        dict_to_json_file(cfg_server, PATH_JSON_SERVER)

    def init_mysql(self):
        try:
            global db, cursor
            # 创建数据库对象
            db = pymysql.connect(
                host="119.29.167.100",
                port=3306,
                user="root",
                password="659457",
                database="net_auth"
            )
            # 创建游标对象, 指定返回一个字典列表, 获取的每条数据的类型为字典(默认是元组)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            log.info("连接数据库成功")
        except Exception as e:
            log.info(f"mysql连接失败: {e}")
            QMessageBox.critical(self, "错误", f"mysql连接失败: {e}")
            raise e
        # 清零用户管理表今日次数
        lastest_time = sql_table_query("select max(最后更新时间) from 2用户管理;")[0]["max(最后更新时间)"]
        lastest_day = str(lastest_time)[:10]
        if lastest_day != today:
            log.info("新的一天到了, 清零用户管理表今日次数")
            sql_table_update("update 2用户管理 set 今日登录次数=0, 今日解绑次数=0;")  # "2用户管理", {"今日登录次数": 0, "今日解绑次数": 0}
        # 插入每日流水表今日记录
        if not sql_table_query("select * from 5每日流水 where 日期=%s;", (today,)):  # "5每日流水", {"日期": today}
            log.info("新的一天到了, 插入每日流水表今日记录")
            sql_table_insert_ex("5每日流水", {"日期": today})

    # 初始化tcp连接
    def init_net_auth(self):
        try:
            global tcp_socket
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.bind((server_ip, server_port))  # 主机号+端口号
            tcp_socket.listen(128)  # 允许同时有XX个客户端连接此服务器, 排队等待被服务
            Thread(target=self.thd_accept_client, daemon=True).start()
        except Exception as e:
            log.info(f"tcp连接失败: {e}")
            QMessageBox.critical(self, "错误", f"tcp连接失败: {e}")
            raise e

    # 初始化实例属性
    def init_instance_field(self):
        # ---------------------- 状态栏 --------------------
        self.lbe_1 = QLabel("<提示> : ")
        self.lbe_info = QLabel("窗口初始化成功")
        self.lbe_2 = QLabel("最新客户端版本:")
        self.lbe_latest_ver = QLabel("x.x.x")
        # ---------------------- 定时器 ----------------------
        self.timer_sec = QTimer()
        self.timer_sec.timeout.connect(self.on_timer_sec_timeout)
        self.timer_sec.start(1000)
        self.timer_min = QTimer()
        self.timer_min.timeout.connect(self.on_timer_min_timeout)
        self.timer_min.start(1000 * 60 * 15)

    def init_wnd(self):
        self.setWindowTitle(f"Ip: {server_ip}  Port: {server_port}  Ver: {server_ver}")
        self.setWindowIcon(QIcon(":/server.png"))

    def init_controls(self):
        # ------------------------------ 堆叠窗口 ------------------------------
        self.stack_widget.setCurrentIndex(0)
        # ------------------------------ 状态栏 ------------------------------
        self.latest_ver = sql_table_query("select max(客户端版本) from 1项目管理;")[0]["max(客户端版本)"]
        self.lbe_latest_ver.setText(self.latest_ver)
        self.status_bar.addWidget(self.lbe_1)
        self.status_bar.addWidget(self.lbe_info)
        self.status_bar.addPermanentWidget(self.lbe_2)
        self.status_bar.addPermanentWidget(self.lbe_latest_ver)
        # ------------------------------ 工具栏 ------------------------------
        self.tool_bar.addAction(QIcon(":/proj.png"), "项目管理")
        self.tool_bar.addAction(QIcon(":/users.png"), "用户管理")
        self.tool_bar.addAction(QIcon(":/card.png"), "卡密管理")
        self.tool_bar.addAction(QIcon(":/flow.png"), "每日流水")
        self.tool_bar.addAction(QIcon(":/log.png"), "IP与日志")
        # ------------------------------ 表 格 ------------------------------
        # 所有表头可视化
        self.tbe_proj.horizontalHeader().setVisible(True)
        self.tbe_user.horizontalHeader().setVisible(True)
        self.tbe_card.horizontalHeader().setVisible(True)
        # 项目管理表
        id, ver, notice, login, reg, unbind, last_update_time = [i for i in range(7)]
        self.tbe_proj.setColumnWidth(id, 40)
        self.tbe_proj.setColumnWidth(ver, 70)
        self.tbe_proj.setColumnWidth(notice, 260)
        self.tbe_proj.setColumnWidth(login, 80)
        self.tbe_proj.setColumnWidth(reg, 80)
        self.tbe_proj.setColumnWidth(unbind, 80)
        self.tbe_proj.setColumnWidth(last_update_time, 130)
        # 用户管理表
        id, account, pwd, qq, state, heart_time, due_time, last_login_time, last_login_ip, \
        last_login_place, today_login_count, today_unbind_count, machine_code, reg_time, \
        opration_system, comment, last_update_time = [i for i in range(17)]
        self.tbe_user.setColumnWidth(id, 40)
        self.tbe_user.setColumnWidth(account, 70)
        self.tbe_user.setColumnWidth(pwd, 40)
        self.tbe_user.setColumnWidth(qq, 70)
        self.tbe_user.setColumnWidth(state, 50)
        self.tbe_user.setColumnWidth(heart_time, 130)
        self.tbe_user.setColumnWidth(due_time, 130)
        self.tbe_user.setColumnWidth(last_login_time, 130)
        self.tbe_user.setColumnWidth(machine_code, 180)
        self.tbe_user.setColumnWidth(reg_time, 130)
        self.tbe_user.setColumnWidth(opration_system, 175)
        self.tbe_user.setColumnWidth(last_update_time, 130)
        # 卡密管理表
        id, card_key, type, gen_time, export_time, use_time = [i for i in range(6)]
        self.tbe_card.setColumnWidth(id, 40)
        self.tbe_card.setColumnWidth(card_key, 250)
        self.tbe_card.setColumnWidth(type, 60)
        self.tbe_card.setColumnWidth(gen_time, 130)
        self.tbe_card.setColumnWidth(export_time, 130)
        self.tbe_card.setColumnWidth(use_time, 130)
        # 自定义数据表
        id, key, val, en_val = [i for i in range(4)]
        self.tbe_custom.setColumnWidth(id, 40)
        self.tbe_custom.setColumnWidth(key, 100)
        self.tbe_custom.setColumnWidth(val, 120)
        self.tbe_custom.setColumnWidth(en_val, 200)
        # 每日流水表
        id, date = 0, 1
        self.tbe_everyday.setColumnWidth(id, 40)
        self.tbe_everyday.setColumnWidth(date, 80)
        # IP管理表
        id, today_connect_time = 0, 3
        self.tbe_ip.setColumnWidth(id, 40)
        self.tbe_ip.setColumnWidth(today_connect_time, 320)
        # 显示全部
        self.show_all_tbe_proj()
        self.show_all_tbe_user()
        self.show_all_tbe_card()
        self.show_all_tbe_custom()
        self.show_all_tbe_everyday()
        self.show_all_tbe_ip()

    def init_menus(self):
        # 项目管理表
        self.tbe_proj.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_proj = QMenu()
        self.action_proj_show_all = QAction("显示全部版本信息")
        self.action_proj_del_sel = QAction("删除选中版本")
        self.action_proj_all_allow_sel = QAction("选中版本全部允许")
        self.action_proj_all_forbid_sel = QAction("选中版本全部禁止")
        self.menu_tbe_proj.addAction(self.action_proj_show_all)
        self.menu_tbe_proj.addAction(self.action_proj_del_sel)
        self.menu_tbe_proj.addSeparator()
        self.menu_tbe_proj.addActions([self.action_proj_all_allow_sel,
                                       self.action_proj_all_forbid_sel])
        self.action_proj_show_all.triggered.connect(self.show_all_tbe_proj)
        self.action_proj_del_sel.triggered.connect(self.on_action_proj_del_sel_triggered)
        self.action_proj_all_allow_sel.triggered.connect(self.on_action_proj_all_allow_sel_triggered)
        self.action_proj_all_forbid_sel.triggered.connect(self.on_action_proj_all_forbid_sel_triggered)
        self.tbe_proj.customContextMenuRequested.connect(
            lambda: self.menu_tbe_proj.exec_(QCursor.pos())
        )

        # 用户管理表
        self.tbe_user.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_user = QMenu()
        self.action_user_show_all = QAction("显示全部用户信息")
        self.action_user_comment_sel = QAction("备注选中用户")
        self.action_user_state_sel = QAction("设置选中用户状态")  # 二级菜单
        self.action_user_del_sel = QAction("删除选中用户")
        # --------------------------------------------------------
        self.action_user_frozen_ip = QAction("冻结指定IP下的所有用户")
        self.action_user_frozen_sel = QAction("冻结选中用户")
        self.action_user_unfrozen_sel = QAction("解冻选中用户")
        # --------------------------------------------------------
        self.action_user_charge_sel = QAction("续费选中用户")
        self.action_user_charge_all = QAction("续费全部用户")
        self.menu_tbe_user.addActions([self.action_user_show_all,
                                       self.action_user_comment_sel,
                                       self.action_user_state_sel,
                                       self.action_user_del_sel])
        self.menu_tbe_user.addSeparator()
        self.menu_tbe_user.addActions([self.action_user_frozen_ip,
                                       self.action_user_frozen_sel,
                                       self.action_user_unfrozen_sel])
        self.menu_tbe_user.addSeparator()
        self.menu_tbe_user.addActions([self.action_user_charge_sel,
                                       self.action_user_charge_all])
        self.action_user_show_all.triggered.connect(self.show_all_tbe_user)
        self.action_user_comment_sel.triggered.connect(self.on_action_user_comment_sel_triggered)
        self.action_user_del_sel.triggered.connect(self.on_action_user_del_sel_triggered)
        self.action_user_frozen_ip.triggered.connect(self.on_action_user_frozen_ip_triggered)
        self.action_user_frozen_sel.triggered.connect(self.on_action_user_frozen_sel_triggered)
        self.action_user_unfrozen_sel.triggered.connect(self.on_action_user_unfrozen_sel_triggered)
        self.action_user_charge_sel.triggered.connect(self.on_action_user_charge_sel_triggered)
        self.action_user_charge_all.triggered.connect(self.on_action_user_charge_all_triggered)
        self.tbe_user.customContextMenuRequested.connect(
            lambda: self.menu_tbe_user.exec_(QCursor.pos())
        )
        self.sub_menu_user_state = QMenu()
        self.sub_action_offline = QAction("离线")
        self.sub_action_frozen = QAction("冻结")
        self.sub_action_online = QAction("在线")
        self.action_user_state_sel.setMenu(self.sub_menu_user_state)
        self.sub_menu_user_state.addActions([self.sub_action_offline,
                                             self.sub_action_frozen,
                                             self.sub_action_online])
        self.sub_action_offline.triggered.connect(self.on_action_user_state_triggered)
        self.sub_action_frozen.triggered.connect(self.on_action_user_state_triggered)
        self.sub_action_online.triggered.connect(self.on_action_user_state_triggered)

        # 卡密管理表
        self.tbe_card.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_card = QMenu()
        self.action_card_show_all = QAction("显示全部卡密信息")
        self.action_card_show_unuse = QAction("显示未使用卡密")
        self.action_card_show_export = QAction("显示已导出卡密")
        self.action_card_del_sel = QAction("删除选中卡密")
        self.action_card_del_used = QAction("删除已使用卡密")
        self.action_card_export_sel = QAction("导出选中卡密")
        self.menu_tbe_card.addActions([self.action_card_show_all,
                                       self.action_card_show_unuse,
                                       self.action_card_show_export])
        self.menu_tbe_card.addSeparator()
        self.menu_tbe_card.addActions([self.action_card_del_sel,
                                       self.action_card_del_used])
        self.menu_tbe_card.addSeparator()
        self.menu_tbe_card.addAction(self.action_card_export_sel)
        self.action_card_show_all.triggered.connect(self.show_all_tbe_card)
        self.action_card_show_unuse.triggered.connect(self.on_action_card_show_unuse_triggered)
        self.action_card_show_export.triggered.connect(self.on_action_card_show_export_triggered)
        self.action_card_del_sel.triggered.connect(self.on_action_card_del_sel_triggered)
        self.action_card_del_used.triggered.connect(self.on_action_card_del_used_triggered)
        self.action_card_export_sel.triggered.connect(self.on_action_card_export_sel_triggered)
        self.tbe_card.customContextMenuRequested.connect(
            lambda: self.menu_tbe_card.exec_(QCursor.pos())
        )

        # 自定义数据表
        self.tbe_custom.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_custom = QMenu()
        self.action_custom_show_all = QAction("显示全部自定义数据")
        self.action_custom_del_sel = QAction("删除选中自定义数据")
        self.menu_tbe_custom.addActions([self.action_custom_show_all,
                                         self.action_custom_del_sel])
        self.action_custom_show_all.triggered.connect(self.show_all_tbe_custom)
        self.action_custom_del_sel.triggered.connect(self.on_action_custom_del_sel_triggered)
        self.tbe_custom.customContextMenuRequested.connect(
            lambda: self.menu_tbe_custom.exec_(QCursor.pos())
        )

        # 每日流水表
        self.tbe_everyday.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_everyday = QMenu()
        self.action_everyday_show_all = QAction("显示全部流水信息")
        self.menu_tbe_everyday.addAction(self.action_everyday_show_all)
        self.action_everyday_show_all.triggered.connect(self.show_all_tbe_everyday)
        self.tbe_everyday.customContextMenuRequested.connect(
            lambda: self.menu_tbe_everyday.exec_(QCursor.pos())
        )

        # IP管理表
        self.tbe_ip.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_ip = QMenu()
        self.action_ip_show_all = QAction("显示全部IP信息")
        self.menu_tbe_ip.addAction(self.action_ip_show_all)
        self.action_ip_show_all.triggered.connect(self.show_all_tbe_ip)
        self.tbe_ip.customContextMenuRequested.connect(
            lambda: self.menu_tbe_ip.exec_(QCursor.pos())
        )

    def init_sig_slot(self):
        # 工具栏
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        # 按钮相关
        self.btn_proj_confirm.clicked.connect(self.on_btn_proj_confirm_clicked)
        self.btn_user_query.clicked.connect(self.on_btn_user_query_clicked)
        self.btn_card_gen.clicked.connect(self.on_btn_card_gen_clicked)
        self.btn_custom_confirm.clicked.connect(self.on_btn_custom_confirm_clicked)
        self.btn_cfg_save.clicked.connect(self.on_btn_cfg_save_clicked)
        # 表格相关
        self.tbe_proj.cellClicked.connect(self.on_tbe_proj_cellClicked)
        self.tbe_custom.cellClicked.connect(self.on_tbe_custom_cellClicked)
        # 列表框
        self.lst_log.itemDoubleClicked.connect(self.on_lst_log_itemDoubleClicked)

    def show_info(self, text):
        self.lbe_info.setText(text)
        log.info(text)

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        if action_name == "项目管理":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "用户管理":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "卡密管理":
            self.stack_widget.setCurrentIndex(2)
        elif action_name == "每日流水":
            self.stack_widget.setCurrentIndex(3)
        elif action_name == "IP与日志":
            self.stack_widget.setCurrentIndex(4)
            self.refresh_lst_log()

    def on_btn_proj_confirm_clicked(self):
        client_ver = self.edt_proj_client_ver.text()
        pub_notice = self.pedt_proj_public_notice.toPlainText()
        url_update = self.edt_proj_url_update.text()
        url_card = self.edt_proj_url_card.text()
        reg_gift_day = self.edt_proj_reg_gift_day.text()
        free_unbind_count = self.edt_proj_free_unbind_count.text()
        unbind_sub_hour = self.edt_proj_unbind_sub_hour.text()
        allow_login = int(self.chk_proj_login.isChecked())
        allow_reg = int(self.chk_proj_reg.isChecked())
        allow_unbind = int(self.chk_proj_unbind.isChecked())
        val_dict = {
            "客户端版本": client_ver,
            "客户端公告": pub_notice,
            "更新网址": url_update,
            "发卡网址": url_card,
            "注册赠送天数": reg_gift_day,
            "免费解绑次数": free_unbind_count,
            "解绑扣除小时": unbind_sub_hour,
            "允许登录": allow_login,
            "允许注册": allow_reg,
            "允许解绑": allow_unbind,
        }
        if sql_table_query("select * from 1项目管理 where 客户端版本=%s;", (client_ver,)):
            num = sql_table_update_ex("1项目管理", val_dict, {"客户端版本": client_ver})
            self.show_info(f"{num}个版本更新成功")
        else:
            num = sql_table_insert_ex("1项目管理", val_dict)
            self.show_info(f"{num}个版本添加成功")
        self.show_all_tbe_proj()

    def on_btn_user_query_clicked(self):
        field = self.cmb_user_field.currentText()
        operator = self.cmb_user_operator.currentText()
        value = self.edt_user_value.text()
        query_user_list = sql_table_query(f"select * from 2用户管理 where {field} {operator} %s;", (value,))
        num = len(query_user_list)
        self.show_info(f"查询到{num}个符合条件的用户")
        self.refresh_tbe_user(query_user_list)

    def on_btn_card_gen_clicked(self):
        gen_time = cur_time_fmt
        card_type = self.cmb_card_type.currentText()
        card_num = int(self.edt_card_num.text())
        for i in range(card_num):
            card_key = gen_rnd_card_key()
            val_dict = {
                "卡号": card_key,
                "卡类型": card_type,
                "制卡时间": gen_time
            }
            if sql_table_insert_ex("3卡密管理", val_dict):
                self.show_info(f"生成{card_type}{card_key}成功")
            else:
                self.show_info(f"生成{card_type}{card_key}失败")
        self.show_all_tbe_card()

    def on_btn_custom_confirm_clicked(self):
        key = self.edt_custom_key.text()
        val = self.edt_custom_val.text()
        eval = aes.encrypt(val)
        self.edt_custom_eval.setText(eval)
        query_custom_list = sql_table_query("select * from 4自定义数据 where 键=%s;", (key,))
        if query_custom_list:  # 查到, 则更新
            num = sql_table_update("update 4自定义数据 set 值=%s, 加密值=%s where 键=%s;", (val, eval, key))
            self.show_info(f"{num}个自定义数据更新成功")
        else:  # 没查到, 则插入
            num = sql_table_insert("insert 4自定义数据(键, 值, 加密值) values(%s, %s, %s);", (key, val, eval))
            self.show_info(f"{num}个自定义数据添加成功")
        self.show_all_tbe_custom()

    def on_btn_cfg_save_clicked(self):
        self.cfg_write()
        self.show_info("保存项目配置成功")

    def on_tbe_proj_cellClicked(self, row: int, col: int):
        self.edt_proj_client_ver.setText(self.tbe_proj.item(row, 1).text())
        self.pedt_proj_public_notice.setPlainText(self.tbe_proj.item(row, 2).text())
        self.chk_proj_login.setChecked(int(self.tbe_proj.item(row, 3).text()))
        self.chk_proj_reg.setChecked(int(self.tbe_proj.item(row, 4).text()))
        self.chk_proj_unbind.setChecked(int(self.tbe_proj.item(row, 5).text()))

    def on_tbe_custom_cellClicked(self, row: int, col: int):
        self.edt_custom_key.setText(self.tbe_custom.item(row, 1).text())
        self.edt_custom_val.setText(self.tbe_custom.item(row, 2).text())
        self.edt_custom_eval.setText(self.tbe_custom.item(row, 3).text())

    def on_lst_log_itemDoubleClicked(self, item: QListWidgetItem):
        def thd_cmd(path):
            os.system(f"notepad {path}")

        file = item.text()
        path_log_file = "\\".join([PATH_LOG, file])
        Thread(target=thd_cmd, args=(path_log_file,), daemon=True).start()

    def on_action_proj_del_sel_triggered(self):
        item_list = self.tbe_proj.selectedItems()
        ver_set = {self.tbe_proj.item(it.row(), 1).text() for it in item_list}
        if not ver_set:
            return
        ret = QMessageBox.information(self, "警告", "是否确认删除选中版本?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        vers = "','".join(ver_set)  # "1项目管理", f"客户端版本 in ('{vers}')"
        num = sql_table_del(f"delete from 1项目管理 where 客户端版本 in ('{vers}');")
        self.show_info(f"{num}个版本删除成功")
        self.show_all_tbe_proj()

    def on_action_proj_all_allow_sel_triggered(self):
        item_list = self.tbe_proj.selectedItems()
        ver_set = {self.tbe_proj.item(it.row(), 1).text() for it in item_list}
        if not ver_set:
            return
        vers = "','".join(ver_set)
        num = sql_table_update(f"update 1项目管理 set 允许登录=1,允许注册=1,允许解绑=1 where 客户端版本 in ('{vers}');")
        self.show_info(f"{num}个版本全部允许成功")
        self.show_all_tbe_proj()

    def on_action_proj_all_forbid_sel_triggered(self):
        item_list = self.tbe_proj.selectedItems()
        ver_set = {self.tbe_proj.item(it.row(), 1).text() for it in item_list}
        if not ver_set:
            return
        vers = "','".join(ver_set)
        num = sql_table_update(f"update 1项目管理 set 允许登录=0,允许注册=0,允许解绑=0 where 客户端版本 in ('{vers}');")
        self.show_info(f"{num}个版本全部禁止成功")
        self.show_all_tbe_proj()

    def on_action_user_comment_sel_triggered(self):
        item_list = self.tbe_user.selectedItems()
        account_set = {self.tbe_user.item(it.row(), 1).text() for it in item_list}
        if not account_set:
            return
        comment, ok_pressed = QInputDialog.getText(self, "备注", "备注:", QLineEdit.Normal)
        if not ok_pressed:
            return
        accounts = "','".join(account_set)  # "2用户管理", f"备注='{comment}'", f"账号 in ('{accounts}')"
        num = sql_table_update(f"update 2用户管理 set 备注='{comment}' where 账号 in ('{accounts}');")
        self.show_info(f"{num}个用户备注成功")
        self.show_all_tbe_user()

    def on_action_user_frozen_ip_triggered(self):
        frozen_ip, ok_pressed = QInputDialog.getText(self, "冻结IP下的所有账号", "IP:", QLineEdit.Normal)
        if not ok_pressed or not frozen_ip:
            return
        num = sql_table_update(f"update 2用户管理 set 状态='冻结', 备注='冻结IP下的所有账号' where 上次登录IP='{frozen_ip}';")
        self.show_info(f"{num}个用户冻结IP成功")
        self.show_all_tbe_user()

    def on_action_user_frozen_sel_triggered(self):
        item_list = self.tbe_user.selectedItems()
        account_set = {self.tbe_user.item(it.row(), 1).text() for it in item_list}
        if not account_set:
            return
        comment, ok_pressed = QInputDialog.getText(self, "冻结", "备注原因:", QLineEdit.Normal)
        if not ok_pressed:
            return
        accounts = "','".join(account_set)  # "2用户管理", f"状态='冻结', 备注='{comment}'", f"账号 in ('{accounts}')"
        num = sql_table_update(f"update 2用户管理 set 状态='冻结', 备注='{comment}' where 账号 in ('{accounts}');")
        self.show_info(f"{num}个账号冻结成功")
        self.show_all_tbe_user()

    def on_action_user_unfrozen_sel_triggered(self):
        item_list = self.tbe_user.selectedItems()
        account_set = {self.tbe_user.item(it.row(), 1).text() for it in item_list
                       if self.tbe_user.item(it.row(), 4).text() == "冻结"}
        if not account_set:
            return
        ret = QMessageBox.information(self, "提示", "确定解冻选中账号?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        accounts = "','".join(account_set)
        # 解冻时备注应加天数  "2用户管理", f"状态='离线', 备注=datediff(到期时间, 心跳时间)", f"账号 in ('{accounts}')"
        num = sql_table_update(f"update 2用户管理 set 状态='离线', 备注=datediff(到期时间, 心跳时间) where 账号 in ('{accounts}');")
        self.show_info(f"{num}个账号解冻成功")
        self.show_all_tbe_user()

    def on_action_user_charge_sel_triggered(self):
        item_list = self.tbe_user.selectedItems()
        account_set = {self.tbe_user.item(it.row(), 1).text() for it in item_list}
        if not account_set:
            return
        gift_day, ok_pressed = QInputDialog.getInt(self, "续费选中(选中行, 且状态不为'', 冻结)",
                                                   "续费天数:", QLineEdit.Normal)
        if not ok_pressed:
            return
        accounts = "','".join(account_set)
        # 若用户已到期, 从now()开始加, 否则从到期时间开始加
        num = sql_table_update(f"update 2用户管理 set 到期时间 = if(到期时间 < now(), date_add(now(), interval {gift_day} day), "
                               f"date_add(到期时间, interval {gift_day} day)) where 账号 in ('{accounts}') and 状态 not in ('', '冻结');")
        self.show_info(f"{num}个用户续费{gift_day}天成功")
        self.show_all_tbe_user()

    def on_action_user_charge_all_triggered(self):
        gift_day, ok_pressed = QInputDialog.getInt(self, "续费全部(没到期, 且状态不为'', 冻结)",
                                                   "续费天数:", QLineEdit.Normal)
        if not ok_pressed:
            return
        # 若用户已到期, 从now()开始加, 否则从到期时间开始加
        num = sql_table_update(f"update 2用户管理 set 到期时间 = if(到期时间 < now(), date_add(now(), interval {gift_day} day), "
                               f"date_add(到期时间, interval {gift_day} day)) where now() < 到期时间 and 状态 not in ('', '冻结');")
        self.show_info(f"{num}个用户续费{gift_day}天成功")
        self.show_all_tbe_user()

    def on_action_user_del_sel_triggered(self):
        item_list = self.tbe_user.selectedItems()
        account_set = {self.tbe_user.item(it.row(), 1).text() for it in item_list}
        if not account_set:
            return
        ret = QMessageBox.information(self, "提示", "确定删除选中账号?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret != QMessageBox.Yes:
            return
        accounts = "','".join(account_set)
        num = sql_table_del(f"delete from 2用户管理 where 账号 in ('{accounts}');")
        self.show_info(f"{num}个用户删除成功")
        self.show_all_tbe_user()

    def on_action_user_state_triggered(self):
        state = self.sender().text()
        item_list = self.tbe_user.selectedItems()
        account_set = {self.tbe_user.item(it.row(), 1).text() for it in item_list}
        if not account_set:
            return
        accounts = "','".join(account_set)
        num = sql_table_update(f"update 2用户管理 set 状态='{state}' where 账号 in ('{accounts}');")
        self.show_info(f"{num}个用户设置状态 {state} 成功")
        self.show_all_tbe_user()

    def on_action_card_show_unuse_triggered(self):
        query_card_list = sql_table_query("select * from 3卡密管理 where 使用时间 is null;")
        self.refresh_tbe_card(query_card_list)
        self.show_info("已显示未使用卡密")

    def on_action_card_show_export_triggered(self):
        query_card_list = sql_table_query("select * from 3卡密管理 where 导出时间 is not null;")
        self.refresh_tbe_card(query_card_list)
        self.show_info("已显示已导出卡密")

    def on_action_card_del_sel_triggered(self):
        ret = QMessageBox.information(self, "提示", "是否确定删除选中的卡号?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        item_list = self.tbe_card.selectedItems()
        card_set = {self.tbe_card.item(it.row(), 1).text() for it in item_list}
        if not card_set:
            return
        cards = "','".join(card_set)  # "3卡密管理", f"卡号 in ('{cards}')"
        sql_table_del(f"delete from 3卡密管理 where 卡号 in ('{cards}');")
        self.show_info("已删除选中的卡号")
        self.show_all_tbe_card()

    def on_action_card_del_used_triggered(self):
        ret = QMessageBox.information(self, "提示", "是否确定删除已使用的卡号?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret != QMessageBox.Yes:
            return
        sql_table_del("delete from 3卡密管理 where 使用时间 is not null;")
        self.show_all_tbe_card()

    def on_action_card_export_sel_triggered(self):
        item_list = self.tbe_card.selectedItems()
        card_set = {self.tbe_card.item(it.row(), 1).text() for it in item_list}
        if not card_set:
            return
        cards = "','".join(card_set)
        # 导出未使用的选中卡号 "3卡密管理", f"导出时间='{cur_time_fmt}'", f"卡号 in ('{cards}') and 使用时间 is null"
        num = sql_table_update(f"update 3卡密管理 set 导出时间='{cur_time_fmt}' where 卡号 in ('{cards}') and 使用时间 is null;")
        export_card_key = "\n".join(card_set)
        self.pedt_card_export.setPlainText(export_card_key)
        # 复制到剪切板
        clip_copy(export_card_key)
        self.show_info(f"{num}个卡号已复制到剪切板")
        self.show_all_tbe_card()

    def on_action_custom_del_sel_triggered(self):
        item_list = self.tbe_custom.selectedItems()
        key_set = {self.tbe_custom.item(it.row(), 1).text() for it in item_list}
        if not key_set:
            return
        keys = "','".join(key_set)  # "4自定义数据", f"键 in ('{keys}')"
        num = sql_table_del(f"delete from 4自定义数据 where 键 in ('{keys}');")
        self.show_info(f"{num}个自定义数据删除成功")
        self.show_all_tbe_custom()

    def show_all_tbe_proj(self):
        # 读取表全部内容
        query_proj_list = sql_table_query("select * from 1项目管理;")
        self.refresh_tbe_proj(query_proj_list)
        # 刷新最新客户端版本号
        self.latest_ver = sql_table_query("select max(客户端版本) from 1项目管理;")[0]["max(客户端版本)"]
        self.lbe_latest_ver.setText(self.latest_ver)

    def show_all_tbe_user(self):
        # 刷新ip归属地
        self.refresh_ip_location()
        # 读取表全部内容
        query_user_list = sql_table_query("select * from 2用户管理;")
        self.refresh_tbe_user(query_user_list)

    def show_all_tbe_card(self):
        query_card_list = sql_table_query("select * from 3卡密管理;")
        self.refresh_tbe_card(query_card_list)

    def show_all_tbe_custom(self):
        # 读取表全部内容
        query_custom_list = sql_table_query("select * from 4自定义数据;")
        self.refresh_tbe_custom(query_custom_list)
        # 刷新 第一批自定义数据 和 第二批自定义数据
        key_eval_dict = {custom_dict["键"]: custom_dict["加密值"] for custom_dict in query_custom_list}
        self.custom1 = {"pic": key_eval_dict.pop("pic"),
                        "zk": key_eval_dict.pop("zk")}
        self.custom2 = key_eval_dict

    def show_all_tbe_everyday(self):
        # 读取用户表内容, 获取今日活跃用户数, 在线用户数
        active_user_num = sql_table_query("select count(*) from 2用户管理 where date_format(心跳时间,'%Y-%m-%d')="
                                                 "date_format(now(), '%Y-%m-%d');")[0]["count(*)"]
        online_user_num = sql_table_query("select count(*) from 2用户管理 where 状态='在线';")[0]["count(*)"]
        # 更新每日流水表
        sql_table_update(f"update 5每日流水 set 活跃用户数=%s, 在线用户数=%s where 日期=%s;",
                         (active_user_num, online_user_num, today))
        # 读取每日流水表全部内容
        query_everyday_list = sql_table_query("select * from 5每日流水;")
        self.refresh_tbe_everyday(query_everyday_list)

    def show_all_tbe_ip(self):
        # 按今日连接次数从大到小排序显示
        query_ip_list = sql_table_query("select * from 6ip管理 order by 今日连接次数 desc;")
        print(query_ip_list)
        self.refresh_tbe_ip(query_ip_list)

    def refresh_tbe_proj(self, query_proj_list):
        self.tbe_proj.setRowCount(len(query_proj_list))
        for row, query_proj in enumerate(query_proj_list):
            self.tbe_proj.setItem(row, 0, QTableWidgetItem(str(query_proj["ID"])))
            self.tbe_proj.setItem(row, 1, QTableWidgetItem(query_proj["客户端版本"]))
            self.tbe_proj.setItem(row, 2, QTableWidgetItem(query_proj["客户端公告"]))
            self.tbe_proj.setItem(row, 3, QTableWidgetItem(str(query_proj["允许登录"])))
            self.tbe_proj.setItem(row, 4, QTableWidgetItem(str(query_proj["允许注册"])))
            self.tbe_proj.setItem(row, 5, QTableWidgetItem(str(query_proj["允许解绑"])))
            self.tbe_proj.setItem(row, 6, QTableWidgetItem(str(query_proj["最后更新时间"])))

    def refresh_tbe_user(self, query_user_list):
        self.tbe_user.setRowCount(len(query_user_list))
        for row, query_user in enumerate(query_user_list):
            query_user["到期时间"] = "" if query_user["到期时间"] is None else str(query_user["到期时间"])
            query_user["心跳时间"] = "" if query_user["心跳时间"] is None else str(query_user["心跳时间"])
            query_user["上次登录时间"] = "" if query_user["上次登录时间"] is None else str(query_user["上次登录时间"])
            query_user["注册时间"] = "" if query_user["注册时间"] is None else str(query_user["注册时间"])
            query_user["最后更新时间"] = "" if query_user["最后更新时间"] is None else str(query_user["最后更新时间"])
            self.tbe_user.setItem(row, 0, QTableWidgetItem(str(query_user["ID"])))
            self.tbe_user.setItem(row, 1, QTableWidgetItem(query_user["账号"]))
            self.tbe_user.setItem(row, 2, QTableWidgetItem("***"))
            self.tbe_user.setItem(row, 3, QTableWidgetItem(query_user["QQ"]))
            self.tbe_user.setItem(row, 4, QTableWidgetItem(query_user["状态"]))
            self.tbe_user.setItem(row, 5, QTableWidgetItem(query_user["到期时间"]))
            self.tbe_user.setItem(row, 6, QTableWidgetItem(query_user["心跳时间"]))
            self.tbe_user.setItem(row, 7, QTableWidgetItem(query_user["上次登录时间"]))
            self.tbe_user.setItem(row, 8, QTableWidgetItem(query_user["上次登录IP"]))
            self.tbe_user.setItem(row, 9, QTableWidgetItem(query_user["上次登录地"]))
            self.tbe_user.setItem(row, 10, QTableWidgetItem(str(query_user["今日登录次数"])))
            self.tbe_user.setItem(row, 11, QTableWidgetItem(str(query_user["今日解绑次数"])))
            self.tbe_user.setItem(row, 12, QTableWidgetItem(query_user["机器码"]))
            self.tbe_user.setItem(row, 13, QTableWidgetItem(query_user["注册时间"]))
            self.tbe_user.setItem(row, 14, QTableWidgetItem(query_user["操作系统"]))
            self.tbe_user.setItem(row, 15, QTableWidgetItem(query_user["备注"]))
            self.tbe_user.setItem(row, 16, QTableWidgetItem(query_user["最后更新时间"]))

    def refresh_tbe_card(self, query_card_list):
        self.tbe_card.setRowCount(len(query_card_list))
        for row, query_card in enumerate(query_card_list):
            query_card["制卡时间"] = "" if query_card["制卡时间"] is None else str(query_card["制卡时间"])
            query_card["导出时间"] = "" if query_card["导出时间"] is None else str(query_card["导出时间"])
            query_card["使用时间"] = "" if query_card["使用时间"] is None else str(query_card["使用时间"])
            id = QTableWidgetItem(str(query_card["ID"]))
            card_key = QTableWidgetItem(query_card["卡号"])
            card_type = QTableWidgetItem(query_card["卡类型"])
            gen_time = QTableWidgetItem(query_card["制卡时间"])
            export_time = QTableWidgetItem(query_card["导出时间"])
            use_time = QTableWidgetItem(query_card["使用时间"])
            self.tbe_card.setItem(row, 0, id)
            self.tbe_card.setItem(row, 1, card_key)
            self.tbe_card.setItem(row, 2, card_type)
            self.tbe_card.setItem(row, 3, gen_time)
            self.tbe_card.setItem(row, 4, export_time)
            self.tbe_card.setItem(row, 5, use_time)

    def refresh_tbe_custom(self, query_custom_list: list):
        self.tbe_custom.setRowCount(len(query_custom_list))
        for row, query_custom in enumerate(query_custom_list):
            self.tbe_custom.setItem(row, 0, QTableWidgetItem(str(query_custom["ID"])))
            self.tbe_custom.setItem(row, 1, QTableWidgetItem(query_custom["键"]))
            self.tbe_custom.setItem(row, 2, QTableWidgetItem(query_custom["值"]))
            self.tbe_custom.setItem(row, 3, QTableWidgetItem(query_custom["加密值"]))

    def refresh_tbe_everyday(self, query_everyday_list: list):
        self.tbe_everyday.setRowCount(len(query_everyday_list))
        for row, query_everyday in enumerate(query_everyday_list):
            query_everyday["日期"] = "" if query_everyday["日期"] is None else str(query_everyday["日期"])
            query_everyday["最后更新时间"] = "" if query_everyday["最后更新时间"] is None else str(query_everyday["最后更新时间"])
            self.tbe_everyday.setItem(row, 0, QTableWidgetItem(str(query_everyday["ID"])))
            self.tbe_everyday.setItem(row, 1, QTableWidgetItem(query_everyday["日期"]))
            self.tbe_everyday.setItem(row, 2, QTableWidgetItem(str(query_everyday["天卡充值数"])))
            self.tbe_everyday.setItem(row, 3, QTableWidgetItem(str(query_everyday["周卡充值数"])))
            self.tbe_everyday.setItem(row, 4, QTableWidgetItem(str(query_everyday["月卡充值数"])))
            self.tbe_everyday.setItem(row, 5, QTableWidgetItem(str(query_everyday["季卡充值数"])))
            self.tbe_everyday.setItem(row, 6, QTableWidgetItem(str(query_everyday["充值用户数"])))
            self.tbe_everyday.setItem(row, 7, QTableWidgetItem(str(query_everyday["活跃用户数"])))
            self.tbe_everyday.setItem(row, 8, QTableWidgetItem(str(query_everyday["在线用户数"])))
            self.tbe_everyday.setItem(row, 9, QTableWidgetItem(query_everyday["最后更新时间"]))

    def refresh_tbe_ip(self, query_ip_list: list):
        self.tbe_ip.setRowCount(len(query_ip_list))
        for row, query_ip in enumerate(query_ip_list):
            query_ip["最后更新时间"] = "" if query_ip["最后更新时间"] is None else str(query_ip["最后更新时间"])
            self.tbe_ip.setItem(row, 0, QTableWidgetItem(str(query_ip["ID"])))
            self.tbe_ip.setItem(row, 1, QTableWidgetItem(query_ip["IP地址"]))
            self.tbe_ip.setItem(row, 2, QTableWidgetItem(query_ip["归属地"]))
            self.tbe_ip.setItem(row, 3, QTableWidgetItem(query_ip["今日连接时间"]))
            self.tbe_ip.setItem(row, 4, QTableWidgetItem(str(query_ip["今日连接次数"])))
            self.tbe_ip.setItem(row, 5, QTableWidgetItem(query_ip["最后更新时间"]))

    def refresh_lst_log(self):
        self.lst_log.clear()
        self.lst_log.addItems(dir_get_files(PATH_LOG))

    # 刷新ip归属地
    def refresh_ip_location(self):
        def append_ip_location(ip: str):
            location = get_ip_location(ip)
            with mutex:
                ip_location_list.append((ip, location))

        # 获取用户表有但归属表没有的ip列表
        query_ip_list = sql_table_query("select distinct A.上次登录IP from 2用户管理 A left join 6ip管理 B "
                                               "on A.上次登录IP=B.IP地址 where B.IP地址 is null;")
        query_ip_list = [ip_dict["上次登录IP"] for ip_dict in query_ip_list]
        if query_ip_list:
            # 并发获取这些ip的归属地
            ip_location_list = []
            thd_pool = []
            mutex = Lock()
            for query_ip in query_ip_list:
                t = Thread(target=append_ip_location, args=(query_ip,))
                t.start()
                thd_pool.append(t)
            # 等待所有执行完
            [t.join() for t in thd_pool]
            if ip_location_list:
                # 把获取到的归属地信息插入到IP归属表
                ip_locations = str(ip_location_list).strip("[|]")
                log.info(f"新IP归属地信息: {ip_locations}")  # "('127.0.0.1', '本地'), ('39.128.151.56', '中国-云南-文山-移动')
                sql_table_insert(f"insert 6ip管理(IP地址, 归属地) values{ip_locations};")
        # 更新用户表的上次登录地
        sql_table_update("update 2用户管理 A inner join 6ip管理 B on A.上次登录IP=B.IP地址 set A.上次登录地=B.归属地;")

    def on_timer_sec_timeout(self):
        global cur_time_fmt
        cur_time_fmt = time.strftime("%Y-%m-%d %H:%M:%S")

    def on_timer_min_timeout(self):
        self.show_info("----------------------------- 每15分钟一轮的检测开始 -----------------------------")
        global today
        cur_day = cur_time_fmt[:10]

        # 1 检测日期改变
        if cur_day != today:
            today = cur_day
            # 1.1 更新日志
            self.show_info("新的一天到了, 清零用户管理表今日次数, 新增每日流水表今日记录")
            # 1.2 更新用户表每日次数
            sql_table_update("update 2用户管理 set 今日登录次数=0, 今日解绑次数=0;")
            # 1.3 插入流水表新记录
            sql_table_insert_ex("5每日流水", {"日期": today})
            # 1.4 更新IP表每日次数  "6ip管理", {"今日连接时间": "", "今日连接次数": 0}
            sql_table_update("update 6ip管理 set 今日连接次数=0;")
        # 2 刷新所有用户状态(状态为在线, 且心跳时间在15分钟前, 置为离线)
        sql_table_update("update 2用户管理 set 状态='离线' where 状态='在线' and 心跳时间 < date_sub(now(), interval -15 minute);")
        # 3 刷新显示所有表
        self.show_all_tbe_proj()
        self.show_all_tbe_user()
        self.show_all_tbe_card()
        self.show_all_tbe_custom()
        self.show_all_tbe_everyday()
        self.show_info("----------------------------- 每15分钟一轮的检测结束 -----------------------------")

    def thd_accept_client(self):
        log.info("服务端已开启, 准备接受客户请求...")
        while True:
            log.info("等待接收新客户端...")
            try:
                client_socket, client_addr = tcp_socket.accept()
            except:
                break
            ip = client_addr[0]
            log.info(f"新接收客户端{ip}, 已分配客服套接字")
            sql_table_update("update 6ip管理 set 今日连接次数=今日连接次数+1 where IP地址=%s;", (ip,))
            Thread(target=self.thd_serve_client, args=(client_socket, ip), daemon=True).start()
        log.info("服务端已关闭, 停止接受客户端请求...")

    def thd_serve_client(self, client_socket: socket.socket, ip: str):
        while True:
            log.info("等待客户端发出消息中...")
            try:  # 若任务消息都没收到, 客户端直接退出, 会抛出异常
                recv_bytes = client_socket.recv(4096)
            except:
                recv_bytes = ""
            if not recv_bytes:  # 若客户端退出,会收到一个空str
                break
            # base85解码
            json_str = base64.b85decode(recv_bytes).decode()
            log.info(f"收到客户端{client_socket.getpeername()}的消息: {json_str}")
            # json字符串 转 py字典
            client_info_dict = json.loads(json_str)
            msg_type = client_info_dict["消息类型"]
            client_content_str = client_info_dict["内容"]
            # 把内容json字符串 转 py字典
            if msg_type == "初始":  # 若为初始类型的消息
                # json字符串 转 py字典
                client_content_dict = json.loads(client_content_str)
            else:  # 若不为初始类型的消息
                # 先aes解密, 获取json字符串
                client_content_str = aes.decrypt(client_content_str)
                # json字符串 转 py字典
                client_content_dict = json.loads(client_content_str)
            msg_func_dict = {
                "初始": deal_init,
                "锟斤拷": deal_proj,
                "烫烫烫": deal_custom1,
                "屯屯屯": deal_custom2,
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
                log.info(f"消息类型不存在: {msg_type}")
            else:
                func(client_socket, client_content_dict)
        log.info(f"客户端{ip}已断开连接, 服务结束")
        client_socket.close()


# 处理_初始
def deal_init(client_socket: socket.socket, client_content_dict: dict):
    ip = client_socket.getpeername()
    log.info(f"[初始] 正在处理IP: {ip}")

    if client_content_dict["备注"] == user_comment["危险"]:  # 客户端数据被修改, 记录到日志
        ret = False
        detail = "???"
        machine_code = client_content_dict["机器码"]
        log.warn(f"[初始Warn] IP:{ip}, MC:{machine_code}, 全局变量被修改")
    else:  # 若用户没有用OD修改掉这个数据, 才把RSA加密数据发过去
        ret = True
        detail = enc_aes_key
    # 把注册结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "初始",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)


# 处理_项目
def deal_proj(client_socket: socket.socket, client_content_dict: dict):
    ip = client_socket.getpeername()
    log.info(f"[项目] 正在处理IP: {ip}")

    client_ver = client_content_dict["版本号"]  # "1项目管理", {"客户端版本": client_ver}
    query_proj_list = sql_table_query("select * from 1项目管理 where 客户端版本=%s;", (client_ver,))
    if query_proj_list:
        ret = True
        query_proj = query_proj_list[0]
        detail = {
            "最新版本": wnd_server.latest_ver,
            "客户端公告": query_proj["客户端公告"],
            "允许登录": query_proj["允许登录"],
            "允许注册": query_proj["允许注册"],
            "允许解绑": query_proj["允许解绑"],
            "更新网址": cfg_server["更新网址"],
            "发卡网址": cfg_server["发卡网址"],
        }
    else:
        ret = False
        detail = "客户端版本过低, 请下载最新版本"
    # 把处理_项目数据结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "锟斤拷",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)


# 处理_自定义数据1
def deal_custom1(client_socket: socket.socket, client_content_dict: dict):
    ip = client_socket.getpeername()
    log.info(f"[自定义数据] 正在处理IP: {ip}")
    # 把第一批自定义数据整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "烫烫烫",
                        "内容": {"结果": True, "详情": wnd_server.custom1}}
    send_to_client(client_socket, server_info_dict)


# 处理_自定义数据2
def deal_custom2(client_socket: socket.socket, client_content_dict: dict):
    ip = client_socket.getpeername()
    log.info(f"[自定义数据] 正在处理IP: {ip}")
    # 把第二批自定义数据整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "屯屯屯",
                        "内容": {"结果": True, "详情": wnd_server.custom2}}
    send_to_client(client_socket, server_info_dict)


# 处理_注册
def deal_reg(client_socket: socket.socket, client_content_dict: dict):
    account = client_content_dict["账号"]
    log.info(f"[注册] 正在处理账号: {account}")
    ret = False

    # "2用户管理", {"账号": account}
    if not sql_table_query("select * from 2用户管理 where 账号=%s;", (account,)):  # 不存在则插入记录
        machine_code = client_content_dict["机器码"]  # "2用户管理", {"机器码": machine_code}
        query_user_list = sql_table_query("select * from 2用户管理 where 机器码=%s;", (machine_code,))
        if not query_user_list:  # 没有找到此机器码
            client_content_dict["注册时间"] = cur_time_fmt
            client_content_dict["到期时间"] = datetime.datetime.now() + datetime.timedelta(days=wnd_server.cfg["注册赠送天数"])
            # "2用户管理", client_content_dict
            ret = sql_table_insert_ex("2用户管理", client_content_dict)
            detail = "注册成功" if ret else "注册失败, 数据库异常"
        else:
            query_user = query_user_list[0]
            reged_account = query_user["账号"]
            detail = f"注册失败, 此机器已注册过账号{reged_account}"
    else:
        detail = "注册失败, 此账号已被注册!"
    # 记录到日志
    log.info(f"[注册] 账号{account} {detail}")
    # 把注册结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "注册",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)


# 处理_登录
def deal_login(client_socket: socket.socket, client_content_dict: dict):
    ip = client_socket.getpeername()[0]
    account = client_content_dict["账号"]
    log.info(f"[登录] 正在处理账号: {account}")
    pwd = client_content_dict["密码"]
    machine_code = client_content_dict["机器码"]
    ret, query_user = False, {}

    # "2用户管理", {"账号": account}
    query_user_list = sql_table_query("select * from 2用户管理 where 账号=%s;", (account,))  # 判断账号是否存在
    if query_user_list:
        query_user = query_user_list[0]
        if query_user["状态"] == "冻结":
            detail = "登录失败, 此账号已冻结"
        elif query_user["状态"] == "在线":
            detail = "登录失败, 此账号在线中, 请15分钟后再试"
        elif cur_time_fmt > str(query_user["到期时间"]):
            detail = "登录失败, 此账号已到期"
        elif pwd == query_user["密码"]:  # 判断密码是否符合
            if query_user["机器码"] in (machine_code, ""):  # 判断机器码是否符合
                ret = True
                detail = "登录成功"
                if query_user["状态"] == "":  # 新到期时间 = 到期时间 + (现在时间 - 注册时间)
                    detail = "首次登录成功, 开始倒计时"
                    sql_table_update("update 2用户管理 set 到期时间=date_add(到期时间, interval timestampdiff(minute, 注册时间, now()) minute);")
            else:
                detail = "登录失败, 异机登录请先解绑"
        else:
            detail = "登录失败, 密码错误"
    else:
        detail = "登录失败, 此账号不存在"
    # 记录到日志
    log.info(f"[登录] 账号{account} {detail}")
    # 把登录结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "登录",
                        "内容": {"结果": ret, "详情": detail, "账号": account}}
    send_to_client(client_socket, server_info_dict)
    # 把客户端发送过来的数据记录到数据库
    if not query_user:  # 若该账号不存在
        return
    account = query_user["账号"]
    # 无论是否登录成功, 登录次数+1
    update_dict = {"今日登录次数": query_user["今日登录次数"] + 1,
                   "操作系统": client_content_dict["操作系统"]}
    # 若登录成功, 才更新
    if ret:
        update_dict["机器码"] = client_content_dict["机器码"]
        update_dict["上次登录时间"] = cur_time_fmt
        update_dict["上次登录IP"] = ip
    sql_table_update_ex("2用户管理", update_dict, {"账号": account})


# 处理_充值
def deal_pay(client_socket: socket.socket, client_content_dict: dict):
    account = client_content_dict["账号"]
    log.info(f"[充值] 正在处理账号: {account}")
    card_key = client_content_dict["卡号"]
    ret = False

    query_user_list = sql_table_query_ex("2用户管理", {"账号": account})  # 查找账号是否存在
    if query_user_list:  # 账号存在
        query_user = query_user_list[0]
        query_card_list = sql_table_query_ex("3卡密管理", {"卡号": card_key})  # 查询数据库, 判断卡密是否存在
        if query_card_list:
            query_card = query_card_list[0]
            if not query_card["使用时间"]:  # 卡密未被使用
                # 更新账号到期时间
                type_time_dict = {"天卡": 1, "周卡": 7, "月卡": 30, "季卡": 120, "年卡": 365, "永久卡": 3650}
                card_type = query_card["卡类型"]
                delta_day = type_time_dict[card_type]
                account = query_user["账号"]
                # 若到期时间大于当前时间, 则从到期时间开始加, 否则从当前时间开始加
                ret = sql_table_update("update 2用户管理 set 到期时间 = if(到期时间 < now(), date_add(now(), interval %s day), "
                                        "date_add(到期时间, interval %s day)) where 账号=%s;", (delta_day, delta_day, account))
                if ret:  # todo: 多线程访问的安全性?是否要上锁
                    detail = "充值成功"
                    # 更新卡密的使用时间  "3卡密管理", {"使用时间": cur_time_fmt}, {"卡号": card_key}
                    sql_table_update("update 3卡密管理 set 使用时间=%s where 卡号=%s;", (cur_time_fmt, card_key))
                    # 更新流水充值用户数
                    card_pay_num = card_type + "充值数"
                    sql_table_update(f"update 5每日流水 set 充值用户数=充值用户数+1, {card_pay_num}={card_pay_num}+1 "
                                            f"where 日期='{today}';")
                else:
                    detail = "充值失败, 数据库异常"
            else:
                detail = "充值失败, 此卡密已被使用"
        else:  # 没查到数据
            detail = "充值失败, 此卡密不存在"
    else:
        detail = "充值失败, 此账号不存在"
    # 记录到日志
    log.info(f"[充值] 账号{account} {detail}")
    # 把充值结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "充值",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)


# 处理_改密
def deal_modify(client_socket: socket.socket, client_content_dict: dict):
    account = client_content_dict["账号"]
    log.info(f"[改密] 正在处理账号: {account}")
    qq = client_content_dict["QQ"]
    new_pwd = client_content_dict["密码"]
    ret = False

    # 查询数据库, 判断用户是否存在  "2用户管理", {"账号": account}
    query_user_list = sql_table_query("select * from 2用户管理 where 账号=%s;", (account,))  # 查找账号是否存在
    if query_user_list:
        query_user = query_user_list[0]
        query_qq = query_user["QQ"]
        if qq == query_qq:  # "2用户管理", {"密码": new_pwd}, {"账号": account}
            ret = sql_table_update("update 2用户管理 set 密码=%s where 账号=%s;", (new_pwd, account))
            detail = "改密成功" if ret else "改密失败, 数据库异常"
        else:
            detail = "改密失败, QQ错误"
    else:
        detail = "改密失败, 此账号不存在"
    # 记录到日志
    log.info(f"[改密] 账号{account} {detail}")
    # 把改密结果整理成py字典, 并发送给客户端
    server_info_dict = {"消息类型": "改密",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)


# 处理_心跳
def deal_heart(client_socket: socket.socket, client_content_dict: dict):
    account = client_content_dict["账号"]
    log.info(f"[心跳] 正在处理账号: {account}")
    comment = client_content_dict["备注"]
    machine_code = client_content_dict["机器码"]
    update_dict = {"心跳时间": cur_time_fmt, "备注": comment}
    query_user_list = sql_table_query("select * from 2用户管理 where 账号=%s;", (account,))  # 查找账号是否存在  "2用户管理", {"账号": account}
    if query_user_list:
        query_user = query_user_list[0]
        if query_user["状态"] == "冻结":  # 服务端已冻结此账号, 则令其下线
            ret, detail = "下线", "此账号已被冻结"
        elif cur_time_fmt > str(query_user["到期时间"]):
            ret, detail = "下线", "此账号已到期"
        elif comment == user_comment["危险"]:  # 发现客户危险行为
            ret, detail = "下线", "客户端数据被破解或修改"
            update_dict["状态"] = "冻结"
            update_dict["备注"] = detail
        elif query_user["机器码"] != machine_code:
            ret, detail = "下线", "异机登录此账号"
        else:
            ret, detail = "正常", ""
            update_dict["状态"] = "在线"
    else:
        ret, detail = "下线", "此账号不存在"
    # 记录到日志
    log.info(f"[心跳] 账号{account} {ret} {detail}")
    # 发送消息回客户端
    server_info_dict = {"消息类型": "心跳",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)
    # 更新用户数据
    sql_table_update_ex("2用户管理", update_dict, {"账号": account})


# 处理_离线
def deal_offline(client_socket: socket.socket, client_content_dict: dict):
    account = client_content_dict["账号"]
    log.info(f"[离线] 正在处理账号: {account}")
    comment = client_content_dict["备注"]
    comment = "危险" if comment == user_comment["危险"] else "正常"
    update_dict = {"心跳时间": cur_time_fmt, "备注": comment, "状态": "离线"}

    query_user_list = sql_table_query("select * from 2用户管理 where 账号=%s;", (account,))  # 查找账号是否存在  "2用户管理", {"账号": account}
    if query_user_list:
        query_user = query_user_list[0]
        # 若账号在线时有非法操作, 服务端自动冻结其账号, 客户端离线时不要改变冻结状态
        if query_user["状态"] == "冻结":
            update_dict["状态"] = "冻结"
            detail = "此账号已冻结, 未设置离线状态"
        else:
            detail = "已设置为离线状态"
    else:
        detail = f"此账号不存在, IP={client_socket.getpeername()}"
    # 记录到日志
    log.info(f"[离线] 账号{account} {detail}")
    # 更新用户数据
    sql_table_update_ex("2用户管理", update_dict, {"账号": account})


# 处理_解绑
def deal_unbind(client_socket: socket.socket, client_content_dict: dict):
    account = client_content_dict["账号"]
    log.info(f"[解绑] 正在处理账号: {account}")
    pwd = client_content_dict["密码"]
    ret = False
    query_user_list = sql_table_query("select * from 2用户管理 where 账号=%s;", (account,))
    if query_user_list:  # 判断账号是否存在
        query_user = query_user_list[0]
        if query_user["机器码"] == "":  # 若原本就没绑定机器
            detail = "无需解绑, 此账号未绑定机器"
        elif query_user["状态"] == "在线":
            detail = "解绑失败, 此账号在线中, 请15分钟后再试"
        elif query_user["状态"] == "冻结":
            detail = "解绑失败, 此账号已冻结, 无法解绑"
        elif pwd == query_user["密码"]:  # 密码正确, 把机器码置为空
            ret = sql_table_update("update 2用户管理 set 机器码='', 今日解绑次数=今日解绑次数+1 where 账号=%s;", (account,))
            detail = "解绑成功" if ret else "解绑失败, 数据库异常"
        else:
            detail = "解绑失败, 密码错误"
    else:
        detail = "解绑失败, 此账号不存在"
    # 记录到日志
    log.info(f"[解绑] 账号{account} {detail}")
    # 发送消息回客户端
    server_info_dict = {"消息类型": "解绑",
                        "内容": {"结果": ret, "详情": detail}}
    send_to_client(client_socket, server_info_dict)


# 发送数据给客户端
def send_to_client(client_socket: socket.socket, server_info_dict: dict):
    # 内容 转 json字符串
    server_info_dict["内容"] = json.dumps(server_info_dict["内容"], ensure_ascii=False)
    # 根据消息类型决定是否对内容aes加密
    if server_info_dict["消息类型"] != "初始":  # 若不为初始类型的消息
        # 对json内容进行aes加密
        server_info_dict["内容"] = aes.encrypt(server_info_dict["内容"])
    # 把整个服务端信息字典 转 json字符串
    json_str = json.dumps(server_info_dict, ensure_ascii=False)
    # json字符串 base85编码
    send_bytes = base64.b85encode(json_str.encode())
    try:
        client_socket.send(send_bytes)
        log.info(f"向客户端{client_socket.getpeername()}回复成功: {json_str}")
    except Exception as e:
        log.info(f"向客户端{client_socket.getpeername()}回复失败: {e}")


def sql_table_insert(sql: str, args=tuple()):
    num = 0
    try:
        num = cursor.execute(sql, args)  # 执行SQL语句
        db.commit()
    except Exception as e:
        log.warn(f"表插入异常: {sql} -----原因: {e}")
        db.rollback()
    log.info(f"表插入数量: {num}")
    return num

def sql_table_insert_ex(table_name: str, val_dict: dict):
    keys = ", ".join(val_dict.keys())
    vals = tuple(val_dict.values())
    occupys = ", ".join(["%s"] * len(val_dict))
    sql = f"insert {table_name}({keys}) values({occupys});"
    num = 0
    try:
        num = cursor.execute(sql, vals)
        db.commit()
    except Exception as e:
        log.warn(f"表插入异常: {sql} -----原因: {e}")
        db.rollback()
    log.info(f"表插入扩展数量: {num}")
    return num

def sql_table_query(sql: str, args=tuple()):
    query_list = []
    try:
        cursor.execute(sql, args)  # 执行SQL语句
        query_list = cursor.execute(sql, args)
        db.commit()
    except Exception as e:
        log.warn(f"表查询异常: {sql} -----原因: {e}")
        db.rollback()
    log.info(f"表查询结果: {query_list}")
    return query_list

def sql_table_query_ex(table_name: str, condition_dict={}):
    fields = condition_dict.keys()
    vals = tuple(condition_dict.values())
    condition = [f"{field}=%s" for field in fields]
    condition = " and ".join(condition)
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"select * from {table_name} where {condition};"
    else:
        sql = f"select * from {table_name};"
    query_list = []
    try:
        cursor.execute(sql, vals)  # 执行SQL语句
        query_list = cursor.fetchall()  # 获取查询结果, 没查到返回空列表
        db.commit()  # 提交到数据库
    except Exception as e:
        log.warn(f"表查询异常: {sql} -----原因: {e}")
        db.rollback()  # 数据库回滚
    print(f"表查询结果: {query_list}")
    return query_list


def sql_table_update(sql: str, args=tuple()):
    num = 0
    try:
        num = cursor.execute(sql, args)  # 执行SQL语句
        db.commit()
    except Exception as e:
        log.warn(f"表更新异常: {sql} -----原因: {e}")
        db.rollback()
    log.info(f"表更新数量: {num}")
    return num

def sql_table_update_ex(table_name: str, update_dict: dict, condition_dict={}):
    update_fields = update_dict.keys()
    update = [f"{field}=%s" for field in update_fields]
    update = ", ".join(update)

    condition_fields = condition_dict.keys()
    condition = [f"{field}=%s" for field in condition_fields]
    condition = " and ".join(condition)

    update_vals = tuple(update_dict.values())
    condition_vals = tuple(condition_dict.values())

    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"update {table_name} set {update} where {condition};"
    else:
        sql = f"update {table_name} set {update};"
    num = 0
    try:
        num = cursor.execute(sql, update_vals+condition_vals)
        db.commit()
    except Exception as e:
        log.warn(f"表更新异常: {sql} -----原因: {e}")
        db.rollback()
    log.info(f"表更新数量: {num}")
    return num


def sql_table_del(sql: str, args=tuple()):
    num = 0
    try:
        num = cursor.execute(sql, args)  # 执行SQL语句
        db.commit()
    except Exception as e:
        log.warn(f"表删除异常: {sql} -----原因: {e}")
        db.rollback()
    log.info(f"表删除数量: {num}")
    return num


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


# 剪切板拷贝
def clip_copy(content: str):
    clip_bd = QApplication.clipboard()
    clip_bd.setText(content)


# 获取IP归属地
def get_ip_location(ip: str) -> str:
    appcode = "3799d32779864269b80bd92e70619498"
    url = f"https://hcapi20.market.alicloudapi.com/ip?ip={ip}"
    request = urllib.request.Request(url)
    request.add_header("Authorization", "APPCODE " + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read().decode()  # 返回json字符串
    if not content:
        return ""
    ret_dict = json.loads(content)  # json字符串 转 py字典
    if ret_dict["msg"] != "success":
        return ""
    data = ret_dict["data"]
    country, region, city, isp = data["country"], data["region"], data["city"], data["isp"]
    location = f"{country}-{region}-{city}-{isp}"
    print("location:", location)
    return location


# 路径是否存在
def path_exist(path: str):
    if os.path.exists(path):
        return True
    return False


# 创建目录, 不存在才创建
def dir_create(dir: str):
    if not path_exist(dir):
        os.makedirs(dir)


# 获取目录中的文件
def dir_get_files(dir: str):
    ret = []
    for root, dirs, files in os.walk(dir):
        ret = files
        break
    return ret


# json文件 -> py字典
def json_file_to_dict(path_cfg: str, default_cfg: dict):
    try:
        # 若文件不存在, 则用默认的配置字典先创建json文件
        if not path_exist(path_cfg):
            with open(path_cfg, "w", encoding="utf-8") as f:
                json.dump(default_cfg, f, ensure_ascii=False)
        with open(path_cfg, "r", encoding="utf-8") as f:
            cfg_load = json.load(f)
    except:
        print("json decode error!")
        cfg_load = {}
    return cfg_load


# py对象 -> json文件
def dict_to_json_file(py_dict: dict, path_cfg: str):
    try:
        with open(path_cfg, "w", encoding="utf-8") as f:
            json.dump(py_dict, f, ensure_ascii=False, sort_keys=True)
    except:
        print("json encode error!")


if __name__ == '__main__':
    log = Log()
    log.info("------------------------------------------------------------------")
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 应用程序
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    # 窗口
    wnd_server = WndServer()
    wnd_server.show()
    # 消息循环
    sys.exit(app.exec_())

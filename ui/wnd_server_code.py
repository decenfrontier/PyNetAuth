from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtWidgets import QMainWindow
import pymysql

from ui.wnd_server import Ui_WndServer
from ui import qres

class WndServer(QMainWindow, Ui_WndServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_all_controls()
        self.init_all_sig_slot()
        self.init_mysql()

    def closeEvent(self, event: QCloseEvent):
        self.crsr.close()
        self.conn.close()

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

    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/users.png"), "全部用户")
        self.tool_bar.addAction(QIcon(":/user.png"), "在线用户")
        self.tool_bar.addAction(QIcon(":/card.png"), "卡密管理")
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
        self.tbe_card_manage.setColumnWidth(card_key, 350)
        self.tbe_card_manage.setColumnWidth(state, 80)
        self.tbe_card_manage.setColumnWidth(type, 80)
        self.tbe_card_manage.setColumnWidth(gen_time, 150)
        self.tbe_card_manage.setColumnWidth(use_time, 150)


    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        if action_name == "全部用户":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "在线用户":
            self.stack_widget.setCurrentIndex(1)
        else:
            self.stack_widget.setCurrentIndex(2)




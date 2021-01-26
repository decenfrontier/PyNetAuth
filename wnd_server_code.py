import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QStyleFactory, QMainWindow
from PySide2.QtCore import Qt

from ui.wnd_server import Ui_wnd_server
from ui import qres
import mf

class WndServer(QMainWindow, Ui_wnd_server):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tool_bar.addAction(QIcon(":/users.png"), "all_user")
        self.tool_bar.addAction(QIcon(":/user.png"), "online_user")
        self.tool_bar.addAction(QIcon(":/card.png"), "card_manage")
        self.init_all_controls()
        self.init_all_sig_slot()

    def init_all_controls(self):
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
        if action_name == "all_user":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "online_user":
            self.stack_widget.setCurrentIndex(1)
        else:
            self.stack_widget.setCurrentIndex(2)


if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    wnd_server = WndServer()
    wnd_server.show()

    sys.exit(app.exec_())

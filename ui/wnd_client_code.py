from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from ui.wnd_client import Ui_WndClient
from res import qres

class WndClient(QMainWindow, Ui_WndClient):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_all_controls()
        self.init_all_sig_slot()
        self.init_tcp_client()

    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/login.png"), "登录")
        self.tool_bar.addAction(QIcon(":/register.png"), "注册")
        self.tool_bar.addAction(QIcon(":/pay.png"), "充值")
        self.tool_bar.addAction(QIcon(":/modify.png"), "改密")

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)

    def init_tcp_client(self):

        ...

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        if action_name == "登录":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "注册":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "充值":
            self.stack_widget.setCurrentIndex(2)
        else:
            self.stack_widget.setCurrentIndex(3)

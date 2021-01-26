import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QStyleFactory, QMainWindow
from PySide2.QtCore import Qt

from ui.wnd_server import Ui_wnd_server
from ui import qres

class WndServer(QMainWindow, Ui_wnd_server):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tool_bar.addAction(QIcon(":/users.png"), "all_user")
        self.tool_bar.addAction(QIcon(":/user.png"), "online_user")
        self.tool_bar.addAction(QIcon(":/card.png"), "card_manage")
        self.init_all_sig_slot()

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

    wnd_server = WndServer()
    wnd_server.show()

    sys.exit(app.exec_())

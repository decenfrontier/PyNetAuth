from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from ui.wnd_client import Ui_WndClient
from ui import qres

class WndClient(QMainWindow, Ui_WndClient):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_all_controls()

    def init_all_controls(self):
        self.stack_widget.setCurrentIndex(0)
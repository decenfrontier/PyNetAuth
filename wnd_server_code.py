from ui.wnd_server import Ui_wnd_server

import sys

from PySide2.QtWidgets import QApplication, QStyleFactory, QMessageBox
from PySide2.QtCore import *


if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()




    sys.exit(app.exec_())

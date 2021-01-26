import sys

from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt

from ui.wnd_server_code import WndServer
from ui.wnd_client_code import WndClient

import mf

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    # wnd_server = WndServer()
    # wnd_server.show()

    wnd_client = WndClient()
    wnd_client.show()

    sys.exit(app.exec_())
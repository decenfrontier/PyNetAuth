from PySide2.QtWidgets import QWidget
from ui.wnd_client_main import Ui_WndClientMain
import mf


class WndClientMain(QWidget, Ui_WndClientMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


from PySide2.QtWidgets import QApplication, QStyleFactory
from PySide2.QtCore import Qt
import sys

if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)

    wnd_client_main = WndClientMain()
    wnd_client_main.show()

    sys.exit(app.exec_())
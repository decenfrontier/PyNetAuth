# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_client_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndClientMain(object):
    def setupUi(self, WndClientMain):
        if not WndClientMain.objectName():
            WndClientMain.setObjectName(u"WndClientMain")
        WndClientMain.resize(768, 454)
        self.centralwidget = QWidget(WndClientMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 220, 114, 16))
        self.label.setScaledContents(True)
        WndClientMain.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndClientMain)
        self.status_bar.setObjectName(u"status_bar")
        WndClientMain.setStatusBar(self.status_bar)

        self.retranslateUi(WndClientMain)

        QMetaObject.connectSlotsByName(WndClientMain)
    # setupUi

    def retranslateUi(self, WndClientMain):
        WndClientMain.setWindowTitle(QCoreApplication.translate("WndClientMain", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("WndClientMain", u"\u767b\u5f55\u6210\u529f,\u7a0b\u5e8f\u4e3b\u754c\u9762", None))
    # retranslateUi


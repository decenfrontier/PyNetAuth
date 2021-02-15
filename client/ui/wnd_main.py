# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(768, 454)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 220, 114, 16))
        self.label.setScaledContents(True)
        WndMain.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndMain)
        self.status_bar.setObjectName(u"status_bar")
        WndMain.setStatusBar(self.status_bar)

        self.retranslateUi(WndMain)

        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"\u7a0b\u5e8f\u4e3b\u7a97\u53e3", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"\u767b\u5f55\u6210\u529f,\u7a0b\u5e8f\u4e3b\u754c\u9762", None))
    # retranslateUi


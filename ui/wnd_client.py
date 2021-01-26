# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_client.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndClient(object):
    def setupUi(self, WndClient):
        if not WndClient.objectName():
            WndClient.setObjectName(u"WndClient")
        WndClient.resize(341, 207)
        self.centralwidget = QWidget(WndClient)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stack_widget = QStackedWidget(self.centralwidget)
        self.stack_widget.setObjectName(u"stack_widget")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.pushButton = QPushButton(self.page_login)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 140, 75, 23))
        self.layoutWidget = QWidget(self.page_login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 80, 171, 48))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.stack_widget.addWidget(self.page_login)
        self.page_reg = QWidget()
        self.page_reg.setObjectName(u"page_reg")
        self.pushButton_2 = QPushButton(self.page_reg)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 150, 75, 23))
        self.layoutWidget1 = QWidget(self.page_reg)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 40, 195, 100))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.layoutWidget1)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 3, 1, 1, 1)

        self.stack_widget.addWidget(self.page_reg)
        self.page_pay = QWidget()
        self.page_pay.setObjectName(u"page_pay")
        self.pushButton_3 = QPushButton(self.page_pay)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(120, 120, 75, 23))
        self.layoutWidget2 = QWidget(self.page_pay)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(70, 80, 201, 22))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.layoutWidget2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_4.addWidget(self.lineEdit_9, 0, 1, 1, 1)

        self.stack_widget.addWidget(self.page_pay)
        self.page_findback = QWidget()
        self.page_findback.setObjectName(u"page_findback")
        self.pushButton_4 = QPushButton(self.page_findback)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 140, 75, 23))
        self.layoutWidget3 = QWidget(self.page_findback)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(70, 50, 183, 74))
        self.gridLayout_5 = QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.layoutWidget3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_5.addWidget(self.lineEdit_10, 0, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.layoutWidget3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_5.addWidget(self.lineEdit_12, 1, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.layoutWidget3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_5.addWidget(self.lineEdit_11, 2, 1, 1, 1)

        self.stack_widget.addWidget(self.page_findback)

        self.gridLayout.addWidget(self.stack_widget, 0, 0, 1, 1)

        WndClient.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndClient)
        self.status_bar.setObjectName(u"status_bar")
        WndClient.setStatusBar(self.status_bar)
        self.tool_bar = QToolBar(WndClient)
        self.tool_bar.setObjectName(u"tool_bar")
        self.tool_bar.setMovable(False)
        WndClient.addToolBar(Qt.LeftToolBarArea, self.tool_bar)

        self.retranslateUi(WndClient)

        self.stack_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(WndClient)
    # setupUi

    def retranslateUi(self, WndClient):
        WndClient.setWindowTitle(QCoreApplication.translate("WndClient", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("WndClient", u"\u767b \u5f55", None))
        self.label.setText(QCoreApplication.translate("WndClient", u"\u8d26\u53f7:", None))
        self.label_2.setText(QCoreApplication.translate("WndClient", u"\u5bc6\u7801:", None))
        self.pushButton_2.setText(QCoreApplication.translate("WndClient", u"\u6ce8 \u518c", None))
        self.label_5.setText(QCoreApplication.translate("WndClient", u"\u8d26\u53f7:", None))
        self.label_6.setText(QCoreApplication.translate("WndClient", u"\u5bc6\u7801:", None))
        self.label_7.setText(QCoreApplication.translate("WndClient", u"\u91cd\u590d\u5bc6\u7801:", None))
        self.label_8.setText(QCoreApplication.translate("WndClient", u"\u90ae\u7bb1:", None))
        self.pushButton_3.setText(QCoreApplication.translate("WndClient", u"\u5145 \u503c", None))
        self.label_9.setText(QCoreApplication.translate("WndClient", u"\u5145\u503c\u5361\u53f7:", None))
        self.lineEdit_9.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("WndClient", u"\u786e\u5b9a\u4fee\u6539", None))
        self.label_10.setText(QCoreApplication.translate("WndClient", u"\u8d26\u53f7:", None))
        self.label_12.setText(QCoreApplication.translate("WndClient", u"\u90ae\u7bb1:", None))
        self.label_11.setText(QCoreApplication.translate("WndClient", u"\u65b0\u5bc6\u7801:", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndClient", u"toolBar", None))
    # retranslateUi


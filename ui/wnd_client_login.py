# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_client_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndClientLogin(object):
    def setupUi(self, WndClientLogin):
        if not WndClientLogin.objectName():
            WndClientLogin.setObjectName(u"WndClientLogin")
        WndClientLogin.resize(351, 270)
        WndClientLogin.setSizeGripEnabled(False)
        WndClientLogin.setModal(False)
        self.stack_widget = QStackedWidget(WndClientLogin)
        self.stack_widget.setObjectName(u"stack_widget")
        self.stack_widget.setGeometry(QRect(0, 0, 350, 268))
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.gridLayout_13 = QGridLayout(self.page_login)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_login)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.edt_login_account = QLineEdit(self.widget)
        self.edt_login_account.setObjectName(u"edt_login_account")

        self.gridLayout_2.addWidget(self.edt_login_account, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.edt_login_pwd = QLineEdit(self.widget)
        self.edt_login_pwd.setObjectName(u"edt_login_pwd")

        self.gridLayout_2.addWidget(self.edt_login_pwd, 1, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 1, 1, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(74, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")

        self.gridLayout_6.addWidget(self.btn_login, 2, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(75, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_login)
        self.page_reg = QWidget()
        self.page_reg.setObjectName(u"page_reg")
        self.gridLayout_10 = QGridLayout(self.page_reg)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.page_reg)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.edt_reg_account = QLineEdit(self.widget_2)
        self.edt_reg_account.setObjectName(u"edt_reg_account")

        self.gridLayout_3.addWidget(self.edt_reg_account, 0, 1, 1, 1)

        self.edt_reg_qq = QLineEdit(self.widget_2)
        self.edt_reg_qq.setObjectName(u"edt_reg_qq")

        self.gridLayout_3.addWidget(self.edt_reg_qq, 2, 1, 1, 1)

        self.edt_reg_pwd = QLineEdit(self.widget_2)
        self.edt_reg_pwd.setObjectName(u"edt_reg_pwd")

        self.gridLayout_3.addWidget(self.edt_reg_pwd, 1, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 1, 1, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(62, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(53, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)

        self.btn_reg = QPushButton(self.widget_2)
        self.btn_reg.setObjectName(u"btn_reg")

        self.gridLayout_7.addWidget(self.btn_reg, 2, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(53, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 2, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 3, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_reg)
        self.page_pay = QWidget()
        self.page_pay.setObjectName(u"page_pay")
        self.gridLayout_11 = QGridLayout(self.page_pay)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_pay)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_8 = QGridLayout(self.widget_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_5 = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.lineEdit_13 = QLineEdit(self.widget_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_2.addWidget(self.lineEdit_13)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 1, 1, 1, 3)

        self.horizontalSpacer_13 = QSpacerItem(74, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.widget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout.addWidget(self.lineEdit_9)


        self.gridLayout_8.addLayout(self.verticalLayout, 2, 1, 1, 3)

        self.horizontalSpacer_14 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 2, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_8.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 3, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 4, 2, 1, 1)


        self.gridLayout_11.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_pay)
        self.page_modify = QWidget()
        self.page_modify.setObjectName(u"page_modify")
        self.gridLayout_16 = QGridLayout(self.page_modify)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.page_modify)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_7 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(69, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_5.addWidget(self.lineEdit_10, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widget_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_5.addWidget(self.lineEdit_12, 1, 1, 1, 1)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widget_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_5.addWidget(self.lineEdit_11, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 1, 1, 3)

        self.horizontalSpacer_16 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 67, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 3, 2, 1, 1)


        self.gridLayout_16.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_modify)

        self.retranslateUi(WndClientLogin)

        self.stack_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndClientLogin)
    # setupUi

    def retranslateUi(self, WndClientLogin):
        WndClientLogin.setWindowTitle(QCoreApplication.translate("WndClientLogin", u"Login", None))
#if QT_CONFIG(tooltip)
        self.stack_widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("WndClientLogin", u"\u8d26\u53f7:", None))
        self.label_2.setText(QCoreApplication.translate("WndClientLogin", u"\u5bc6\u7801:", None))
        self.btn_login.setText(QCoreApplication.translate("WndClientLogin", u"\u767b \u5f55", None))
        self.label_3.setText(QCoreApplication.translate("WndClientLogin", u"QQ:", None))
        self.label_6.setText(QCoreApplication.translate("WndClientLogin", u"\u5bc6\u7801:", None))
        self.label_5.setText(QCoreApplication.translate("WndClientLogin", u"\u8d26\u53f7:", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_account.setToolTip(QCoreApplication.translate("WndClientLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 6-12\u4f4d", None))
#endif // QT_CONFIG(tooltip)
        self.edt_reg_account.setText(QCoreApplication.translate("WndClientLogin", u"111111", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_qq.setToolTip(QCoreApplication.translate("WndClientLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 5-10\u4f4d", None))
#endif // QT_CONFIG(tooltip)
        self.edt_reg_qq.setText(QCoreApplication.translate("WndClientLogin", u"333333", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_pwd.setToolTip(QCoreApplication.translate("WndClientLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 6-12\u4f4d", None))
#endif // QT_CONFIG(tooltip)
        self.edt_reg_pwd.setText(QCoreApplication.translate("WndClientLogin", u"222222", None))
        self.btn_reg.setText(QCoreApplication.translate("WndClientLogin", u"\u6ce8 \u518c", None))
        self.label_13.setText(QCoreApplication.translate("WndClientLogin", u"\u8d26\u53f7:", None))
        self.lineEdit_13.setText("")
        self.label_9.setText(QCoreApplication.translate("WndClientLogin", u"\u5145\u503c\u5361\u53f7:", None))
        self.lineEdit_9.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("WndClientLogin", u"\u5145 \u503c", None))
        self.label_10.setText(QCoreApplication.translate("WndClientLogin", u"\u8d26\u53f7:", None))
        self.label_12.setText(QCoreApplication.translate("WndClientLogin", u"QQ:", None))
        self.label_11.setText(QCoreApplication.translate("WndClientLogin", u"\u65b0\u5bc6\u7801:", None))
        self.pushButton_4.setText(QCoreApplication.translate("WndClientLogin", u"\u6539 \u5bc6", None))
    # retranslateUi


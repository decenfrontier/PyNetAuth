# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_server.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndServer(object):
    def setupUi(self, WndServer):
        if not WndServer.objectName():
            WndServer.setObjectName(u"WndServer")
        WndServer.resize(1080, 620)
        WndServer.setStyleSheet(u"    * {\n"
"        font-size: 12px;\n"
"        font-family: \"Microsoft YaHei\";\n"
"    }\n"
"    QTableView {\n"
"        background: white;\n"
"        selection-color: #000000;\n"
"	    selection-background-color: #c4e1d2;  \n"
"        gridline-color: rgb(213, 213, 213); \n"
"        alternate-background-color: rgb(243, 246, 249);\n"
"    }\n"
"    QTableView::item:hover	{\n"
"	    background-color: #a1b1c9;\n"
"    }")
        WndServer.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QWidget(WndServer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stack_widget = QStackedWidget(self.centralwidget)
        self.stack_widget.setObjectName(u"stack_widget")
        self.page_proj = QWidget()
        self.page_proj.setObjectName(u"page_proj")
        self.verticalLayout_7 = QVBoxLayout(self.page_proj)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tbe_proj = QTableWidget(self.page_proj)
        if (self.tbe_proj.columnCount() < 6):
            self.tbe_proj.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tbe_proj.rowCount() < 20):
            self.tbe_proj.setRowCount(20)
        self.tbe_proj.setObjectName(u"tbe_proj")
        self.tbe_proj.setAlternatingRowColors(True)
        self.tbe_proj.setRowCount(20)
        self.tbe_proj.horizontalHeader().setDefaultSectionSize(90)
        self.tbe_proj.horizontalHeader().setStretchLastSection(True)
        self.tbe_proj.verticalHeader().setVisible(False)
        self.tbe_proj.verticalHeader().setMinimumSectionSize(20)
        self.tbe_proj.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_3.addWidget(self.tbe_proj)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.btn_proj_page_prev = QPushButton(self.page_proj)
        self.btn_proj_page_prev.setObjectName(u"btn_proj_page_prev")
        self.btn_proj_page_prev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_proj_page_prev)

        self.edt_proj_page_go = QLineEdit(self.page_proj)
        self.edt_proj_page_go.setObjectName(u"edt_proj_page_go")
        self.edt_proj_page_go.setMaximumSize(QSize(50, 16777215))
        self.edt_proj_page_go.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.edt_proj_page_go)

        self.btn_proj_page_next = QPushButton(self.page_proj)
        self.btn_proj_page_next.setObjectName(u"btn_proj_page_next")
        self.btn_proj_page_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_proj_page_next)

        self.btn_proj_page_go = QPushButton(self.page_proj)
        self.btn_proj_page_go.setObjectName(u"btn_proj_page_go")
        self.btn_proj_page_go.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_proj_page_go)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_5 = QGroupBox(self.page_proj)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_2 = QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.chk_proj_login = QCheckBox(self.groupBox_5)
        self.chk_proj_login.setObjectName(u"chk_proj_login")
        self.chk_proj_login.setChecked(True)

        self.horizontalLayout_6.addWidget(self.chk_proj_login)

        self.chk_proj_reg = QCheckBox(self.groupBox_5)
        self.chk_proj_reg.setObjectName(u"chk_proj_reg")
        self.chk_proj_reg.setChecked(True)

        self.horizontalLayout_6.addWidget(self.chk_proj_reg)

        self.chk_proj_unbind = QCheckBox(self.groupBox_5)
        self.chk_proj_unbind.setObjectName(u"chk_proj_unbind")
        self.chk_proj_unbind.setChecked(True)

        self.horizontalLayout_6.addWidget(self.chk_proj_unbind)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 3)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.edt_proj_client_ver = QLineEdit(self.groupBox_5)
        self.edt_proj_client_ver.setObjectName(u"edt_proj_client_ver")

        self.gridLayout_2.addWidget(self.edt_proj_client_ver, 1, 1, 1, 1)

        self.btn_proj_confirm = QPushButton(self.groupBox_5)
        self.btn_proj_confirm.setObjectName(u"btn_proj_confirm")
        self.btn_proj_confirm.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.btn_proj_confirm, 1, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.groupBox = QGroupBox(self.page_proj)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.edt_proj_url_update = QLineEdit(self.groupBox)
        self.edt_proj_url_update.setObjectName(u"edt_proj_url_update")

        self.gridLayout_3.addWidget(self.edt_proj_url_update, 0, 1, 1, 6)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.edt_proj_url_card = QLineEdit(self.groupBox)
        self.edt_proj_url_card.setObjectName(u"edt_proj_url_card")

        self.gridLayout_3.addWidget(self.edt_proj_url_card, 1, 1, 1, 6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 2)

        self.edt_proj_pay_gift_day = QLineEdit(self.groupBox)
        self.edt_proj_pay_gift_day.setObjectName(u"edt_proj_pay_gift_day")

        self.gridLayout_3.addWidget(self.edt_proj_pay_gift_day, 2, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.tedt_proj_public_notice = QTextEdit(self.groupBox)
        self.tedt_proj_public_notice.setObjectName(u"tedt_proj_public_notice")

        self.gridLayout_3.addWidget(self.tedt_proj_public_notice, 3, 1, 2, 6)

        self.verticalSpacer = QSpacerItem(20, 139, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.chk_additional_gift = QCheckBox(self.groupBox)
        self.chk_additional_gift.setObjectName(u"chk_additional_gift")

        self.gridLayout_3.addWidget(self.chk_additional_gift, 2, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 6, 1, 1)

        self.edt_addtional_gift = QLineEdit(self.groupBox)
        self.edt_addtional_gift.setObjectName(u"edt_addtional_gift")

        self.gridLayout_3.addWidget(self.edt_addtional_gift, 2, 4, 1, 2)

        self.btn_cfg_read = QPushButton(self.groupBox)
        self.btn_cfg_read.setObjectName(u"btn_cfg_read")

        self.gridLayout_3.addWidget(self.btn_cfg_read, 5, 3, 1, 1)

        self.btn_cfg_save = QPushButton(self.groupBox)
        self.btn_cfg_save.setObjectName(u"btn_cfg_save")

        self.gridLayout_3.addWidget(self.btn_cfg_save, 5, 4, 1, 3)


        self.verticalLayout_6.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbe_custom = QTableWidget(self.page_proj)
        if (self.tbe_custom.columnCount() < 4):
            self.tbe_custom.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        if (self.tbe_custom.rowCount() < 10):
            self.tbe_custom.setRowCount(10)
        self.tbe_custom.setObjectName(u"tbe_custom")
        self.tbe_custom.setAlternatingRowColors(True)
        self.tbe_custom.setRowCount(10)
        self.tbe_custom.horizontalHeader().setStretchLastSection(True)
        self.tbe_custom.verticalHeader().setVisible(False)
        self.tbe_custom.verticalHeader().setCascadingSectionResizes(False)
        self.tbe_custom.verticalHeader().setMinimumSectionSize(20)
        self.tbe_custom.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout.addWidget(self.tbe_custom)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.page_proj)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 2, 0, 1, 7)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 5, 1, 1)

        self.edt_custom_eval = QLineEdit(self.groupBox_4)
        self.edt_custom_eval.setObjectName(u"edt_custom_eval")
        self.edt_custom_eval.setReadOnly(True)

        self.gridLayout_4.addWidget(self.edt_custom_eval, 1, 1, 1, 7)

        self.horizontalSpacer_9 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 0, 4, 1, 1)

        self.edt_custom_val = QLineEdit(self.groupBox_4)
        self.edt_custom_val.setObjectName(u"edt_custom_val")

        self.gridLayout_4.addWidget(self.edt_custom_val, 0, 6, 1, 2)

        self.edt_custom_key = QLineEdit(self.groupBox_4)
        self.edt_custom_key.setObjectName(u"edt_custom_key")

        self.gridLayout_4.addWidget(self.edt_custom_key, 0, 1, 1, 1)

        self.btn_custom_confirm = QPushButton(self.groupBox_4)
        self.btn_custom_confirm.setObjectName(u"btn_custom_confirm")
        self.btn_custom_confirm.setMinimumSize(QSize(120, 0))

        self.gridLayout_4.addWidget(self.btn_custom_confirm, 2, 7, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_custom_page_prev = QPushButton(self.page_proj)
        self.btn_custom_page_prev.setObjectName(u"btn_custom_page_prev")
        self.btn_custom_page_prev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_8.addWidget(self.btn_custom_page_prev)

        self.edt_custom_page_go = QLineEdit(self.page_proj)
        self.edt_custom_page_go.setObjectName(u"edt_custom_page_go")
        self.edt_custom_page_go.setMaximumSize(QSize(50, 16777215))
        self.edt_custom_page_go.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.edt_custom_page_go)

        self.btn_custom_page_next = QPushButton(self.page_proj)
        self.btn_custom_page_next.setObjectName(u"btn_custom_page_next")
        self.btn_custom_page_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_8.addWidget(self.btn_custom_page_next)

        self.btn_custom_page_go = QPushButton(self.page_proj)
        self.btn_custom_page_go.setObjectName(u"btn_custom_page_go")
        self.btn_custom_page_go.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_8.addWidget(self.btn_custom_page_go)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.stack_widget.addWidget(self.page_proj)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.verticalLayout_15 = QVBoxLayout(self.page_user)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 4, 2, 2)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_user_page_prev = QPushButton(self.page_user)
        self.btn_user_page_prev.setObjectName(u"btn_user_page_prev")
        self.btn_user_page_prev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_21.addWidget(self.btn_user_page_prev)

        self.edt_user_page_go = QLineEdit(self.page_user)
        self.edt_user_page_go.setObjectName(u"edt_user_page_go")
        self.edt_user_page_go.setMaximumSize(QSize(50, 16777215))
        self.edt_user_page_go.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.edt_user_page_go)

        self.btn_user_page_next = QPushButton(self.page_user)
        self.btn_user_page_next.setObjectName(u"btn_user_page_next")
        self.btn_user_page_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_21.addWidget(self.btn_user_page_next)

        self.btn_user_page_go = QPushButton(self.page_user)
        self.btn_user_page_go.setObjectName(u"btn_user_page_go")
        self.btn_user_page_go.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_21.addWidget(self.btn_user_page_go)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer)

        self.chk_user_order = QCheckBox(self.page_user)
        self.chk_user_order.setObjectName(u"chk_user_order")

        self.horizontalLayout_21.addWidget(self.chk_user_order)

        self.cmb_user_order_by = QComboBox(self.page_user)
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.addItem("")
        self.cmb_user_order_by.setObjectName(u"cmb_user_order_by")
        self.cmb_user_order_by.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_21.addWidget(self.cmb_user_order_by)

        self.cmb_user_order = QComboBox(self.page_user)
        self.cmb_user_order.addItem("")
        self.cmb_user_order.addItem("")
        self.cmb_user_order.setObjectName(u"cmb_user_order")

        self.horizontalLayout_21.addWidget(self.cmb_user_order)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.cmb_user_field = QComboBox(self.page_user)
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.addItem("")
        self.cmb_user_field.setObjectName(u"cmb_user_field")

        self.horizontalLayout_21.addWidget(self.cmb_user_field)

        self.cmb_user_operator = QComboBox(self.page_user)
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.setObjectName(u"cmb_user_operator")

        self.horizontalLayout_21.addWidget(self.cmb_user_operator)

        self.edt_user_value = QLineEdit(self.page_user)
        self.edt_user_value.setObjectName(u"edt_user_value")

        self.horizontalLayout_21.addWidget(self.edt_user_value)

        self.btn_user_query = QPushButton(self.page_user)
        self.btn_user_query.setObjectName(u"btn_user_query")

        self.horizontalLayout_21.addWidget(self.btn_user_query)


        self.verticalLayout_15.addLayout(self.horizontalLayout_21)

        self.tbe_user = QTableWidget(self.page_user)
        if (self.tbe_user.columnCount() < 20):
            self.tbe_user.setColumnCount(20)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(11, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(12, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(13, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(14, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(15, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(16, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(17, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(18, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(19, __qtablewidgetitem29)
        if (self.tbe_user.rowCount() < 26):
            self.tbe_user.setRowCount(26)
        self.tbe_user.setObjectName(u"tbe_user")
        self.tbe_user.setAlternatingRowColors(True)
        self.tbe_user.setTextElideMode(Qt.ElideNone)
        self.tbe_user.setShowGrid(True)
        self.tbe_user.setSortingEnabled(True)
        self.tbe_user.setWordWrap(False)
        self.tbe_user.setCornerButtonEnabled(False)
        self.tbe_user.setRowCount(26)
        self.tbe_user.horizontalHeader().setVisible(False)
        self.tbe_user.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbe_user.horizontalHeader().setStretchLastSection(True)
        self.tbe_user.verticalHeader().setVisible(False)
        self.tbe_user.verticalHeader().setMinimumSectionSize(20)
        self.tbe_user.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_15.addWidget(self.tbe_user)

        self.stack_widget.addWidget(self.page_user)
        self.page_card = QWidget()
        self.page_card.setObjectName(u"page_card")
        self.horizontalLayout_3 = QHBoxLayout(self.page_card)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.tbe_card = QTableWidget(self.page_card)
        if (self.tbe_card.columnCount() < 6):
            self.tbe_card.setColumnCount(6)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        if (self.tbe_card.rowCount() < 28):
            self.tbe_card.setRowCount(28)
        self.tbe_card.setObjectName(u"tbe_card")
        self.tbe_card.setAlternatingRowColors(True)
        self.tbe_card.setTextElideMode(Qt.ElideNone)
        self.tbe_card.setShowGrid(True)
        self.tbe_card.setSortingEnabled(True)
        self.tbe_card.setWordWrap(False)
        self.tbe_card.setCornerButtonEnabled(False)
        self.tbe_card.setRowCount(28)
        self.tbe_card.horizontalHeader().setVisible(False)
        self.tbe_card.horizontalHeader().setDefaultSectionSize(100)
        self.tbe_card.horizontalHeader().setStretchLastSection(True)
        self.tbe_card.verticalHeader().setVisible(False)
        self.tbe_card.verticalHeader().setMinimumSectionSize(20)
        self.tbe_card.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_3.addWidget(self.tbe_card)

        self.groupBox_3 = QGroupBox(self.page_card)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(220, 0))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cmb_card_type = QComboBox(self.groupBox_3)
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.setObjectName(u"cmb_card_type")

        self.gridLayout_6.addWidget(self.cmb_card_type, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.edt_card_num = QLineEdit(self.groupBox_3)
        self.edt_card_num.setObjectName(u"edt_card_num")
        self.edt_card_num.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.edt_card_num, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.btn_card_gen = QPushButton(self.groupBox_3)
        self.btn_card_gen.setObjectName(u"btn_card_gen")

        self.gridLayout_6.addWidget(self.btn_card_gen, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.pedt_card_export = QPlainTextEdit(self.groupBox_3)
        self.pedt_card_export.setObjectName(u"pedt_card_export")
        self.pedt_card_export.setMinimumSize(QSize(0, 0))
        self.pedt_card_export.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_4.addWidget(self.pedt_card_export)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_card_page_prev = QPushButton(self.groupBox_3)
        self.btn_card_page_prev.setObjectName(u"btn_card_page_prev")
        self.btn_card_page_prev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_10.addWidget(self.btn_card_page_prev)

        self.edt_card_page_go = QLineEdit(self.groupBox_3)
        self.edt_card_page_go.setObjectName(u"edt_card_page_go")
        self.edt_card_page_go.setMaximumSize(QSize(50, 16777215))
        self.edt_card_page_go.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.edt_card_page_go)

        self.btn_card_page_next = QPushButton(self.groupBox_3)
        self.btn_card_page_next.setObjectName(u"btn_card_page_next")
        self.btn_card_page_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_10.addWidget(self.btn_card_page_next)

        self.btn_card_page_go = QPushButton(self.groupBox_3)
        self.btn_card_page_go.setObjectName(u"btn_card_page_go")
        self.btn_card_page_go.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_10.addWidget(self.btn_card_page_go)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.stack_widget.addWidget(self.page_card)
        self.page_flow = QWidget()
        self.page_flow.setObjectName(u"page_flow")
        self.verticalLayout_8 = QVBoxLayout(self.page_flow)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 4, 2, 2)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_flow_page_prev = QPushButton(self.page_flow)
        self.btn_flow_page_prev.setObjectName(u"btn_flow_page_prev")
        self.btn_flow_page_prev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_11.addWidget(self.btn_flow_page_prev)

        self.edt_flow_page_go = QLineEdit(self.page_flow)
        self.edt_flow_page_go.setObjectName(u"edt_flow_page_go")
        self.edt_flow_page_go.setMaximumSize(QSize(50, 16777215))
        self.edt_flow_page_go.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.edt_flow_page_go)

        self.btn_flow_page_next = QPushButton(self.page_flow)
        self.btn_flow_page_next.setObjectName(u"btn_flow_page_next")
        self.btn_flow_page_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_11.addWidget(self.btn_flow_page_next)

        self.btn_flow_page_go = QPushButton(self.page_flow)
        self.btn_flow_page_go.setObjectName(u"btn_flow_page_go")
        self.btn_flow_page_go.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_11.addWidget(self.btn_flow_page_go)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.tbe_flow = QTableWidget(self.page_flow)
        if (self.tbe_flow.columnCount() < 10):
            self.tbe_flow.setColumnCount(10)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(6, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(7, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(8, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tbe_flow.setHorizontalHeaderItem(9, __qtablewidgetitem45)
        if (self.tbe_flow.rowCount() < 26):
            self.tbe_flow.setRowCount(26)
        self.tbe_flow.setObjectName(u"tbe_flow")
        self.tbe_flow.setAlternatingRowColors(True)
        self.tbe_flow.setRowCount(26)
        self.tbe_flow.horizontalHeader().setStretchLastSection(True)
        self.tbe_flow.verticalHeader().setVisible(False)
        self.tbe_flow.verticalHeader().setMinimumSectionSize(20)
        self.tbe_flow.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_8.addWidget(self.tbe_flow)

        self.stack_widget.addWidget(self.page_flow)
        self.page_ip = QWidget()
        self.page_ip.setObjectName(u"page_ip")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_ip.sizePolicy().hasHeightForWidth())
        self.page_ip.setSizePolicy(sizePolicy)
        self.page_ip.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.page_ip)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 6, 2)
        self.tbe_ip = QTableWidget(self.page_ip)
        if (self.tbe_ip.columnCount() < 6):
            self.tbe_ip.setColumnCount(6)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tbe_ip.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tbe_ip.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tbe_ip.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tbe_ip.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tbe_ip.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tbe_ip.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        if (self.tbe_ip.rowCount() < 30):
            self.tbe_ip.setRowCount(30)
        self.tbe_ip.setObjectName(u"tbe_ip")
        self.tbe_ip.setAlternatingRowColors(True)
        self.tbe_ip.setSortingEnabled(True)
        self.tbe_ip.setRowCount(30)
        self.tbe_ip.horizontalHeader().setStretchLastSection(True)
        self.tbe_ip.verticalHeader().setVisible(False)
        self.tbe_ip.verticalHeader().setMinimumSectionSize(20)
        self.tbe_ip.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_14.addWidget(self.tbe_ip)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_14 = QLabel(self.page_ip)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_14)

        self.lst_log = QListWidget(self.page_ip)
        self.lst_log.setObjectName(u"lst_log")
        self.lst_log.setMinimumSize(QSize(0, 400))

        self.verticalLayout.addWidget(self.lst_log)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_ip_page_prev = QPushButton(self.page_ip)
        self.btn_ip_page_prev.setObjectName(u"btn_ip_page_prev")
        self.btn_ip_page_prev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.btn_ip_page_prev)

        self.edt_ip_page_go = QLineEdit(self.page_ip)
        self.edt_ip_page_go.setObjectName(u"edt_ip_page_go")
        self.edt_ip_page_go.setMaximumSize(QSize(50, 16777215))
        self.edt_ip_page_go.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.edt_ip_page_go)

        self.btn_ip_page_next = QPushButton(self.page_ip)
        self.btn_ip_page_next.setObjectName(u"btn_ip_page_next")
        self.btn_ip_page_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.btn_ip_page_next)

        self.btn_ip_page_go = QPushButton(self.page_ip)
        self.btn_ip_page_go.setObjectName(u"btn_ip_page_go")
        self.btn_ip_page_go.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.btn_ip_page_go)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_2 = QSpacerItem(20, 91, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 1)
        self.stack_widget.addWidget(self.page_ip)

        self.gridLayout.addWidget(self.stack_widget, 0, 0, 1, 1)

        WndServer.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndServer)
        self.status_bar.setObjectName(u"status_bar")
        WndServer.setStatusBar(self.status_bar)
        self.tool_bar = QToolBar(WndServer)
        self.tool_bar.setObjectName(u"tool_bar")
        self.tool_bar.setMovable(False)
        self.tool_bar.setOrientation(Qt.Vertical)
        WndServer.addToolBar(Qt.LeftToolBarArea, self.tool_bar)

        self.retranslateUi(WndServer)

        self.stack_widget.setCurrentIndex(1)
        self.cmb_user_order_by.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndServer)
    # setupUi

    def retranslateUi(self, WndServer):
        WndServer.setWindowTitle(QCoreApplication.translate("WndServer", u"YZ\u7f51\u7edc\u9a8c\u8bc1-\u670d\u52a1\u7aef", None))
        ___qtablewidgetitem = self.tbe_proj.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem1 = self.tbe_proj.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u7248\u672c", None));
        ___qtablewidgetitem2 = self.tbe_proj.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u767b\u5f55", None));
        ___qtablewidgetitem3 = self.tbe_proj.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u6ce8\u518c", None));
        ___qtablewidgetitem4 = self.tbe_proj.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u89e3\u7ed1", None));
        ___qtablewidgetitem5 = self.tbe_proj.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndServer", u"\u6700\u540e\u66f4\u65b0\u65f6\u95f4", None));
        self.btn_proj_page_prev.setText(QCoreApplication.translate("WndServer", u"<", None))
        self.edt_proj_page_go.setText(QCoreApplication.translate("WndServer", u"0", None))
        self.btn_proj_page_next.setText(QCoreApplication.translate("WndServer", u">", None))
        self.btn_proj_page_go.setText(QCoreApplication.translate("WndServer", u"Go", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("WndServer", u"\u7248\u672c\u7ba1\u7406", None))
        self.chk_proj_login.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u767b\u5f55", None))
        self.chk_proj_reg.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u6ce8\u518c", None))
        self.chk_proj_unbind.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u89e3\u7ed1", None))
        self.label.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u7248\u672c", None))
        self.btn_proj_confirm.setText(QCoreApplication.translate("WndServer", u"\u786e\u5b9a\u6dfb\u52a0\u6216\u4fee\u6539", None))
        self.groupBox.setTitle(QCoreApplication.translate("WndServer", u"\u9879\u76ee\u7ba1\u7406", None))
        self.label_5.setText(QCoreApplication.translate("WndServer", u"\u66f4\u65b0\u7f51\u5740", None))
        self.label_6.setText(QCoreApplication.translate("WndServer", u"\u53d1\u5361\u7f51\u5740", None))
        self.label_7.setText(QCoreApplication.translate("WndServer", u"\u5145\u503c\u8d60\u9001\u5929\u6570", None))
        self.label_3.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u516c\u544a", None))
        self.chk_additional_gift.setText(QCoreApplication.translate("WndServer", u"\u989d\u5916\u8d60\u9001 \u7d2f\u8ba1\u5145\u503c\u6708\u6570 * ", None))
        self.label_11.setText(QCoreApplication.translate("WndServer", u"\u5929 ", None))
        self.btn_cfg_read.setText(QCoreApplication.translate("WndServer", u"\u8bfb\u53d6\u914d\u7f6e", None))
        self.btn_cfg_save.setText(QCoreApplication.translate("WndServer", u"\u4fdd\u5b58\u914d\u7f6e", None))
        ___qtablewidgetitem6 = self.tbe_custom.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem7 = self.tbe_custom.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndServer", u"\u952e", None));
        ___qtablewidgetitem8 = self.tbe_custom.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndServer", u"\u503c", None));
        ___qtablewidgetitem9 = self.tbe_custom.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndServer", u"\u52a0\u5bc6\u503c", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("WndServer", u"\u81ea\u5b9a\u4e49\u6570\u636e", None))
        self.label_13.setText(QCoreApplication.translate("WndServer", u"\u5bc6", None))
        self.label_8.setText(QCoreApplication.translate("WndServer", u"\u952e", None))
        self.label_9.setText(QCoreApplication.translate("WndServer", u"\u503c", None))
        self.btn_custom_confirm.setText(QCoreApplication.translate("WndServer", u"\u786e\u8ba4\u6dfb\u52a0\u6216\u4fee\u6539", None))
        self.btn_custom_page_prev.setText(QCoreApplication.translate("WndServer", u"<", None))
        self.edt_custom_page_go.setText(QCoreApplication.translate("WndServer", u"0", None))
        self.btn_custom_page_next.setText(QCoreApplication.translate("WndServer", u">", None))
        self.btn_custom_page_go.setText(QCoreApplication.translate("WndServer", u"Go", None))
        self.btn_user_page_prev.setText(QCoreApplication.translate("WndServer", u"<", None))
        self.edt_user_page_go.setText(QCoreApplication.translate("WndServer", u"0", None))
        self.btn_user_page_next.setText(QCoreApplication.translate("WndServer", u">", None))
        self.btn_user_page_go.setText(QCoreApplication.translate("WndServer", u"Go", None))
        self.chk_user_order.setText(QCoreApplication.translate("WndServer", u"\u6392\u5e8f", None))
        self.cmb_user_order_by.setItemText(0, QCoreApplication.translate("WndServer", u"\u5230\u671f\u65f6\u95f4", None))
        self.cmb_user_order_by.setItemText(1, QCoreApplication.translate("WndServer", u"\u5fc3\u8df3\u65f6\u95f4", None))
        self.cmb_user_order_by.setItemText(2, QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u7248\u672c", None))
        self.cmb_user_order_by.setItemText(3, QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u767b\u5f55\u6b21\u6570", None))
        self.cmb_user_order_by.setItemText(4, QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u89e3\u7ed1\u6b21\u6570", None))
        self.cmb_user_order_by.setItemText(5, QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u65f6\u95f4", None))
        self.cmb_user_order_by.setItemText(6, QCoreApplication.translate("WndServer", u"\u7d2f\u8ba1\u5145\u503c\u6708\u6570", None))
        self.cmb_user_order_by.setItemText(7, QCoreApplication.translate("WndServer", u"ID", None))

        self.cmb_user_order.setItemText(0, QCoreApplication.translate("WndServer", u"\u964d\u5e8f", None))
        self.cmb_user_order.setItemText(1, QCoreApplication.translate("WndServer", u"\u5347\u5e8f", None))

        self.cmb_user_field.setItemText(0, QCoreApplication.translate("WndServer", u"\u8d26\u53f7", None))
        self.cmb_user_field.setItemText(1, QCoreApplication.translate("WndServer", u"\u5bc6\u7801", None))
        self.cmb_user_field.setItemText(2, QCoreApplication.translate("WndServer", u"QQ", None))
        self.cmb_user_field.setItemText(3, QCoreApplication.translate("WndServer", u"\u72b6\u6001", None))
        self.cmb_user_field.setItemText(4, QCoreApplication.translate("WndServer", u"\u5230\u671f\u65f6\u95f4", None))
        self.cmb_user_field.setItemText(5, QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4", None))
        self.cmb_user_field.setItemText(6, QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55IP", None))
        self.cmb_user_field.setItemText(7, QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u7248\u672c", None))
        self.cmb_user_field.setItemText(8, QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u767b\u5f55\u6b21\u6570", None))
        self.cmb_user_field.setItemText(9, QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u89e3\u7ed1\u6b21\u6570", None))
        self.cmb_user_field.setItemText(10, QCoreApplication.translate("WndServer", u"\u7d2f\u8ba1\u5145\u503c\u6708\u6570", None))
        self.cmb_user_field.setItemText(11, QCoreApplication.translate("WndServer", u"\u673a\u5668\u7801", None))
        self.cmb_user_field.setItemText(12, QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u65f6\u95f4", None))
        self.cmb_user_field.setItemText(13, QCoreApplication.translate("WndServer", u"\u5907\u6ce8", None))

        self.cmb_user_operator.setItemText(0, QCoreApplication.translate("WndServer", u"=", None))
        self.cmb_user_operator.setItemText(1, QCoreApplication.translate("WndServer", u"!=", None))
        self.cmb_user_operator.setItemText(2, QCoreApplication.translate("WndServer", u">", None))
        self.cmb_user_operator.setItemText(3, QCoreApplication.translate("WndServer", u"<", None))
        self.cmb_user_operator.setItemText(4, QCoreApplication.translate("WndServer", u"like", None))
        self.cmb_user_operator.setItemText(5, QCoreApplication.translate("WndServer", u"rlike", None))

        self.btn_user_query.setText(QCoreApplication.translate("WndServer", u"\u67e5 \u8be2", None))
        ___qtablewidgetitem10 = self.tbe_user.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem11 = self.tbe_user.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndServer", u"\u8d26\u53f7", None));
        ___qtablewidgetitem12 = self.tbe_user.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndServer", u"\u5907\u6ce8", None));
        ___qtablewidgetitem13 = self.tbe_user.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndServer", u"\u5bc6\u7801", None));
        ___qtablewidgetitem14 = self.tbe_user.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndServer", u"QQ", None));
        ___qtablewidgetitem15 = self.tbe_user.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndServer", u"\u72b6\u6001", None));
        ___qtablewidgetitem16 = self.tbe_user.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndServer", u"\u5230\u671f\u65f6\u95f4", None));
        ___qtablewidgetitem17 = self.tbe_user.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndServer", u"\u5fc3\u8df3\u65f6\u95f4", None));
        ___qtablewidgetitem18 = self.tbe_user.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4", None));
        ___qtablewidgetitem19 = self.tbe_user.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55IP", None));
        ___qtablewidgetitem20 = self.tbe_user.horizontalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u5730", None));
        ___qtablewidgetitem21 = self.tbe_user.horizontalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u7248\u672c", None));
        ___qtablewidgetitem22 = self.tbe_user.horizontalHeaderItem(12)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u767b\u5f55\u6b21\u6570", None));
        ___qtablewidgetitem23 = self.tbe_user.horizontalHeaderItem(13)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u89e3\u7ed1\u6b21\u6570", None));
        ___qtablewidgetitem24 = self.tbe_user.horizontalHeaderItem(14)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("WndServer", u"\u673a\u5668\u7801", None));
        ___qtablewidgetitem25 = self.tbe_user.horizontalHeaderItem(15)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u65f6\u95f4", None));
        ___qtablewidgetitem26 = self.tbe_user.horizontalHeaderItem(16)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("WndServer", u"\u7d2f\u8ba1\u5145\u503c\u6708\u6570", None));
        ___qtablewidgetitem27 = self.tbe_user.horizontalHeaderItem(17)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("WndServer", u"\u64cd\u4f5c\u7cfb\u7edf", None));
        ___qtablewidgetitem28 = self.tbe_user.horizontalHeaderItem(18)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("WndServer", u"\u7528\u6237\u884c\u4e3a", None));
        ___qtablewidgetitem29 = self.tbe_user.horizontalHeaderItem(19)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("WndServer", u"\u6700\u540e\u66f4\u65b0\u65f6\u95f4", None));
        ___qtablewidgetitem30 = self.tbe_card.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem31 = self.tbe_card.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("WndServer", u"\u5361\u53f7", None));
        ___qtablewidgetitem32 = self.tbe_card.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("WndServer", u"\u5361\u7c7b\u578b", None));
        ___qtablewidgetitem33 = self.tbe_card.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("WndServer", u"\u5236\u5361\u65f6\u95f4", None));
        ___qtablewidgetitem34 = self.tbe_card.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("WndServer", u"\u5bfc\u51fa\u65f6\u95f4", None));
        ___qtablewidgetitem35 = self.tbe_card.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("WndServer", u"\u4f7f\u7528\u65f6\u95f4", None));
        self.groupBox_3.setTitle("")
        self.cmb_card_type.setItemText(0, QCoreApplication.translate("WndServer", u"\u5929\u5361", None))
        self.cmb_card_type.setItemText(1, QCoreApplication.translate("WndServer", u"\u5468\u5361", None))
        self.cmb_card_type.setItemText(2, QCoreApplication.translate("WndServer", u"\u6708\u5361", None))
        self.cmb_card_type.setItemText(3, QCoreApplication.translate("WndServer", u"\u5b63\u5361", None))

        self.label_2.setText(QCoreApplication.translate("WndServer", u"\u751f\u6210\u5f20\u6570:", None))
        self.edt_card_num.setInputMask("")
        self.edt_card_num.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("WndServer", u"\u5361\u5bc6\u7c7b\u578b:", None))
        self.btn_card_gen.setText(QCoreApplication.translate("WndServer", u"\u786e\u5b9a\u751f\u6210", None))
        self.label_10.setText(QCoreApplication.translate("WndServer", u"\u5bfc\u51fa\u7684\u5361\u53f7:", None))
        self.btn_card_page_prev.setText(QCoreApplication.translate("WndServer", u"<", None))
        self.edt_card_page_go.setText(QCoreApplication.translate("WndServer", u"0", None))
        self.btn_card_page_next.setText(QCoreApplication.translate("WndServer", u">", None))
        self.btn_card_page_go.setText(QCoreApplication.translate("WndServer", u"Go", None))
        self.btn_flow_page_prev.setText(QCoreApplication.translate("WndServer", u"<", None))
        self.edt_flow_page_go.setText(QCoreApplication.translate("WndServer", u"0", None))
        self.btn_flow_page_next.setText(QCoreApplication.translate("WndServer", u">", None))
        self.btn_flow_page_go.setText(QCoreApplication.translate("WndServer", u"Go", None))
        ___qtablewidgetitem36 = self.tbe_flow.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem37 = self.tbe_flow.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("WndServer", u"\u65e5\u671f", None));
        ___qtablewidgetitem38 = self.tbe_flow.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("WndServer", u"\u5929\u5361\u5145\u503c\u6570", None));
        ___qtablewidgetitem39 = self.tbe_flow.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("WndServer", u"\u5468\u5361\u5145\u503c\u6570", None));
        ___qtablewidgetitem40 = self.tbe_flow.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("WndServer", u"\u6708\u5361\u5145\u503c\u6570", None));
        ___qtablewidgetitem41 = self.tbe_flow.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("WndServer", u"\u5b63\u5361\u5145\u503c\u6570", None));
        ___qtablewidgetitem42 = self.tbe_flow.horizontalHeaderItem(6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("WndServer", u"\u5145\u503c\u7528\u6237\u6570", None));
        ___qtablewidgetitem43 = self.tbe_flow.horizontalHeaderItem(7)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("WndServer", u"\u6d3b\u8dc3\u7528\u6237\u6570", None));
        ___qtablewidgetitem44 = self.tbe_flow.horizontalHeaderItem(8)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("WndServer", u"\u5728\u7ebf\u7528\u6237\u6570", None));
        ___qtablewidgetitem45 = self.tbe_flow.horizontalHeaderItem(9)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("WndServer", u"\u6700\u540e\u66f4\u65b0\u65f6\u95f4", None));
        ___qtablewidgetitem46 = self.tbe_ip.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem47 = self.tbe_ip.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("WndServer", u"IP\u5730\u5740", None));
        ___qtablewidgetitem48 = self.tbe_ip.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("WndServer", u"\u5f52\u5c5e\u5730", None));
        ___qtablewidgetitem49 = self.tbe_ip.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u8fde\u63a5\u65f6\u95f4", None));
        ___qtablewidgetitem50 = self.tbe_ip.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u8fde\u63a5\u6b21\u6570", None));
        ___qtablewidgetitem51 = self.tbe_ip.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("WndServer", u"\u6700\u540e\u66f4\u65b0\u65f6\u95f4", None));
        self.label_14.setText(QCoreApplication.translate("WndServer", u"\u65e5\u5fd7\u5217\u8868", None))
        self.btn_ip_page_prev.setText(QCoreApplication.translate("WndServer", u"<", None))
        self.edt_ip_page_go.setText(QCoreApplication.translate("WndServer", u"0", None))
        self.btn_ip_page_next.setText(QCoreApplication.translate("WndServer", u">", None))
        self.btn_ip_page_go.setText(QCoreApplication.translate("WndServer", u"Go", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndServer", u"toolBar", None))
    # retranslateUi


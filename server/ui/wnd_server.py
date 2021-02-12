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
        WndServer.resize(1097, 633)
        WndServer.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QWidget(WndServer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stack_widget = QStackedWidget(self.centralwidget)
        self.stack_widget.setObjectName(u"stack_widget")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.verticalLayout_2 = QVBoxLayout(self.page_0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbe_proj = QTableWidget(self.page_0)
        if (self.tbe_proj.columnCount() < 12):
            self.tbe_proj.setColumnCount(12)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_proj.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tbe_proj.setObjectName(u"tbe_proj")
        self.tbe_proj.horizontalHeader().setDefaultSectionSize(90)
        self.tbe_proj.horizontalHeader().setStretchLastSection(True)
        self.tbe_proj.verticalHeader().setVisible(False)
        self.tbe_proj.verticalHeader().setMinimumSectionSize(20)
        self.tbe_proj.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout.addWidget(self.tbe_proj)

        self.groupBox = QGroupBox(self.page_0)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edt_proj_client_ver = QLineEdit(self.groupBox)
        self.edt_proj_client_ver.setObjectName(u"edt_proj_client_ver")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edt_proj_client_ver)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.pedt_proj_public_notice = QPlainTextEdit(self.groupBox)
        self.pedt_proj_public_notice.setObjectName(u"pedt_proj_public_notice")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pedt_proj_public_notice)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.edt_proj_url_update = QLineEdit(self.groupBox)
        self.edt_proj_url_update.setObjectName(u"edt_proj_url_update")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edt_proj_url_update)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.edt_proj_url_card = QLineEdit(self.groupBox)
        self.edt_proj_url_card.setObjectName(u"edt_proj_url_card")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edt_proj_url_card)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.edt_proj_reg_gift_day = QLineEdit(self.groupBox)
        self.edt_proj_reg_gift_day.setObjectName(u"edt_proj_reg_gift_day")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.edt_proj_reg_gift_day)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_11)

        self.edt_proj_free_unbind_count = QLineEdit(self.groupBox)
        self.edt_proj_free_unbind_count.setObjectName(u"edt_proj_free_unbind_count")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.edt_proj_free_unbind_count)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_12)

        self.edt_proj_unbind_sub_hour = QLineEdit(self.groupBox)
        self.edt_proj_unbind_sub_hour.setObjectName(u"edt_proj_unbind_sub_hour")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.edt_proj_unbind_sub_hour)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.chk_proj_login = QCheckBox(self.groupBox)
        self.chk_proj_login.setObjectName(u"chk_proj_login")
        self.chk_proj_login.setChecked(True)

        self.horizontalLayout_6.addWidget(self.chk_proj_login)

        self.chk_proj_reg = QCheckBox(self.groupBox)
        self.chk_proj_reg.setObjectName(u"chk_proj_reg")
        self.chk_proj_reg.setChecked(True)

        self.horizontalLayout_6.addWidget(self.chk_proj_reg)

        self.chk_proj_unbind = QCheckBox(self.groupBox)
        self.chk_proj_unbind.setObjectName(u"chk_proj_unbind")
        self.chk_proj_unbind.setChecked(True)

        self.horizontalLayout_6.addWidget(self.chk_proj_unbind)


        self.formLayout.setLayout(7, QFormLayout.SpanningRole, self.horizontalLayout_6)

        self.btn_proj_confirm = QPushButton(self.groupBox)
        self.btn_proj_confirm.setObjectName(u"btn_proj_confirm")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.btn_proj_confirm)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tbe_custom = QTableWidget(self.page_0)
        if (self.tbe_custom.columnCount() < 4):
            self.tbe_custom.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_custom.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.tbe_custom.setObjectName(u"tbe_custom")
        self.tbe_custom.horizontalHeader().setStretchLastSection(True)
        self.tbe_custom.verticalHeader().setVisible(False)
        self.tbe_custom.verticalHeader().setCascadingSectionResizes(False)
        self.tbe_custom.verticalHeader().setMinimumSectionSize(20)
        self.tbe_custom.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_4.addWidget(self.tbe_custom)

        self.groupBox_4 = QGroupBox(self.page_0)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.edt_custom_key = QLineEdit(self.groupBox_4)
        self.edt_custom_key.setObjectName(u"edt_custom_key")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.edt_custom_key)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.edt_custom_val = QLineEdit(self.groupBox_4)
        self.edt_custom_val.setObjectName(u"edt_custom_val")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.edt_custom_val)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_13)

        self.edt_custom_eval = QLineEdit(self.groupBox_4)
        self.edt_custom_eval.setObjectName(u"edt_custom_eval")
        self.edt_custom_eval.setReadOnly(True)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.edt_custom_eval)

        self.btn_custom_confirm = QPushButton(self.groupBox_4)
        self.btn_custom_confirm.setObjectName(u"btn_custom_confirm")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.btn_custom_confirm)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 2)
        self.stack_widget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.page_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(220, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 32))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cmb_user_field = QComboBox(self.groupBox_2)
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

        self.horizontalLayout_2.addWidget(self.cmb_user_field)

        self.cmb_user_operator = QComboBox(self.groupBox_2)
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.addItem("")
        self.cmb_user_operator.setObjectName(u"cmb_user_operator")

        self.horizontalLayout_2.addWidget(self.cmb_user_operator)

        self.edt_user_value = QLineEdit(self.groupBox_2)
        self.edt_user_value.setObjectName(u"edt_user_value")

        self.horizontalLayout_2.addWidget(self.edt_user_value)

        self.btn_user_query = QPushButton(self.groupBox_2)
        self.btn_user_query.setObjectName(u"btn_user_query")

        self.horizontalLayout_2.addWidget(self.btn_user_query)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(648, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.tbe_user = QTableWidget(self.page_1)
        if (self.tbe_user.columnCount() < 16):
            self.tbe_user.setColumnCount(16)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(7, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(8, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(9, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(10, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(11, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(12, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(13, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(14, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(15, __qtablewidgetitem31)
        self.tbe_user.setObjectName(u"tbe_user")
        self.tbe_user.setAlternatingRowColors(True)
        self.tbe_user.setTextElideMode(Qt.ElideNone)
        self.tbe_user.setShowGrid(True)
        self.tbe_user.setWordWrap(False)
        self.tbe_user.setCornerButtonEnabled(False)
        self.tbe_user.setRowCount(0)
        self.tbe_user.horizontalHeader().setVisible(False)
        self.tbe_user.horizontalHeader().setStretchLastSection(True)
        self.tbe_user.verticalHeader().setVisible(False)
        self.tbe_user.verticalHeader().setMinimumSectionSize(20)
        self.tbe_user.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_3.addWidget(self.tbe_user)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 12)

        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbe_card = QTableWidget(self.page_2)
        if (self.tbe_card.columnCount() < 6):
            self.tbe_card.setColumnCount(6)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        self.tbe_card.setObjectName(u"tbe_card")
        self.tbe_card.setAlternatingRowColors(True)
        self.tbe_card.setTextElideMode(Qt.ElideNone)
        self.tbe_card.setShowGrid(True)
        self.tbe_card.setWordWrap(False)
        self.tbe_card.setCornerButtonEnabled(False)
        self.tbe_card.setRowCount(0)
        self.tbe_card.horizontalHeader().setVisible(False)
        self.tbe_card.horizontalHeader().setDefaultSectionSize(150)
        self.tbe_card.horizontalHeader().setStretchLastSection(True)
        self.tbe_card.verticalHeader().setVisible(False)
        self.tbe_card.verticalHeader().setMinimumSectionSize(20)
        self.tbe_card.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_3.addWidget(self.tbe_card)

        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(220, 0))
        self.layoutWidget = QWidget(self.groupBox_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 181, 101))
        self.gridLayout_6 = QGridLayout(self.layoutWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cmb_card_type = QComboBox(self.layoutWidget)
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.setObjectName(u"cmb_card_type")

        self.gridLayout_6.addWidget(self.cmb_card_type, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.edt_card_num = QLineEdit(self.layoutWidget)
        self.edt_card_num.setObjectName(u"edt_card_num")
        self.edt_card_num.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.edt_card_num, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.btn_card_gen = QPushButton(self.layoutWidget)
        self.btn_card_gen.setObjectName(u"btn_card_gen")

        self.gridLayout_6.addWidget(self.btn_card_gen, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy)
        self.page_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.tbr_log = QTextBrowser(self.page_3)
        self.tbr_log.setObjectName(u"tbr_log")

        self.verticalLayout.addWidget(self.tbr_log)

        self.stack_widget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.tbe_everyday = QTableWidget(self.page)
        if (self.tbe_everyday.columnCount() < 5):
            self.tbe_everyday.setColumnCount(5)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tbe_everyday.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tbe_everyday.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tbe_everyday.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tbe_everyday.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tbe_everyday.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        self.tbe_everyday.setObjectName(u"tbe_everyday")
        self.tbe_everyday.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tbe_everyday, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page)

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

        self.stack_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndServer)
    # setupUi

    def retranslateUi(self, WndServer):
        WndServer.setWindowTitle(QCoreApplication.translate("WndServer", u"YZ\u7f51\u7edc\u9a8c\u8bc1-\u670d\u52a1\u7aef", None))
        ___qtablewidgetitem = self.tbe_proj.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem1 = self.tbe_proj.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u7248\u672c", None));
        ___qtablewidgetitem2 = self.tbe_proj.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u516c\u544a", None));
        ___qtablewidgetitem3 = self.tbe_proj.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndServer", u"\u66f4\u65b0\u7f51\u5740", None));
        ___qtablewidgetitem4 = self.tbe_proj.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndServer", u"\u53d1\u5361\u7f51\u5740", None));
        ___qtablewidgetitem5 = self.tbe_proj.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u8d60\u9001\u5929\u6570", None));
        ___qtablewidgetitem6 = self.tbe_proj.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndServer", u"\u514d\u8d39\u89e3\u7ed1\u6b21\u6570", None));
        ___qtablewidgetitem7 = self.tbe_proj.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndServer", u"\u89e3\u7ed1\u6263\u9664\u5c0f\u65f6", None));
        ___qtablewidgetitem8 = self.tbe_proj.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u767b\u5f55", None));
        ___qtablewidgetitem9 = self.tbe_proj.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u6ce8\u518c", None));
        ___qtablewidgetitem10 = self.tbe_proj.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u89e3\u7ed1", None));
        ___qtablewidgetitem11 = self.tbe_proj.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndServer", u"\u6700\u540e\u4fee\u6539\u65f6\u95f4", None));
        self.groupBox.setTitle(QCoreApplication.translate("WndServer", u"\u9879\u76ee\u7ba1\u7406", None))
        self.label.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u7248\u672c", None))
        self.label_3.setText(QCoreApplication.translate("WndServer", u"\u5ba2\u6237\u7aef\u516c\u544a", None))
        self.label_5.setText(QCoreApplication.translate("WndServer", u"\u66f4\u65b0\u7f51\u5740", None))
        self.label_6.setText(QCoreApplication.translate("WndServer", u"\u53d1\u5361\u7f51\u5740", None))
        self.label_7.setText(QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u8d60\u9001\u5929\u6570", None))
        self.label_11.setText(QCoreApplication.translate("WndServer", u"\u514d\u8d39\u89e3\u7ed1\u6b21\u6570", None))
        self.label_12.setText(QCoreApplication.translate("WndServer", u"\u89e3\u7ed1\u6263\u9664\u5c0f\u65f6", None))
        self.chk_proj_login.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u767b\u5f55", None))
        self.chk_proj_reg.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u6ce8\u518c", None))
        self.chk_proj_unbind.setText(QCoreApplication.translate("WndServer", u"\u5141\u8bb8\u89e3\u7ed1", None))
        self.btn_proj_confirm.setText(QCoreApplication.translate("WndServer", u"\u786e\u5b9a\u6dfb\u52a0\u6216\u4fee\u6539", None))
        ___qtablewidgetitem12 = self.tbe_custom.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem13 = self.tbe_custom.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndServer", u"KEY", None));
        ___qtablewidgetitem14 = self.tbe_custom.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndServer", u"VAL", None));
        ___qtablewidgetitem15 = self.tbe_custom.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndServer", u"EVAL", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("WndServer", u"\u81ea\u5b9a\u4e49\u6570\u636e", None))
        self.label_8.setText(QCoreApplication.translate("WndServer", u"KEY", None))
        self.label_9.setText(QCoreApplication.translate("WndServer", u"VAL", None))
        self.label_13.setText(QCoreApplication.translate("WndServer", u"EVAL", None))
        self.btn_custom_confirm.setText(QCoreApplication.translate("WndServer", u"\u786e\u8ba4\u6dfb\u52a0\u6216\u4fee\u6539", None))
        self.groupBox_2.setTitle("")
        self.cmb_user_field.setItemText(0, QCoreApplication.translate("WndServer", u"\u8d26\u53f7", None))
        self.cmb_user_field.setItemText(1, QCoreApplication.translate("WndServer", u"\u5bc6\u7801", None))
        self.cmb_user_field.setItemText(2, QCoreApplication.translate("WndServer", u"QQ", None))
        self.cmb_user_field.setItemText(3, QCoreApplication.translate("WndServer", u"\u72b6\u6001", None))
        self.cmb_user_field.setItemText(4, QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4", None))
        self.cmb_user_field.setItemText(5, QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55IP", None))
        self.cmb_user_field.setItemText(6, QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u767b\u5f55\u6b21\u6570", None))
        self.cmb_user_field.setItemText(7, QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u89e3\u7ed1\u6b21\u6570", None))
        self.cmb_user_field.setItemText(8, QCoreApplication.translate("WndServer", u"\u673a\u5668\u7801", None))
        self.cmb_user_field.setItemText(9, QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u65f6\u95f4", None))
        self.cmb_user_field.setItemText(10, QCoreApplication.translate("WndServer", u"\u5907\u6ce8", None))

        self.cmb_user_operator.setItemText(0, QCoreApplication.translate("WndServer", u"=", None))
        self.cmb_user_operator.setItemText(1, QCoreApplication.translate("WndServer", u"!=", None))
        self.cmb_user_operator.setItemText(2, QCoreApplication.translate("WndServer", u">", None))
        self.cmb_user_operator.setItemText(3, QCoreApplication.translate("WndServer", u"<", None))
        self.cmb_user_operator.setItemText(4, QCoreApplication.translate("WndServer", u"like", None))
        self.cmb_user_operator.setItemText(5, QCoreApplication.translate("WndServer", u"rlike", None))

        self.btn_user_query.setText(QCoreApplication.translate("WndServer", u"\u67e5\u8be2", None))
        ___qtablewidgetitem16 = self.tbe_user.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem17 = self.tbe_user.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndServer", u"\u8d26\u53f7", None));
        ___qtablewidgetitem18 = self.tbe_user.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndServer", u"\u5bc6\u7801", None));
        ___qtablewidgetitem19 = self.tbe_user.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndServer", u"QQ", None));
        ___qtablewidgetitem20 = self.tbe_user.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndServer", u"\u72b6\u6001", None));
        ___qtablewidgetitem21 = self.tbe_user.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("WndServer", u"\u5fc3\u8df3\u65f6\u95f4", None));
        ___qtablewidgetitem22 = self.tbe_user.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("WndServer", u"\u5230\u671f\u65f6\u95f4", None));
        ___qtablewidgetitem23 = self.tbe_user.horizontalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4", None));
        ___qtablewidgetitem24 = self.tbe_user.horizontalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55IP", None));
        ___qtablewidgetitem25 = self.tbe_user.horizontalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u5730", None));
        ___qtablewidgetitem26 = self.tbe_user.horizontalHeaderItem(10)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u767b\u5f55\u6b21\u6570", None));
        ___qtablewidgetitem27 = self.tbe_user.horizontalHeaderItem(11)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u89e3\u7ed1\u6b21\u6570", None));
        ___qtablewidgetitem28 = self.tbe_user.horizontalHeaderItem(12)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("WndServer", u"\u673a\u5668\u7801", None));
        ___qtablewidgetitem29 = self.tbe_user.horizontalHeaderItem(13)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u65f6\u95f4", None));
        ___qtablewidgetitem30 = self.tbe_user.horizontalHeaderItem(14)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("WndServer", u"\u64cd\u4f5c\u7cfb\u7edf", None));
        ___qtablewidgetitem31 = self.tbe_user.horizontalHeaderItem(15)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("WndServer", u"\u5907\u6ce8", None));
        ___qtablewidgetitem32 = self.tbe_card.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem33 = self.tbe_card.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("WndServer", u"\u5361\u53f7", None));
        ___qtablewidgetitem34 = self.tbe_card.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("WndServer", u"\u5361\u7c7b\u578b", None));
        ___qtablewidgetitem35 = self.tbe_card.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("WndServer", u"\u5236\u5361\u65f6\u95f4", None));
        ___qtablewidgetitem36 = self.tbe_card.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("WndServer", u"\u5bfc\u51fa\u65f6\u95f4", None));
        ___qtablewidgetitem37 = self.tbe_card.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("WndServer", u"\u4f7f\u7528\u65f6\u95f4", None));
        self.groupBox_3.setTitle("")
        self.cmb_card_type.setItemText(0, QCoreApplication.translate("WndServer", u"\u5929\u5361", None))
        self.cmb_card_type.setItemText(1, QCoreApplication.translate("WndServer", u"\u5468\u5361", None))
        self.cmb_card_type.setItemText(2, QCoreApplication.translate("WndServer", u"\u6708\u5361", None))
        self.cmb_card_type.setItemText(3, QCoreApplication.translate("WndServer", u"\u5b63\u5361", None))
        self.cmb_card_type.setItemText(4, QCoreApplication.translate("WndServer", u"\u5e74\u5361", None))
        self.cmb_card_type.setItemText(5, QCoreApplication.translate("WndServer", u"\u6c38\u4e45\u5361", None))

        self.label_2.setText(QCoreApplication.translate("WndServer", u"\u751f\u6210\u5f20\u6570:", None))
        self.edt_card_num.setInputMask("")
        self.edt_card_num.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("WndServer", u"\u5361\u5bc6\u7c7b\u578b:", None))
        self.btn_card_gen.setText(QCoreApplication.translate("WndServer", u"\u786e\u5b9a\u751f\u6210", None))
        self.tbr_log.setDocumentTitle(QCoreApplication.translate("WndServer", u"\u6267\u884c\u65e5\u5fd7", None))
        ___qtablewidgetitem38 = self.tbe_everyday.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("WndServer", u"ID", None));
        ___qtablewidgetitem39 = self.tbe_everyday.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("WndServer", u"\u65e5\u671f", None));
        ___qtablewidgetitem40 = self.tbe_everyday.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("WndServer", u"\u5145\u503c\u7528\u6237\u6570", None));
        ___qtablewidgetitem41 = self.tbe_everyday.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("WndServer", u"\u6d3b\u8dc3\u7528\u6237\u6570", None));
        ___qtablewidgetitem42 = self.tbe_everyday.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("WndServer", u"\u5f53\u524d\u5728\u7ebf\u7528\u6237\u6570", None));
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndServer", u"toolBar", None))
    # retranslateUi


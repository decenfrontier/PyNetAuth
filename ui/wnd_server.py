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
        WndServer.resize(1117, 590)
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
        self.gridLayout_2 = QGridLayout(self.page_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbe_all_user = QTableWidget(self.page_0)
        if (self.tbe_all_user.columnCount() < 8):
            self.tbe_all_user.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbe_all_user.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tbe_all_user.setObjectName(u"tbe_all_user")
        self.tbe_all_user.setAlternatingRowColors(True)
        self.tbe_all_user.setTextElideMode(Qt.ElideNone)
        self.tbe_all_user.setShowGrid(True)
        self.tbe_all_user.setWordWrap(True)
        self.tbe_all_user.setCornerButtonEnabled(False)
        self.tbe_all_user.setRowCount(0)
        self.tbe_all_user.horizontalHeader().setVisible(False)
        self.tbe_all_user.horizontalHeader().setCascadingSectionResizes(False)
        self.tbe_all_user.horizontalHeader().setStretchLastSection(True)
        self.tbe_all_user.verticalHeader().setVisible(False)
        self.tbe_all_user.verticalHeader().setMinimumSectionSize(20)
        self.tbe_all_user.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout.addWidget(self.tbe_all_user)

        self.groupBox = QGroupBox(self.page_0)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(220, 0))

        self.horizontalLayout.addWidget(self.groupBox)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_3 = QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tbe_online_user = QTableWidget(self.page_1)
        if (self.tbe_online_user.columnCount() < 8):
            self.tbe_online_user.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_online_user.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tbe_online_user.setObjectName(u"tbe_online_user")
        self.tbe_online_user.setAlternatingRowColors(True)
        self.tbe_online_user.setTextElideMode(Qt.ElideNone)
        self.tbe_online_user.setShowGrid(True)
        self.tbe_online_user.setWordWrap(True)
        self.tbe_online_user.setCornerButtonEnabled(False)
        self.tbe_online_user.setRowCount(0)
        self.tbe_online_user.horizontalHeader().setVisible(False)
        self.tbe_online_user.horizontalHeader().setStretchLastSection(True)
        self.tbe_online_user.verticalHeader().setVisible(False)
        self.tbe_online_user.verticalHeader().setMinimumSectionSize(20)
        self.tbe_online_user.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_2.addWidget(self.tbe_online_user)

        self.groupBox_2 = QGroupBox(self.page_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(220, 0))

        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

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
        self.tbe_card_manage = QTableWidget(self.page_2)
        if (self.tbe_card_manage.columnCount() < 5):
            self.tbe_card_manage.setColumnCount(5)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_card_manage.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbe_card_manage.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_card_manage.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_card_manage.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_card_manage.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        self.tbe_card_manage.setObjectName(u"tbe_card_manage")
        self.tbe_card_manage.setAlternatingRowColors(True)
        self.tbe_card_manage.setTextElideMode(Qt.ElideNone)
        self.tbe_card_manage.setShowGrid(True)
        self.tbe_card_manage.setWordWrap(True)
        self.tbe_card_manage.setCornerButtonEnabled(False)
        self.tbe_card_manage.setRowCount(0)
        self.tbe_card_manage.horizontalHeader().setVisible(True)
        self.tbe_card_manage.horizontalHeader().setStretchLastSection(True)
        self.tbe_card_manage.verticalHeader().setVisible(False)
        self.tbe_card_manage.verticalHeader().setMinimumSectionSize(20)
        self.tbe_card_manage.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_3.addWidget(self.tbe_card_manage)

        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(220, 0))
        self.layoutWidget = QWidget(self.groupBox_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 181, 106))
        self.gridLayout_6 = QGridLayout(self.layoutWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.edt_card_num = QLineEdit(self.layoutWidget)
        self.edt_card_num.setObjectName(u"edt_card_num")
        self.edt_card_num.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.edt_card_num, 1, 1, 1, 1)

        self.btn_card_refresh = QPushButton(self.layoutWidget)
        self.btn_card_refresh.setObjectName(u"btn_card_refresh")

        self.gridLayout_6.addWidget(self.btn_card_refresh, 6, 0, 1, 2)

        self.cmb_card_type = QComboBox(self.layoutWidget)
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.addItem("")
        self.cmb_card_type.setObjectName(u"cmb_card_type")

        self.gridLayout_6.addWidget(self.cmb_card_type, 0, 1, 1, 1)

        self.btn_card_gen = QPushButton(self.layoutWidget)
        self.btn_card_gen.setObjectName(u"btn_card_gen")

        self.gridLayout_6.addWidget(self.btn_card_gen, 5, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tbr_log = QTextBrowser(self.page_3)
        self.tbr_log.setObjectName(u"tbr_log")

        self.gridLayout_5.addWidget(self.tbr_log, 1, 0, 1, 1)

        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stack_widget, 0, 0, 1, 1)

        WndServer.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndServer)
        self.status_bar.setObjectName(u"status_bar")
        WndServer.setStatusBar(self.status_bar)
        self.tool_bar = QToolBar(WndServer)
        self.tool_bar.setObjectName(u"tool_bar")
        self.tool_bar.setMovable(True)
        self.tool_bar.setOrientation(Qt.Vertical)
        WndServer.addToolBar(Qt.LeftToolBarArea, self.tool_bar)

        self.retranslateUi(WndServer)

        self.stack_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(WndServer)
    # setupUi

    def retranslateUi(self, WndServer):
        WndServer.setWindowTitle(QCoreApplication.translate("WndServer", u"YZ\u7f51\u7edc\u9a8c\u8bc1-\u670d\u52a1\u7aef", None))
        ___qtablewidgetitem = self.tbe_all_user.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndServer", u"account", None));
        ___qtablewidgetitem1 = self.tbe_all_user.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndServer", u"pwd", None));
        ___qtablewidgetitem2 = self.tbe_all_user.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndServer", u"qq", None));
        ___qtablewidgetitem3 = self.tbe_all_user.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndServer", u"machine_code", None));
        ___qtablewidgetitem4 = self.tbe_all_user.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndServer", u"reg_ip", None));
        ___qtablewidgetitem5 = self.tbe_all_user.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndServer", u"reg_time", None));
        ___qtablewidgetitem6 = self.tbe_all_user.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndServer", u"due_time", None));
        ___qtablewidgetitem7 = self.tbe_all_user.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndServer", u"is_forbid", None));
        self.groupBox.setTitle("")
        ___qtablewidgetitem8 = self.tbe_online_user.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndServer", u"\u8d26\u53f7", None));
        ___qtablewidgetitem9 = self.tbe_online_user.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndServer", u"hcomm", None));
        ___qtablewidgetitem10 = self.tbe_online_user.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndServer", u"connect_id", None));
        ___qtablewidgetitem11 = self.tbe_online_user.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndServer", u"machine_code", None));
        ___qtablewidgetitem12 = self.tbe_online_user.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndServer", u"login_ip", None));
        ___qtablewidgetitem13 = self.tbe_online_user.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndServer", u"login_time", None));
        ___qtablewidgetitem14 = self.tbe_online_user.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndServer", u"heart_time", None));
        ___qtablewidgetitem15 = self.tbe_online_user.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndServer", u"online_time", None));
        self.groupBox_2.setTitle("")
        ___qtablewidgetitem16 = self.tbe_card_manage.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndServer", u"\u5361\u5bc6", None));
        ___qtablewidgetitem17 = self.tbe_card_manage.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndServer", u"\u5361\u7c7b\u578b", None));
        ___qtablewidgetitem18 = self.tbe_card_manage.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndServer", u"\u72b6\u6001", None));
        ___qtablewidgetitem19 = self.tbe_card_manage.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndServer", u"\u751f\u6210\u65f6\u95f4", None));
        ___qtablewidgetitem20 = self.tbe_card_manage.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndServer", u"\u4f7f\u7528\u65f6\u95f4", None));
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("WndServer", u"\u751f\u6210\u5f20\u6570:", None))
        self.label_4.setText(QCoreApplication.translate("WndServer", u"\u5361\u5bc6\u7c7b\u578b:", None))
        self.edt_card_num.setInputMask("")
        self.edt_card_num.setPlaceholderText("")
        self.btn_card_refresh.setText(QCoreApplication.translate("WndServer", u"\u5237\u65b0\u5361\u5bc6\u5e93", None))
        self.cmb_card_type.setItemText(0, QCoreApplication.translate("WndServer", u"\u5929\u5361", None))
        self.cmb_card_type.setItemText(1, QCoreApplication.translate("WndServer", u"\u5468\u5361", None))
        self.cmb_card_type.setItemText(2, QCoreApplication.translate("WndServer", u"\u6708\u5361", None))
        self.cmb_card_type.setItemText(3, QCoreApplication.translate("WndServer", u"\u5b63\u5361", None))
        self.cmb_card_type.setItemText(4, QCoreApplication.translate("WndServer", u"\u5e74\u5361", None))
        self.cmb_card_type.setItemText(5, QCoreApplication.translate("WndServer", u"\u6c38\u4e45\u5361", None))

        self.btn_card_gen.setText(QCoreApplication.translate("WndServer", u"\u786e\u5b9a\u751f\u6210", None))
        self.label.setText(QCoreApplication.translate("WndServer", u"\u6267\u884c\u65e5\u5fd7", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndServer", u"toolBar", None))
    # retranslateUi


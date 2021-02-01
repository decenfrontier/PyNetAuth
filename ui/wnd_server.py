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
        self.tbe_proj = QTableWidget(self.page_0)
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
        self.tbe_proj.setObjectName(u"tbe_proj")
        self.tbe_proj.setAlternatingRowColors(True)
        self.tbe_proj.setTextElideMode(Qt.ElideNone)
        self.tbe_proj.setShowGrid(True)
        self.tbe_proj.setWordWrap(True)
        self.tbe_proj.setCornerButtonEnabled(False)
        self.tbe_proj.setRowCount(0)
        self.tbe_proj.horizontalHeader().setVisible(False)
        self.tbe_proj.horizontalHeader().setCascadingSectionResizes(False)
        self.tbe_proj.horizontalHeader().setStretchLastSection(True)
        self.tbe_proj.verticalHeader().setVisible(False)
        self.tbe_proj.verticalHeader().setMinimumSectionSize(20)
        self.tbe_proj.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout.addWidget(self.tbe_proj)

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
        self.tbe_user = QTableWidget(self.page_1)
        if (self.tbe_user.columnCount() < 14):
            self.tbe_user.setColumnCount(14)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_user.setHorizontalHeaderItem(13, __qtablewidgetitem19)
        self.tbe_user.setObjectName(u"tbe_user")
        self.tbe_user.setAlternatingRowColors(True)
        self.tbe_user.setTextElideMode(Qt.ElideNone)
        self.tbe_user.setShowGrid(True)
        self.tbe_user.setWordWrap(True)
        self.tbe_user.setCornerButtonEnabled(False)
        self.tbe_user.setRowCount(0)
        self.tbe_user.horizontalHeader().setVisible(False)
        self.tbe_user.horizontalHeader().setStretchLastSection(True)
        self.tbe_user.verticalHeader().setVisible(False)
        self.tbe_user.verticalHeader().setMinimumSectionSize(20)
        self.tbe_user.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_2.addWidget(self.tbe_user)

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
        self.tbe_card = QTableWidget(self.page_2)
        if (self.tbe_card.columnCount() < 5):
            self.tbe_card.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbe_card.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.tbe_card.setObjectName(u"tbe_card")
        self.tbe_card.setAlternatingRowColors(True)
        self.tbe_card.setTextElideMode(Qt.ElideNone)
        self.tbe_card.setShowGrid(True)
        self.tbe_card.setWordWrap(True)
        self.tbe_card.setCornerButtonEnabled(False)
        self.tbe_card.setRowCount(0)
        self.tbe_card.horizontalHeader().setVisible(True)
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
        ___qtablewidgetitem = self.tbe_proj.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndServer", u"\u9879\u76ee\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tbe_proj.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndServer", u"\u7248\u672c\u53f7", None));
        ___qtablewidgetitem2 = self.tbe_proj.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndServer", u"\u7ed1\u5b9a\u6a21\u5f0f", None));
        ___qtablewidgetitem3 = self.tbe_proj.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndServer", u"\u8f6f\u4ef6\u516c\u544a", None));
        ___qtablewidgetitem4 = self.tbe_proj.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndServer", u"\u66f4\u65b0\u5730\u5740", None));
        ___qtablewidgetitem5 = self.tbe_proj.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndServer", u"\u53d1\u5361\u5730\u5740", None));
        self.groupBox.setTitle("")
        ___qtablewidgetitem6 = self.tbe_user.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndServer", u"\u8d26\u53f7", None));
        ___qtablewidgetitem7 = self.tbe_user.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndServer", u"\u5bc6\u7801", None));
        ___qtablewidgetitem8 = self.tbe_user.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndServer", u"QQ", None));
        ___qtablewidgetitem9 = self.tbe_user.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndServer", u"\u72b6\u6001", None));
        ___qtablewidgetitem10 = self.tbe_user.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndServer", u"\u5fc3\u8df3\u65f6\u95f4", None));
        ___qtablewidgetitem11 = self.tbe_user.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndServer", u"\u5230\u671f\u65f6\u95f4", None));
        ___qtablewidgetitem12 = self.tbe_user.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4", None));
        ___qtablewidgetitem13 = self.tbe_user.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55IP", None));
        ___qtablewidgetitem14 = self.tbe_user.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndServer", u"\u4e0a\u6b21\u767b\u5f55\u5730", None));
        ___qtablewidgetitem15 = self.tbe_user.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u767b\u5f55\u6b21\u6570", None));
        ___qtablewidgetitem16 = self.tbe_user.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndServer", u"\u4eca\u65e5\u6362\u7ed1\u6b21\u6570", None));
        ___qtablewidgetitem17 = self.tbe_user.horizontalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndServer", u"\u673a\u5668\u7801", None));
        ___qtablewidgetitem18 = self.tbe_user.horizontalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndServer", u"\u6ce8\u518c\u65f6\u95f4", None));
        ___qtablewidgetitem19 = self.tbe_user.horizontalHeaderItem(13)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndServer", u"\u5907\u6ce8", None));
        self.groupBox_2.setTitle("")
        ___qtablewidgetitem20 = self.tbe_card.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndServer", u"\u5361\u5bc6", None));
        ___qtablewidgetitem21 = self.tbe_card.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("WndServer", u"\u5361\u7c7b\u578b", None));
        ___qtablewidgetitem22 = self.tbe_card.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("WndServer", u"\u5236\u5361\u65f6\u95f4", None));
        ___qtablewidgetitem23 = self.tbe_card.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("WndServer", u"\u4f7f\u7528\u65f6\u95f4", None));
        ___qtablewidgetitem24 = self.tbe_card.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("WndServer", u"\u9879\u76ee\u540d\u79f0", None));
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


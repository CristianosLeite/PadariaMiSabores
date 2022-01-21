# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_pagesjOZxfL.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(864, 518)
        StackedWidget.setToolTipDuration(2)
        self.actionLogo = QAction(StackedWidget)
        self.actionLogo.setObjectName(u"actionLogo")
        icon = QIcon()
        icon.addFile(u"Logo.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLogo.setIcon(icon)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.page_1.setAcceptDrops(False)
        self.gridLayout = QGridLayout(self.page_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setLineWidth(0)
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        StackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout = QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 500))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 22))

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.frame_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 22))

        self.verticalLayout_5.addWidget(self.lineEdit_3)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.frame_14)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 22))

        self.verticalLayout_9.addWidget(self.lineEdit_7)


        self.horizontalLayout_5.addWidget(self.frame_14)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.groupBox = QGroupBox(self.frame_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_7 = QFrame(self.groupBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 15))

        self.verticalLayout_6.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 22))

        self.verticalLayout_6.addWidget(self.lineEdit_4)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.groupBox)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setMaximumSize(QSize(60, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 15))
        self.label_6.setMaximumSize(QSize(30, 16777215))

        self.verticalLayout_7.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(50, 22))
        self.lineEdit_5.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_7.addWidget(self.lineEdit_5)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.groupBox)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 15))

        self.verticalLayout_8.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 22))

        self.verticalLayout_8.addWidget(self.lineEdit_6)


        self.horizontalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_2 = QGroupBox(self.frame_11)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_41 = QHBoxLayout(self.page)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")

        self.horizontalLayout_41.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")

        self.horizontalLayout_41.addLayout(self.horizontalLayout_40)

        self.stackedWidget.addWidget(self.page)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_23 = QVBoxLayout(self.page_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_24 = QFrame(self.page_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_5 = QGroupBox(self.frame_24)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(370, 0))
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_26 = QFrame(self.groupBox_5)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.frame_26)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 22))
        self.label_16.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_14.addWidget(self.label_16)

        self.lineEdit_15 = QLineEdit(self.frame_26)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 22))
        self.lineEdit_15.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_14.addWidget(self.lineEdit_15)

        self.radioButton = QRadioButton(self.frame_26)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 22))
        self.radioButton.setMaximumSize(QSize(1600000, 16777215))

        self.horizontalLayout_14.addWidget(self.radioButton)


        self.verticalLayout_19.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.groupBox_5)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.frame_27)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_15.addWidget(self.label_17)

        self.lineEdit_16 = QLineEdit(self.frame_27)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 22))
        self.lineEdit_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.lineEdit_16)

        self.label_18 = QLabel(self.frame_27)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_15.addWidget(self.label_18)

        self.lineEdit_17 = QLineEdit(self.frame_27)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_15.addWidget(self.lineEdit_17)


        self.verticalLayout_19.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.groupBox_5)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.frame_28)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_16.addWidget(self.label_19)

        self.lineEdit_18 = QLineEdit(self.frame_28)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_16.addWidget(self.lineEdit_18)


        self.verticalLayout_19.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.groupBox_5)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.frame_29)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 22))
        self.label_20.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_17.addWidget(self.label_20)

        self.comboBox = QComboBox(self.frame_29)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 22))
        self.comboBox.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.comboBox)

        self.label_21 = QLabel(self.frame_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 22))
        self.label_21.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_17.addWidget(self.label_21)

        self.comboBox_2 = QComboBox(self.frame_29)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 22))
        self.comboBox_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.comboBox_2)


        self.verticalLayout_19.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.groupBox_5)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_22 = QLabel(self.frame_30)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_18.addWidget(self.label_22)

        self.lineEdit_19 = QLineEdit(self.frame_30)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_18.addWidget(self.lineEdit_19)

        self.label_23 = QLabel(self.frame_30)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_18.addWidget(self.label_23)

        self.lineEdit_20 = QLineEdit(self.frame_30)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_18.addWidget(self.lineEdit_20)


        self.verticalLayout_19.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.groupBox_5)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_24 = QLabel(self.frame_31)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 22))
        self.label_24.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_19.addWidget(self.label_24)

        self.lineEdit_21 = QLineEdit(self.frame_31)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 22))
        self.lineEdit_21.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_19.addWidget(self.lineEdit_21)

        self.label_25 = QLabel(self.frame_31)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 22))
        self.label_25.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_19.addWidget(self.label_25)

        self.comboBox_3 = QComboBox(self.frame_31)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_19.addWidget(self.comboBox_3)


        self.verticalLayout_19.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.groupBox_5)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")

        self.verticalLayout_19.addWidget(self.frame_32)


        self.horizontalLayout_12.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_24)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_33 = QFrame(self.groupBox_6)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_26 = QLabel(self.frame_33)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_20.addWidget(self.label_26)

        self.comboBox_4 = QComboBox(self.frame_33)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 22))
        

        self.horizontalLayout_20.addWidget(self.comboBox_4)


        self.label_27 = QLabel(self.frame_33)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_20.addWidget(self.label_27)

        self.lineEdit_22 = QLineEdit(self.frame_33)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_20.addWidget(self.lineEdit_22)


        self.verticalLayout_20.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.groupBox_6)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_28 = QLabel(self.frame_34)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_21.addWidget(self.label_28)

        self.comboBox_5 = QComboBox(self.frame_34)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(120, 22))

        self.horizontalLayout_21.addWidget(self.comboBox_5)


        self.verticalLayout_20.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.groupBox_6)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_29 = QLabel(self.frame_35)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_22.addWidget(self.label_29)

        self.comboBox_6 = QComboBox(self.frame_35)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_22.addWidget(self.comboBox_6)


        self.verticalLayout_20.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.groupBox_6)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_30 = QLabel(self.frame_36)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_23.addWidget(self.label_30)

        self.comboBox_7 = QComboBox(self.frame_36)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(120, 22))

        self.horizontalLayout_23.addWidget(self.comboBox_7)


        self.verticalLayout_20.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.groupBox_6)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_31 = QLabel(self.frame_37)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_24.addWidget(self.label_31)

        self.comboBox_8 = QComboBox(self.frame_37)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_24.addWidget(self.comboBox_8)


        self.verticalLayout_20.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.groupBox_6)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_32 = QLabel(self.frame_38)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_25.addWidget(self.label_32)

        self.comboBox_9 = QComboBox(self.frame_38)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_25.addWidget(self.comboBox_9)


        self.verticalLayout_20.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.groupBox_6)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_26.addWidget(self.label_33)

        self.comboBox_10 = QComboBox(self.frame_39)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_26.addWidget(self.comboBox_10)


        self.verticalLayout_20.addWidget(self.frame_39)


        self.horizontalLayout_12.addWidget(self.groupBox_6)


        self.verticalLayout_23.addWidget(self.frame_24)

        self.groupBox_9 = QGroupBox(self.page_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_37 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.textEdit_3 = QTextEdit(self.groupBox_9)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(0, 40))
        self.textEdit_3.setMaximumSize(QSize(450, 16777215))

        self.horizontalLayout_37.addWidget(self.textEdit_3)

        self.frame_49 = QFrame(self.groupBox_9)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pushButton_11 = QPushButton(self.frame_49)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 25))
        self.pushButton_11.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_33.addWidget(self.pushButton_11)

        self.pushButton_7 = QPushButton(self.frame_49)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 25))
        self.pushButton_7.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_33.addWidget(self.pushButton_7)


        self.horizontalLayout_37.addWidget(self.frame_49)


        self.verticalLayout_23.addWidget(self.groupBox_9)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_40 = QFrame(self.page_8)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.groupBox_8 = QGroupBox(self.frame_40)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_42 = QFrame(self.groupBox_8)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_34 = QLabel(self.frame_42)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_32.addWidget(self.label_34)

        self.lineEdit_23 = QLineEdit(self.frame_42)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setToolTipDuration(0)
        self.lineEdit_23.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_23.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhNoPredictiveText|Qt.ImhNoTextHandles|Qt.ImhPreferNumbers)

        self.horizontalLayout_32.addWidget(self.lineEdit_23)

        self.label_35 = QLabel(self.frame_42)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_32.addWidget(self.label_35)

        self.lineEdit_24 = QLineEdit(self.frame_42)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.horizontalLayout_32.addWidget(self.lineEdit_24)


        self.verticalLayout_22.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.groupBox_8)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_36 = QLabel(self.frame_43)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_31.addWidget(self.label_36)

        self.lineEdit_25 = QLineEdit(self.frame_43)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.horizontalLayout_31.addWidget(self.lineEdit_25)

        self.label_37 = QLabel(self.frame_43)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_31.addWidget(self.label_37)

        self.lineEdit_26 = QLineEdit(self.frame_43)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.horizontalLayout_31.addWidget(self.lineEdit_26)


        self.verticalLayout_22.addWidget(self.frame_43)

        self.frame_45 = QFrame(self.groupBox_8)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_38 = QLabel(self.frame_45)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_30.addWidget(self.label_38)

        self.lineEdit_27 = QLineEdit(self.frame_45)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.horizontalLayout_30.addWidget(self.lineEdit_27)

        self.label_39 = QLabel(self.frame_45)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_30.addWidget(self.label_39)

        self.lineEdit_28 = QLineEdit(self.frame_45)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.horizontalLayout_30.addWidget(self.lineEdit_28)


        self.verticalLayout_22.addWidget(self.frame_45)

        self.frame_44 = QFrame(self.groupBox_8)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_40 = QLabel(self.frame_44)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_29.addWidget(self.label_40)

        self.lineEdit_29 = QLineEdit(self.frame_44)
        self.lineEdit_29.setObjectName(u"lineEdit_29")

        self.horizontalLayout_29.addWidget(self.lineEdit_29)

        self.label_41 = QLabel(self.frame_44)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_29.addWidget(self.label_41)

        self.lineEdit_30 = QLineEdit(self.frame_44)
        self.lineEdit_30.setObjectName(u"lineEdit_30")

        self.horizontalLayout_29.addWidget(self.lineEdit_30)


        self.verticalLayout_22.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.groupBox_8)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_42 = QLabel(self.frame_46)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_28.addWidget(self.label_42)

        self.lineEdit_31 = QLineEdit(self.frame_46)
        self.lineEdit_31.setObjectName(u"lineEdit_31")

        self.horizontalLayout_28.addWidget(self.lineEdit_31)

        self.label_43 = QLabel(self.frame_46)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_28.addWidget(self.label_43)

        self.lineEdit_32 = QLineEdit(self.frame_46)
        self.lineEdit_32.setObjectName(u"lineEdit_32")

        self.horizontalLayout_28.addWidget(self.lineEdit_32)


        self.verticalLayout_22.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.groupBox_8)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_44 = QLabel(self.frame_47)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_27.addWidget(self.label_44)

        self.lineEdit_33 = QLineEdit(self.frame_47)
        self.lineEdit_33.setObjectName(u"lineEdit_33")

        self.horizontalLayout_27.addWidget(self.lineEdit_33)

        self.label_45 = QLabel(self.frame_47)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_27.addWidget(self.label_45)

        self.lineEdit_34 = QLineEdit(self.frame_47)
        self.lineEdit_34.setObjectName(u"lineEdit_34")

        self.horizontalLayout_27.addWidget(self.lineEdit_34)


        self.verticalLayout_22.addWidget(self.frame_47)


        self.horizontalLayout_34.addWidget(self.groupBox_8)


        self.verticalLayout_18.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.page_8)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.groupBox_7 = QGroupBox(self.frame_41)
        self.groupBox_7.setObjectName(u"groupBox_7")

        self.horizontalLayout_35.addWidget(self.groupBox_7)

        self.frame_48 = QFrame(self.frame_41)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_8 = QPushButton(self.frame_48)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_38.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.frame_48)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_38.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_48)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_38.addWidget(self.pushButton_9)


        self.horizontalLayout_35.addWidget(self.frame_48)


        self.verticalLayout_18.addWidget(self.frame_41)

        self.stackedWidget.addWidget(self.page_8)

        self.horizontalLayout_13.addWidget(self.stackedWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_13 = QFrame(self.tab_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 200))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.frame_15)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_11.addWidget(self.lineEdit_8)


        self.verticalLayout_10.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.frame_17)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 22))

        self.verticalLayout_12.addWidget(self.lineEdit_9)


        self.horizontalLayout_7.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.frame_18)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 22))

        self.verticalLayout_13.addWidget(self.lineEdit_10)


        self.horizontalLayout_7.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_12 = QLabel(self.frame_19)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)

        self.lineEdit_11 = QLineEdit(self.frame_19)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 22))

        self.verticalLayout_14.addWidget(self.lineEdit_11)


        self.horizontalLayout_7.addWidget(self.frame_19)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.groupBox_3 = QGroupBox(self.frame_13)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_20 = QFrame(self.groupBox_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 15))

        self.verticalLayout_15.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.frame_20)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 22))

        self.verticalLayout_15.addWidget(self.lineEdit_12)


        self.horizontalLayout_8.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.groupBox_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 50))
        self.frame_21.setMaximumSize(QSize(60, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 15))
        self.label_14.setMaximumSize(QSize(30, 16777215))

        self.verticalLayout_16.addWidget(self.label_14)

        self.lineEdit_13 = QLineEdit(self.frame_21)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(50, 22))
        self.lineEdit_13.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_16.addWidget(self.lineEdit_13)


        self.horizontalLayout_8.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.groupBox_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 50))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 15))

        self.verticalLayout_17.addWidget(self.label_15)

        self.lineEdit_14 = QLineEdit(self.frame_22)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 22))

        self.verticalLayout_17.addWidget(self.lineEdit_14)


        self.horizontalLayout_8.addWidget(self.frame_22)


        self.verticalLayout_10.addWidget(self.groupBox_3)

        self.frame_23 = QFrame(self.frame_13)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_4 = QGroupBox(self.frame_23)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.textEdit_2 = QTextEdit(self.groupBox_4)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.textEdit_2)


        self.horizontalLayout_9.addWidget(self.groupBox_4)

        self.pushButton_4 = QPushButton(self.frame_23)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_23)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_23)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.pushButton_6)


        self.verticalLayout_10.addWidget(self.frame_23)


        self.horizontalLayout_11.addWidget(self.frame_13)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_27.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        StackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        StackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        StackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        StackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        StackedWidget.addWidget(self.page_6)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.actionLogo.setText(QCoreApplication.translate("StackedWidget", u"Logo", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Telefone", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"CPF / CNPJ", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"E-mail", None))
        self.groupBox.setTitle(QCoreApplication.translate("StackedWidget", u"Endere\u00e7o", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Rua", None))
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"n\u00ba", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"Bairro", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("StackedWidget", u"Obs:", None))
        self.pushButton_3.setText(QCoreApplication.translate("StackedWidget", u"Limpar", None))
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"Pesquisar", None))
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"Inserir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StackedWidget", u"Clientes", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("StackedWidget", u"B\u00e1sico", None))
        self.label_16.setText(QCoreApplication.translate("StackedWidget", u"Produto ID", None))
        self.radioButton.setText(QCoreApplication.translate("StackedWidget", u"Ativo", None))
        self.label_17.setText(QCoreApplication.translate("StackedWidget", u"Cod. Produto", None))
        self.label_18.setText(QCoreApplication.translate("StackedWidget", u"Cod. Barras", None))
        self.label_19.setText(QCoreApplication.translate("StackedWidget", u"Descri\u00e7\u00e3o", None))
        self.label_20.setText(QCoreApplication.translate("StackedWidget", u"Unidade comercial", None))
        self.label_21.setText(QCoreApplication.translate("StackedWidget", u"Unidade tribut\u00e1vel", None))
        self.label_22.setText(QCoreApplication.translate("StackedWidget", u"Marca", None))
        self.label_23.setText(QCoreApplication.translate("StackedWidget", u"Modelo", None))
        self.label_24.setText(QCoreApplication.translate("StackedWidget", u"Fabricante", None))
        self.label_25.setText(QCoreApplication.translate("StackedWidget", u"Fornecedor", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("StackedWidget", u"Informa\u00e7\u00f5es Tribut\u00e1rias", None))
        self.label_26.setText(QCoreApplication.translate("StackedWidget", u"NCM", None))
        self.label_27.setText(QCoreApplication.translate("StackedWidget", u"CEST", None))
        self.label_28.setText(QCoreApplication.translate("StackedWidget", u"Origem", None))
        self.label_29.setText(QCoreApplication.translate("StackedWidget", u"Tipo de Produto", None))
        self.label_30.setText(QCoreApplication.translate("StackedWidget", u"Tipo de Opera\u00e7\u00e3o", None))
        self.label_31.setText(QCoreApplication.translate("StackedWidget", u"Opera\u00e7\u00e3o PIS/COFINS", None))
        self.label_32.setText(QCoreApplication.translate("StackedWidget", u"Natureza da Receita", None))
        self.label_33.setText(QCoreApplication.translate("StackedWidget", u"Tipo de Opera\u00e7\u00e3o IPI", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("StackedWidget", u"Obs:", None))
        self.pushButton_11.setText(QCoreApplication.translate("StackedWidget", u"Limpar", None))
        self.pushButton_7.setText(QCoreApplication.translate("StackedWidget", u"Avan\u00e7ar", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("StackedWidget", u"Valores", None))
        self.label_34.setText(QCoreApplication.translate("StackedWidget", u"Valor de compra unit\u00e1rio", None))
        self.lineEdit_23.setInputMask("")
        self.lineEdit_23.setText("")
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"0,00", None))
        self.label_35.setText(QCoreApplication.translate("StackedWidget", u"Custo de Venda", None))
        self.label_36.setText(QCoreApplication.translate("StackedWidget", u"Desconto na compra", None))
        self.label_37.setText(QCoreApplication.translate("StackedWidget", u"Custo adicional na compra", None))
        self.label_38.setText(QCoreApplication.translate("StackedWidget", u"Frete da compra", None))
        self.label_39.setText(QCoreApplication.translate("StackedWidget", u"Margem de lucro", None))
        self.label_40.setText(QCoreApplication.translate("StackedWidget", u"IPI compra", None))
        self.label_41.setText(QCoreApplication.translate("StackedWidget", u"Lucro de venda (R$)", None))
        self.label_42.setText(QCoreApplication.translate("StackedWidget", u"Desconto a vista", None))
        self.label_43.setText(QCoreApplication.translate("StackedWidget", u"Valor min. de venda", None))
        self.label_44.setText(QCoreApplication.translate("StackedWidget", u"Estoque", None))
        self.label_45.setText(QCoreApplication.translate("StackedWidget", u"Pre\u00e7o de venda", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("StackedWidget", u"GroupBox", None))
        self.pushButton_8.setText(QCoreApplication.translate("StackedWidget", u"Voltar", None))
        self.pushButton_10.setText(QCoreApplication.translate("StackedWidget", u"Limpar", None))
        self.pushButton_9.setText(QCoreApplication.translate("StackedWidget", u"Inserir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StackedWidget", u"Produtos", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"Fornecedor", None))
        self.label_10.setText(QCoreApplication.translate("StackedWidget", u"Telefone", None))
        self.label_11.setText(QCoreApplication.translate("StackedWidget", u"CPF / CNPJ", None))
        self.label_12.setText(QCoreApplication.translate("StackedWidget", u"E-mail", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("StackedWidget", u"Endere\u00e7o", None))
        self.label_13.setText(QCoreApplication.translate("StackedWidget", u"Rua", None))
        self.label_14.setText(QCoreApplication.translate("StackedWidget", u"n\u00ba", None))
        self.label_15.setText(QCoreApplication.translate("StackedWidget", u"Bairro", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("StackedWidget", u"Obs:", None))
        self.pushButton_4.setText(QCoreApplication.translate("StackedWidget", u"Limpar", None))
        self.pushButton_5.setText(QCoreApplication.translate("StackedWidget", u"Pesquisar", None))
        self.pushButton_6.setText(QCoreApplication.translate("StackedWidget", u"Inserir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("StackedWidget", u"Fornecedores", None))
    # retranslateUi


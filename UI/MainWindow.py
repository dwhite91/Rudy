# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Norton & Abert\Project Rudy\Rudy\UI\MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1418, 837)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/RUDYicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("\n"
"QMainWindow#MainWindow{\n"
"    \n"
"    background-color:rgb(200, 200, 200);\n"
"    font: 10pt \"Microsoft Tai Le\";\n"
"}\n"
"QGroupBox{\n"
"    font: 75 12pt \"Microsoft Tai Le\";\n"
"}\n"
"QFrame#groupFrame,QFrame#groupFrame_2 {\n"
"    \n"
"    background-color:rgb(248, 233, 210);\n"
"}\n"
"QPushButton{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton{\n"
"    \n"
"    background-color: rgb(204, 204, 204);\n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"}\n"
"QToolButton#prevPage{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton#nextPage{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QIcon{background-color:rga(1,1,1);}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.listGroup = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listGroup.sizePolicy().hasHeightForWidth())
        self.listGroup.setSizePolicy(sizePolicy)
        self.listGroup.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.listGroup.setFlat(True)
        self.listGroup.setObjectName(_fromUtf8("listGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.listGroup)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupFrame = QtGui.QFrame(self.listGroup)
        self.groupFrame.setFrameShape(QtGui.QFrame.Panel)
        self.groupFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.groupFrame.setLineWidth(1)
        self.groupFrame.setObjectName(_fromUtf8("groupFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupFrame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupFrame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.groupFrame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.searchContacts = QtGui.QLineEdit(self.groupFrame)
        self.searchContacts.setObjectName(_fromUtf8("searchContacts"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.searchContacts)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.search = QtGui.QPushButton(self.groupFrame)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.reset = QtGui.QPushButton(self.groupFrame)
        self.reset.setObjectName(_fromUtf8("reset"))
        self.horizontalLayout.addWidget(self.reset)
        self.formLayout.setLayout(3, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.searchFirst = QtGui.QLineEdit(self.groupFrame)
        self.searchFirst.setObjectName(_fromUtf8("searchFirst"))
        self.horizontalLayout_7.addWidget(self.searchFirst)
        self.searchLast = QtGui.QLineEdit(self.groupFrame)
        self.searchLast.setObjectName(_fromUtf8("searchLast"))
        self.horizontalLayout_7.addWidget(self.searchLast)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.searchAddr = QtGui.QLineEdit(self.groupFrame)
        self.searchAddr.setObjectName(_fromUtf8("searchAddr"))
        self.gridLayout_10.addWidget(self.searchAddr, 0, 0, 1, 1)
        self.searchState = QtGui.QLineEdit(self.groupFrame)
        self.searchState.setMaximumSize(QtCore.QSize(75, 16777215))
        self.searchState.setObjectName(_fromUtf8("searchState"))
        self.gridLayout_10.addWidget(self.searchState, 0, 2, 1, 1)
        self.searchCity = QtGui.QLineEdit(self.groupFrame)
        self.searchCity.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.searchCity.setObjectName(_fromUtf8("searchCity"))
        self.gridLayout_10.addWidget(self.searchCity, 0, 1, 1, 1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.gridLayout_10)
        self.verticalLayout.addLayout(self.formLayout)
        self.clientList = QtGui.QTableWidget(self.groupFrame)
        self.clientList.setObjectName(_fromUtf8("clientList"))
        self.clientList.setColumnCount(6)
        self.clientList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.clientList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.clientList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.clientList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.clientList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.clientList.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.clientList.setHorizontalHeaderItem(5, item)
        self.clientList.horizontalHeader().setDefaultSectionSize(75)
        self.verticalLayout.addWidget(self.clientList)
        self.verticalLayout_2.addWidget(self.groupFrame)
        self.horizontalLayout_6.addWidget(self.listGroup)
        self.detailGroup = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailGroup.sizePolicy().hasHeightForWidth())
        self.detailGroup.setSizePolicy(sizePolicy)
        self.detailGroup.setStyleSheet(_fromUtf8(""))
        self.detailGroup.setFlat(True)
        self.detailGroup.setObjectName(_fromUtf8("detailGroup"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.detailGroup)
        self.verticalLayout_9.setContentsMargins(3, 0, 0, 0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.groupFrame_2 = QtGui.QFrame(self.detailGroup)
        self.groupFrame_2.setFrameShape(QtGui.QFrame.Panel)
        self.groupFrame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.groupFrame_2.setObjectName(_fromUtf8("groupFrame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupFrame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.clientAddress = QtGui.QGroupBox(self.groupFrame_2)
        self.clientAddress.setFlat(True)
        self.clientAddress.setObjectName(_fromUtf8("clientAddress"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.clientAddress)
        self.verticalLayout_5.setMargin(1)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame_3 = QtGui.QFrame(self.clientAddress)
        self.frame_3.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(220, 220, 220); }"))
        self.frame_3.setFrameShape(QtGui.QFrame.Panel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_27 = QtGui.QLabel(self.frame_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_27)
        self.addr1 = QtGui.QLineEdit(self.frame_3)
        self.addr1.setObjectName(_fromUtf8("addr1"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.addr1)
        self.label_28 = QtGui.QLabel(self.frame_3)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_28)
        self.addr2 = QtGui.QLineEdit(self.frame_3)
        self.addr2.setObjectName(_fromUtf8("addr2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.addr2)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_24 = QtGui.QLabel(self.frame_3)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_9.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.frame_3)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_9.addWidget(self.label_25, 0, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.frame_3)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_9.addWidget(self.label_26, 0, 2, 1, 1)
        self.city = QtGui.QLineEdit(self.frame_3)
        self.city.setObjectName(_fromUtf8("city"))
        self.gridLayout_9.addWidget(self.city, 1, 0, 1, 1)
        self.state = QtGui.QComboBox(self.frame_3)
        self.state.setObjectName(_fromUtf8("state"))
        self.gridLayout_9.addWidget(self.state, 1, 1, 1, 1)
        self.zipcode = QtGui.QLineEdit(self.frame_3)
        self.zipcode.setMaximumSize(QtCore.QSize(75, 16777215))
        self.zipcode.setObjectName(_fromUtf8("zipcode"))
        self.gridLayout_9.addWidget(self.zipcode, 1, 2, 1, 1)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.SpanningRole, self.gridLayout_9)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.gridLayout_2.addWidget(self.clientAddress, 3, 0, 1, 1)
        self.clientInfo = QtGui.QGroupBox(self.groupFrame_2)
        self.clientInfo.setFlat(True)
        self.clientInfo.setObjectName(_fromUtf8("clientInfo"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.clientInfo)
        self.verticalLayout_3.setMargin(1)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.clientInfo)
        self.frame.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(220, 220, 220); }"))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.firstName = QtGui.QLineEdit(self.frame)
        self.firstName.setObjectName(_fromUtf8("firstName"))
        self.gridLayout.addWidget(self.firstName, 1, 0, 1, 1)
        self.middleInitial = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleInitial.sizePolicy().hasHeightForWidth())
        self.middleInitial.setSizePolicy(sizePolicy)
        self.middleInitial.setMaximumSize(QtCore.QSize(75, 16777215))
        self.middleInitial.setObjectName(_fromUtf8("middleInitial"))
        self.gridLayout.addWidget(self.middleInitial, 1, 1, 1, 1)
        self.lastName = QtGui.QLineEdit(self.frame)
        self.lastName.setObjectName(_fromUtf8("lastName"))
        self.gridLayout.addWidget(self.lastName, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.clientInfo, 2, 0, 1, 1)
        self.clientContact = QtGui.QGroupBox(self.groupFrame_2)
        self.clientContact.setFlat(True)
        self.clientContact.setObjectName(_fromUtf8("clientContact"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.clientContact)
        self.verticalLayout_6.setMargin(1)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.frame_4 = QtGui.QFrame(self.clientContact)
        self.frame_4.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(220, 220, 220); }"))
        self.frame_4.setFrameShape(QtGui.QFrame.Panel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_33 = QtGui.QLabel(self.frame_4)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_33)
        self.phone1 = QtGui.QLineEdit(self.frame_4)
        self.phone1.setObjectName(_fromUtf8("phone1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.phone1)
        self.label_32 = QtGui.QLabel(self.frame_4)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_32)
        self.phone2 = QtGui.QLineEdit(self.frame_4)
        self.phone2.setObjectName(_fromUtf8("phone2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.phone2)
        self.label_34 = QtGui.QLabel(self.frame_4)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_34)
        self.email = QtGui.QLineEdit(self.frame_4)
        self.email.setObjectName(_fromUtf8("email"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.email)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.gridLayout_2.addWidget(self.clientContact, 3, 1, 1, 1)
        self.spouseInfo = QtGui.QGroupBox(self.groupFrame_2)
        self.spouseInfo.setFlat(True)
        self.spouseInfo.setCheckable(True)
        self.spouseInfo.setObjectName(_fromUtf8("spouseInfo"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.spouseInfo)
        self.verticalLayout_4.setMargin(1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame_2 = QtGui.QFrame(self.spouseInfo)
        self.frame_2.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(220, 220, 220); }"))
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 0, 2, 1, 1)
        self.firstName_2 = QtGui.QLineEdit(self.frame_2)
        self.firstName_2.setObjectName(_fromUtf8("firstName_2"))
        self.gridLayout_5.addWidget(self.firstName_2, 1, 0, 1, 1)
        self.middleInitial_2 = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleInitial_2.sizePolicy().hasHeightForWidth())
        self.middleInitial_2.setSizePolicy(sizePolicy)
        self.middleInitial_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.middleInitial_2.setObjectName(_fromUtf8("middleInitial_2"))
        self.gridLayout_5.addWidget(self.middleInitial_2, 1, 1, 1, 1)
        self.lastName_2 = QtGui.QLineEdit(self.frame_2)
        self.lastName_2.setObjectName(_fromUtf8("lastName_2"))
        self.gridLayout_5.addWidget(self.lastName_2, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.spouseInfo, 2, 1, 1, 1)
        self.clientAddress_3 = QtGui.QGroupBox(self.groupFrame_2)
        self.clientAddress_3.setFlat(True)
        self.clientAddress_3.setObjectName(_fromUtf8("clientAddress_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.clientAddress_3)
        self.verticalLayout_7.setMargin(1)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.notes = QtGui.QTextEdit(self.clientAddress_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        self.notes.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.notes.setObjectName(_fromUtf8("notes"))
        self.verticalLayout_7.addWidget(self.notes)
        self.gridLayout_2.addWidget(self.clientAddress_3, 2, 2, 2, 1)
        self.mattersGroup = QtGui.QGroupBox(self.groupFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mattersGroup.sizePolicy().hasHeightForWidth())
        self.mattersGroup.setSizePolicy(sizePolicy)
        self.mattersGroup.setObjectName(_fromUtf8("mattersGroup"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.mattersGroup)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.addMatter = QtGui.QToolButton(self.mattersGroup)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/plus.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addMatter.setIcon(icon1)
        self.addMatter.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.addMatter.setObjectName(_fromUtf8("addMatter"))
        self.horizontalLayout_5.addWidget(self.addMatter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.matterList = QtGui.QTableWidget(self.mattersGroup)
        self.matterList.setObjectName(_fromUtf8("matterList"))
        self.matterList.setColumnCount(6)
        self.matterList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.matterList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.matterList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.matterList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.matterList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.matterList.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.matterList.setHorizontalHeaderItem(5, item)
        self.matterList.horizontalHeader().setDefaultSectionSize(75)
        self.verticalLayout_8.addWidget(self.matterList)
        self.gridLayout_2.addWidget(self.mattersGroup, 4, 0, 1, 3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.addClient = QtGui.QToolButton(self.groupFrame_2)
        self.addClient.setIcon(icon1)
        self.addClient.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.addClient.setObjectName(_fromUtf8("addClient"))
        self.horizontalLayout_3.addWidget(self.addClient)
        self.saveClientChanges = QtGui.QToolButton(self.groupFrame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveClientChanges.setIcon(icon2)
        self.saveClientChanges.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.saveClientChanges.setObjectName(_fromUtf8("saveClientChanges"))
        self.horizontalLayout_3.addWidget(self.saveClientChanges)
        self.editClient = QtGui.QToolButton(self.groupFrame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/note.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editClient.setIcon(icon3)
        self.editClient.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.editClient.setObjectName(_fromUtf8("editClient"))
        self.horizontalLayout_3.addWidget(self.editClient)
        self.clearContent = QtGui.QToolButton(self.groupFrame_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/clear.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearContent.setIcon(icon4)
        self.clearContent.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clearContent.setObjectName(_fromUtf8("clearContent"))
        self.horizontalLayout_3.addWidget(self.clearContent)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupFrame_2)
        self.label_4.setStyleSheet(_fromUtf8("font: 75 12pt \"Microsoft Tai Le\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.clientNum = QtGui.QLineEdit(self.groupFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientNum.sizePolicy().hasHeightForWidth())
        self.clientNum.setSizePolicy(sizePolicy)
        self.clientNum.setObjectName(_fromUtf8("clientNum"))
        self.horizontalLayout_4.addWidget(self.clientNum)
        self.donotrep = QtGui.QCheckBox(self.groupFrame_2)
        self.donotrep.setObjectName(_fromUtf8("donotrep"))
        self.horizontalLayout_4.addWidget(self.donotrep)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 3)
        self.verticalLayout_9.addWidget(self.groupFrame_2)
        self.horizontalLayout_6.addWidget(self.detailGroup)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1418, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAdmin = QtGui.QMenu(self.menubar)
        self.menuAdmin.setObjectName(_fromUtf8("menuAdmin"))
        self.menuReports = QtGui.QMenu(self.menubar)
        self.menuReports.setObjectName(_fromUtf8("menuReports"))
        MainWindow.setMenuBar(self.menubar)
        self.actionManage_Users = QtGui.QAction(MainWindow)
        self.actionManage_Users.setObjectName(_fromUtf8("actionManage_Users"))
        self.actionManage_Matter_Types = QtGui.QAction(MainWindow)
        self.actionManage_Matter_Types.setObjectName(_fromUtf8("actionManage_Matter_Types"))
        self.menuAdmin.addAction(self.actionManage_Matter_Types)
        self.menuAdmin.addAction(self.actionManage_Users)
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.searchContacts, self.search)
        MainWindow.setTabOrder(self.search, self.reset)
        MainWindow.setTabOrder(self.reset, self.clientList)
        MainWindow.setTabOrder(self.clientList, self.clientNum)
        MainWindow.setTabOrder(self.clientNum, self.donotrep)
        MainWindow.setTabOrder(self.donotrep, self.firstName)
        MainWindow.setTabOrder(self.firstName, self.middleInitial)
        MainWindow.setTabOrder(self.middleInitial, self.lastName)
        MainWindow.setTabOrder(self.lastName, self.spouseInfo)
        MainWindow.setTabOrder(self.spouseInfo, self.firstName_2)
        MainWindow.setTabOrder(self.firstName_2, self.middleInitial_2)
        MainWindow.setTabOrder(self.middleInitial_2, self.lastName_2)
        MainWindow.setTabOrder(self.lastName_2, self.addr1)
        MainWindow.setTabOrder(self.addr1, self.addr2)
        MainWindow.setTabOrder(self.addr2, self.city)
        MainWindow.setTabOrder(self.city, self.state)
        MainWindow.setTabOrder(self.state, self.zipcode)
        MainWindow.setTabOrder(self.zipcode, self.phone1)
        MainWindow.setTabOrder(self.phone1, self.phone2)
        MainWindow.setTabOrder(self.phone2, self.email)
        MainWindow.setTabOrder(self.email, self.notes)
        MainWindow.setTabOrder(self.notes, self.addMatter)
        MainWindow.setTabOrder(self.addMatter, self.matterList)
        MainWindow.setTabOrder(self.matterList, self.addClient)
        MainWindow.setTabOrder(self.addClient, self.saveClientChanges)
        MainWindow.setTabOrder(self.saveClientChanges, self.editClient)
        MainWindow.setTabOrder(self.editClient, self.clearContent)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Rudy", None))
        self.listGroup.setTitle(_translate("MainWindow", "Client List", None))
        self.label.setText(_translate("MainWindow", "Search Name", None))
        self.label_2.setText(_translate("MainWindow", "Search Address", None))
        self.label_3.setText(_translate("MainWindow", "Search Phone or Email", None))
        self.search.setText(_translate("MainWindow", "Search", None))
        self.reset.setText(_translate("MainWindow", "Reset", None))
        self.searchFirst.setPlaceholderText(_translate("MainWindow", "First Name", None))
        self.searchLast.setPlaceholderText(_translate("MainWindow", "Last Name", None))
        self.searchAddr.setPlaceholderText(_translate("MainWindow", "Address", None))
        self.searchState.setPlaceholderText(_translate("MainWindow", "State", None))
        self.searchCity.setPlaceholderText(_translate("MainWindow", "City", None))
        item = self.clientList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Client #", None))
        item = self.clientList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Client Name", None))
        item = self.clientList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address", None))
        item = self.clientList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "City", None))
        item = self.clientList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "State", None))
        item = self.clientList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Zip", None))
        self.detailGroup.setTitle(_translate("MainWindow", "Client Details", None))
        self.clientAddress.setTitle(_translate("MainWindow", "Address", None))
        self.label_27.setText(_translate("MainWindow", "Address 1", None))
        self.label_28.setText(_translate("MainWindow", "Address 2", None))
        self.label_24.setText(_translate("MainWindow", "City", None))
        self.label_25.setText(_translate("MainWindow", "State", None))
        self.label_26.setText(_translate("MainWindow", "Zip", None))
        self.clientInfo.setTitle(_translate("MainWindow", "Client Info", None))
        self.label_5.setText(_translate("MainWindow", "First Name", None))
        self.label_6.setText(_translate("MainWindow", "Middle Initial", None))
        self.label_7.setText(_translate("MainWindow", "LastName", None))
        self.clientContact.setTitle(_translate("MainWindow", "Contact", None))
        self.label_33.setText(_translate("MainWindow", "Phone 1", None))
        self.label_32.setText(_translate("MainWindow", "Phone 2", None))
        self.label_34.setText(_translate("MainWindow", "Email", None))
        self.spouseInfo.setTitle(_translate("MainWindow", "Married", None))
        self.label_13.setText(_translate("MainWindow", "Spouse First Name", None))
        self.label_14.setText(_translate("MainWindow", "Middle Initial", None))
        self.label_15.setText(_translate("MainWindow", "Spouse LastName", None))
        self.clientAddress_3.setTitle(_translate("MainWindow", "Notes", None))
        self.mattersGroup.setTitle(_translate("MainWindow", "Client Matters", None))
        self.addMatter.setText(_translate("MainWindow", "Add New Matter", None))
        item = self.matterList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Matter #", None))
        item = self.matterList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type", None))
        item = self.matterList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Attorney", None))
        item = self.matterList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date Opened", None))
        item = self.matterList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Closed?", None))
        item = self.matterList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "View Matter", None))
        self.addClient.setText(_translate("MainWindow", "Add", None))
        self.saveClientChanges.setText(_translate("MainWindow", "Save", None))
        self.editClient.setText(_translate("MainWindow", "Edit", None))
        self.clearContent.setText(_translate("MainWindow", "Clear", None))
        self.label_4.setText(_translate("MainWindow", "Client #", None))
        self.donotrep.setText(_translate("MainWindow", "Do Not Represent", None))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin", None))
        self.menuReports.setTitle(_translate("MainWindow", "Reports", None))
        self.actionManage_Users.setText(_translate("MainWindow", "Manage Users", None))
        self.actionManage_Matter_Types.setText(_translate("MainWindow", "Manage Matter Types", None))

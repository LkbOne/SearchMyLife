# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainShow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(935, 613)
        self.initSearchCombox(Form)
        self.initSearchTextAndButton(Form)

        self.listView_2 = QtWidgets.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(290, 360, 371, 251))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(Form)
        self.listView_3.setGeometry(QtCore.QRect(680, 100, 251, 511))
        self.listView_3.setObjectName("listView_3")

        self.listView_4 = QtWidgets.QListView(Form)
        self.listView_4.setGeometry(QtCore.QRect(290, 100, 371, 251))
        self.listView_4.setObjectName("listView_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 70, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(790, 70, 54, 12))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 261, 511))
        self.listWidget.setObjectName("listWidget")
        self.recomandItem = QtWidgets.QWidget(Form)
        self.recomandItem.setGeometry(QtCore.QRect(20, 110, 231, 51))
        self.recomandItem.setObjectName("recomandItem")
        self.label_3 = QtWidgets.QLabel(self.recomandItem)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.recomandItem)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def initSearchCombox(self, Form):
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(430, 0, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Baidu")
        self.comboBox.addItem("JD")
        self.comboBox.addItem("TianMao")
        self.comboBox.addItem("QQMusic")
        self.comboBox.addItem("QQVideo")
        self.comboBox.addItem("DouBan")
        self.comboBox.addItem("Google")
        self.comboBox.addItem("Youtube")


    def clickForSearch(self):
        print("clickForSearch")

    def initSearchTextAndButton(self, Form):
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setGeometry(QtCore.QRect(250, 30, 451, 31))
        self.searchEdit.setObjectName("searchEdit")

        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(430, 70, 75, 23))
        # self.searchButton.setDefault(False)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.setText("SEARCH")
        self.searchButton.clicked.connect(self.clickForSearch)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LIFE"))
        self.label.setText(_translate("Form", "Recomand"))
        self.label_2.setText(_translate("Form", "now"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.lineEdit.setText(_translate("Form", "text"))


import json
import re
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDesktopWidget, QLineEdit, QMessageBox, QCheckBox, \
    QLabel, QComboBox, QSystemTrayIcon, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from WebSelenium import Selenium
from requestBackend import RequestBackend


class FirstGUI(QWidget):
    windowWidth = 500
    windowHeight = 200


    comboxWidthForSearch = 80
    comboxHeightForSearch = 25
    comboxMoveDownForSearch = 0
    comboxMoveRightForSearch = 0

    comboxWidthForBrower = 80
    comboxHeightForBrower = 25

    comboxMoveRightForBrower = windowWidth - comboxWidthForBrower
    comboxMoveDownForBrower = comboxMoveDownForSearch

    textWidht = windowWidth - 1 - comboxWidthForSearch
    textHeight = 20
    textMoveDown = comboxHeightForSearch + 1
    textMoveRight = 0

    buttonMoveDown = comboxHeightForBrower
    buttonMoveRight = textWidht

    buttonWidth = comboxWidthForSearch
    buttonHeight = textHeight
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(self.windowWidth, self.windowHeight)
        self.center()
        self.initTextBox()
        self.initComboBoxForBrower()
        self.initComboBoxForSearchLink()
        self.initButtonForSearch()

        self.initButtonForTable()
        self.show()
        self.systemButtonPane()
        self.inittable()

        pass

    def initTextBox(self):
        self.textbox = QLineEdit(self)
        self.textbox.move(self.textMoveRight, self.textMoveDown)
        self.textbox.resize(self.textWidht, self.textHeight)

    def initButtonForSearch(self):
        self.searchBtn = QPushButton('click me', self)
        self.searchBtn.move(self.buttonMoveRight, self.buttonMoveDown)
        self.searchBtn.resize(self.buttonWidth, self.buttonHeight)
        self.searchBtn.clicked.connect(self.clickForSearch)

    def initButtonForTable(self):
        self.addItemButton = QPushButton('click me22', self)
        self.addItemButton.move(self.buttonMoveRight + 30, self.buttonMoveDown + 30)
        self.addItemButton.resize(self.buttonWidth, self.buttonHeight)
        self.addItemButton.clicked.connect(self.clickForAddItem)


    def initComboBoxForBrower(self):
        self.lb = QLabel('打开的浏览器', self)
        combo = QComboBox(self)
        combo.addItem('Chrome')
        combo.addItem('Firefox')
        combo.resize(self.comboxWidthForBrower, self.comboxHeightForBrower)
        combo.move(self.comboxMoveRightForBrower, self.comboxMoveDownForBrower)
        self.lb.move(50, 150)
        combo.activated[str].connect(self.onActivatedForBrower)

    def initComboBoxForSearchLink(self):
        self.lbSearch = QLabel('搜索的网址', self)
        comboSearch = QComboBox(self)
        comboSearch.addItem('Baidu')
        comboSearch.addItem('JD')
        comboSearch.addItem('TianMao')
        comboSearch.addItem('Google')
        comboSearch.addItem('Youtube')
        comboSearch.move(self.comboxMoveRightForSearch, self.comboxMoveDownForSearch)
        comboSearch.resize(self.comboxWidthForSearch, self.comboxHeightForSearch)
        self.lb.move(100, 150)
        comboSearch.activated[str].connect(self.onActivatedForSearch)

    def systemButtonPane(self):
        self.tray = QSystemTrayIcon() #创建系统托盘对象
        self.icon = QIcon('earth.ico')  #创建图标
        self.tray.setIcon(self.icon)
        self.tray.show()#显示系统托盘
        self.tray.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActivated)

    count = 0
    countArray = []
    def inittable(self):
        self.tableWidget = QTableWidget(0, 2)
        self.tableWidget.setHorizontalHeaderLabels(['Thing', 'ThingItem'])

    def dealTextForPattern(self, text):
        seat = re.search(':', text).span()
        textGroup = []
        textGroup.append(text[0 : seat[1] - 1])
        textGroup.append(text[seat[1] : len(text)])

        return textGroup
    def addTableItem(self, text):
        text = self.dealTextForPattern(text)
        self.count += 1
        self.countArray.append(str(self.count))
        newItemTitle = QTableWidgetItem(text[0])
        newItemThing = QTableWidgetItem(text[1])
        self.tableWidget.setRowCount((self.count))
        self.tableWidget.setItem(self.count - 1, 0, newItemTitle)
        self.tableWidget.setItem(self.count - 1, 1, newItemThing)
        self.tableWidget.setVerticalHeaderLabels(self.countArray)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.show()


    def onActivatedForBrower(self, text):
        self.lb.setText(text)
        self.lb.adjustSize()
        self.webView = Selenium(text)

    def onActivatedForSearch(self, text):
        self.webView.setSearchTarget(text)

    def clickForSearch(self):
        textBoxValue = self.textbox.text()
        self.webView.search(textBoxValue)

    def clickForAddItem(self):
        textBoxValue = self.textbox.text()
        self.addTableItem(textBoxValue)

    def center(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    callBackend = RequestBackend()
    aa = callBackend.getRequest("http://localhost:9090/searchMyLife/init")
    # data={'name':'value'}
    # encode_data= json.dumps(data).encode()
    name = "12"
    bb = callBackend.postRequest("http://localhost:9090/searchMyLife/init", name)
    firstGui = FirstGUI()
    sys.exit(app.exec_())

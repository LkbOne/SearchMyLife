import re

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QLineEdit, QLabel, QComboBox, QSystemTrayIcon, \
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QListWidget
from PyQt5 import QtCore
from service.SearchService import Search
from service.entity.Station import BaiDuStation, QQVideoStation, QQMusicStation, TianMaoStation, JDStation, \
    DouBanStation, DouBanBookStation, TaoBaoStation
from view.ListWidget import ListWidget
from view.WebSelenium import Selenium


class FirstGUI(QWidget):
    windowWidth = 935
    windowHeight = 613

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
        # -----------------------
        self.initLeftListWidget()
        self.initRightListWidget()
        self.initUpListWidget()
        self.initDownListWidget()
        # -----------------------
        self.show()
        self.systemButtonPane()
        self.inittable()

        pass
    def initLeftListWidget(self):
        self.leftListWidget = ListWidget(self)
        self.leftListWidget.setGeometry(QtCore.QRect(10, 100, 261, 511))

    def initRightListWidget(self):
        self.rightListWidget = ListWidget(self)
        self.rightListWidget.setGeometry(QtCore.QRect(680, 100, 251, 511))

    def initUpListWidget(self):
        self.upListWidget = ListWidget(self)
        self.upListWidget.setGeometry(QtCore.QRect(290, 100, 371, 251))

    def initDownListWidget(self):
        self.downListWidget = QListWidget(self)
        self.downListWidget.setGeometry(QtCore.QRect(290, 360, 371, 251))

    def initTextBox(self):
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(QtCore.QRect(250, 30, 451, 31))


    def initButtonForSearch(self):
        self.searchBtn = QPushButton('SEARCH', self)
        self.searchBtn.setGeometry(QtCore.QRect(430, 70, 75, 23))
        self.searchBtn.clicked.connect(self.clickForSearch)


    def initComboBoxForBrower(self):
        self.webView = Selenium('Chrome')
        self.webDrive = self.webView.driver

    def initComboBoxForSearchLink(self):
        self.lbSearch = QLabel('搜索的网址', self)
        comboSearch = QComboBox(self)
        comboSearch.addItem('Baidu')
        comboSearch.addItem('JD')
        comboSearch.addItem('TianMao')
        comboSearch.addItem('Google')
        comboSearch.addItem('Youtube')
        comboSearch.addItem('QQMusic')
        comboSearch.addItem('QQVideo')
        comboSearch.addItem('DouBan')
        comboSearch.addItem('DouBanBook')
        comboSearch.setGeometry(QtCore.QRect(430, 0, 69, 22))
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
        self.station = None
        if text == "Baidu":
            self.station = BaiDuStation()
        elif text == "JD":
            self.station = JDStation()
        elif text == "TianMao":
            self.station = TianMaoStation()
        elif text == "QQMusic":
            self.station = QQMusicStation()
        elif text == "QQVideo":
            self.station = QQVideoStation()
        elif text == "DouBan":
            self.station = DouBanStation()
        elif text == "DouBanBook":
            self.station = DouBanBookStation()

        if self.station is not None:
            self.station.visitStation(self.webDrive)

    def clickForSearch(self):
        textBoxValue = self.textbox.text()
        print("clickForSearch:" + textBoxValue)
        # list, subList = self.webView.search(textBoxValue)
        self.station.search(self.webDrive, textBoxValue)
        if type(self.station) == QQMusicStation:
            self.station.start()
            self.station.data.connect(self.set_MusicListWidget)
        if type(self.station) == DouBanBookStation:
            self.station.start()
            self.station.data.connect(self.set_DouBanBookListWidget)
        if type(self.station) == QQVideoStation:
            self.station.start()
            self.station.data.connect(self.set_QQVideoListWidget)
        if type(self.station) == TianMaoStation:
            self.station.start()
            self.station.data.connect(self.set_ShopListWidget)
        if type(self.station) == JDStation:
            self.station.start()
            self.station.data.connect(self.set_ShopListWidget)

    def set_DouBanBookListWidget(self, data):
        if data is not None:
            # self.leftListWidget.
            self.leftListWidget.init_Tian_Mao_Item(data[0], self.station, 2)
            self.upListWidget.initRightCustinWidgetItem(data[1], self.station, 5)
            self.rightListWidget.init_Tian_Mao_Item(data[2], self.station, 2)

    def set_MusicListWidget(self, data):
        if data is not None:
            self.upListWidget.initCustomWidgetItem(data[0], self.station)
            self.rightListWidget.initRightCustinWidgetItem(data[1], self.station, 5)

    def set_QQVideoListWidget(self, data):
        if data is not None and len(data) == 2:
            if data[0] is not None:
                 self.upListWidget.init_TX_Video_Item(data[0], self.station, 5)
            if data[1] is not None:
                self.rightListWidget.initRightCustinWidgetItem(data[1], self.station, 5)
    def set_ShopListWidget(self, data):
        if data is not None:
            self.upListWidget.init_Tian_Mao_Item(data[0], self.station)
            self.rightListWidget.init_Tian_Mao_Item(data[1], self.station, 2)

    def clickForAddItem(self):
        textBoxValue = self.textbox.text()
        self.addTableItem(textBoxValue)

    def center(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    # 图标作用
    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()


from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *

from service.SearchService import Search
from view.CustomWidget import CustomWidget


class ListWidget(QListWidget):

    def init(self):
        self.search = Search()
    def updateListWidget(self, searchList, webView):
        self.clear()
        self.searchList = searchList
        if searchList is not None:
            for value in searchList:
                self.addItem(value.getTitle())
        self.webView = webView




    def initCustomWidgetItem(self, data, station):
        self.clear()
        self.searchList = data
        for itemData in data:
            item_widget = QListWidgetItem()
            item_widget.setSizeHint(QSize(90, 60))
            self.addItem(item_widget)
            label = CustomWidget(itemData, 'music')
            self.setItemWidget(item_widget, label)
        self.trace_type = 1
        self.itemClicked.connect(self.click)
        self.station = station

    def init_Tian_Mao_Item(self, data, station, trace = 0):
        self.clear()
        self.searchList = data
        for index, itemData in enumerate(data):
            if index > 5:
                break
            item_widget = QListWidgetItem()
            item_widget.setSizeHint(QSize(90, 60))
            self.addItem(item_widget)
            label = CustomWidget(itemData, 'shop')
            self.setItemWidget(item_widget, label)
        self.trace_type = trace
        self.itemClicked.connect(self.click)
        self.station = station

    def init_TX_Video_Item(self, data, station, trace = 0):
        self.clear()
        self.searchList = data
        for index, itemData in enumerate(data):
            if index > 5:
                break
            item_widget = QListWidgetItem()
            item_widget.setSizeHint(QSize(90, 60))
            self.addItem(item_widget)
            label = CustomWidget(itemData, 'tx_video')
            self.setItemWidget(item_widget, label)
        self.trace_type = trace
        self.itemClicked.connect(self.click)
        self.station = station


    def initRightCustinWidgetItem(self, data, station, trace):
        self.clear()
        self.searchList = data
        for itemData in data:
            item_widget = QListWidgetItem()
            item_widget.setSizeHint(QSize(90, 60))
            self.addItem(item_widget)
            label = CustomWidget(itemData, 'douban')
            self.setItemWidget(item_widget, label)
        self.trace_type = trace
        self.itemClicked.connect(self.click)
        self.station = station


    def click(self):
        # item.text()  获取内容
        print("item:" + str(self.currentRow()))
        url = self.searchList[self.currentRow()].getUrl()
        self.station.visitChildStation(url, self.trace_type)

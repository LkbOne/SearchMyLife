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


    def initCustomWidgetItem(self, data, webView):
        self.clear()
        self.searchList = data
        for itemData in data:
            item_widget = QListWidgetItem()
            item_widget.setSizeHint(QSize(90, 60))
            self.addItem(item_widget)
            label = CustomWidget(itemData, 'music')
            self.setItemWidget(item_widget, label)
        self.itemClicked.connect(self.click)
        self.webView = webView

    def initRightCustinWidgetItem(self, data, webView):
        self.clear()
        self.searchList = data
        for itemData in data:
            item_widget = QListWidgetItem()
            item_widget.setSizeHint(QSize(90, 60))
            self.addItem(item_widget)
            label = CustomWidget(itemData, 'douban')
            self.setItemWidget(item_widget, label)
        self.itemClicked.connect(self.click)
        self.webView = webView


    def click(self):
        # item.text()  获取内容
        print("item:" + str(self.currentRow()))
        url = self.searchList[self.currentRow()].getUrl()
        print("url:" + str(url))
        self.webView.setSearchTarget(None, url)
        # self.search.rebackUrl(url)



        # self.currentItem().
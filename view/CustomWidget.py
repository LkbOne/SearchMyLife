import requests
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout,
                            QHBoxLayout, QListWidget, QListWidgetItem)

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont


class CustomWidget(QWidget):

    def initDouBanMusic(self, data):
        self.lb_title = QLabel(data.getTitle())
        self.lb_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lb_subtitle = QLabel(data.getActor())
        self.lb_subtitle.setFont(QFont("Arial", 8, QFont.StyleItalic))
        self.lb_icon = QLabel()
        self.lb_icon.setFixedSize(40, 40)

        req = requests.get(data.getCover())

        pixMap = QPixmap()
        pixMap.loadFromData(req.content)

        self.lb_icon.setPixmap(pixMap.scaled(self.lb_icon.width(), self.lb_icon.height()))

    def initQQMusic(self, data):
        self.lb_title = QLabel(data.getSongTitle())
        self.lb_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lb_subtitle = QLabel(data.getSingerName())
        self.lb_subtitle.setFont(QFont("Arial", 8, QFont.StyleItalic))
        self.lb_icon = QLabel()
        self.lb_icon.setFixedSize(40, 40)

        # req = requests.get(data.getCover())

        pixMap = QPixmap("D:\MBC\TestForSel\static\earth.ico")
        # pixMap.loadFromData(req.content)

        self.lb_icon.setPixmap(pixMap.scaled(self.lb_icon.width(), self.lb_icon.height()))

    def init_shop_data(self, data):
        self.lb_title = QLabel(data.get_title())
        self.lb_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lb_price = QLabel(data.get_price())
        self.lb_price.setFont(QFont("Arial", 8, QFont.StyleItalic))
        self.lb_icon = QLabel()
        self.lb_icon.setFixedSize(40, 40)

        req = requests.get(data.get_img())

        pixMap = QPixmap()
        pixMap.loadFromData(req.content)

        self.lb_icon.setPixmap(pixMap.scaled(self.lb_icon.width(), self.lb_icon.height()))

    def __init__(self, data, type):
        """
        :param title: str title
        :param subtitle: str subtitle
        :param icon_path: path of picture
        """
        super(CustomWidget, self).__init__()
        if type == 'douban':
            self.initDouBanMusic(data)
        if type == 'music':
            self.initQQMusic(data)
        if type == 'shop':
            self.init_shop_data(data)
            self.init_shop_ui()
            return
        if type == 'tx_video':
            self.init_tx_video_data(data)
            # self.init_tx_video_ui()
            # return
        self.double_click_fun = None
        self.init_ui()

    def init_tx_video_data(self, data):
        self.lb_title = QLabel(data.getTitle())
        self.lb_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lb_subtitle = QLabel(data.getSubTitle())
        self.lb_subtitle.setFont(QFont("Arial", 8, QFont.StyleItalic))
        self.lb_icon = QLabel()
        self.lb_icon.setFixedSize(40, 40)

        req = requests.get(data.getImg())

        pixMap = QPixmap()
        pixMap.loadFromData(req.content)

        self.lb_icon.setPixmap(pixMap.scaled(self.lb_icon.width(), self.lb_icon.height()))

    def init_ui(self):
        """handle layout"""
        ly_main = QHBoxLayout()
        ly_right = QVBoxLayout()
        ly_right.addWidget(self.lb_title)
        ly_right.addWidget(self.lb_subtitle)
        ly_right.setAlignment(Qt.AlignVCenter)
        ly_main.addWidget(self.lb_icon)
        ly_main.addLayout(ly_right)
        self.setLayout(ly_main)
        self.resize(90, 60)

    def init_shop_ui(self):
        ly_main = QHBoxLayout()
        ly_down = QVBoxLayout()
        ly_down.addWidget(self.lb_title)
        ly_down.addWidget(self.lb_price)
        ly_down.setAlignment(Qt.AlignVCenter)
        ly_main.addWidget(self.lb_icon)
        ly_main.addLayout(ly_down)
        self.setLayout(ly_main)
        self.resize(90, 60)

    def get_lb_title(self):
        return self.lb_title.text()

    def get_lb_subtitle(self):
        return self.lb_subtitle.text()

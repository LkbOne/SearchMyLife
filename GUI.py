import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDesktopWidget, QLineEdit, QMessageBox, QCheckBox, \
    QLabel, QComboBox
from WebSelenium import Selenium


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
        self.initButton()
        self.show()
        pass

    def initTextBox(self):
        self.textbox = QLineEdit(self)
        self.textbox.move(self.textMoveRight, self.textMoveDown)
        self.textbox.resize(self.textWidht, self.textHeight)

    def initButton(self):
        self.btn = QPushButton('click me', self)
        self.btn.move(self.buttonMoveRight, self.buttonMoveDown)
        self.btn.resize(self.buttonWidth, self.buttonHeight)
        self.btn.clicked.connect(self.on_click)

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

    def onActivatedForBrower(self, text):
        self.lb.setText(text)
        self.lb.adjustSize()
        self.webView = Selenium(text)

    def onActivatedForSearch(self, text):
        self.webView.setSearchTarget(text)

    def on_click(self):
        textBoxValue = self.textbox.text()
        self.webView.search(textBoxValue)

    def center(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstGui = FirstGUI()
    sys.exit(app.exec_())

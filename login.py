from log import Ui_MainWindow
from PyQt5.QtWidgets import QWidget

class mwindow(QWidget, Ui_MainWindow):
    def __init__(self, qwidget):
        super(mwindow, self).__init__()
        self.setupUi(qwidget)
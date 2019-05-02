
import sys
from PyQt5.QtWidgets import QApplication
from log import Ui_MainWindow
from upload import Upload_MainWindow

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # firstGui = FirstGUI()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    b = Upload_MainWindow()
    window = Ui_MainWindow(child = b)
    window.show()
    sys.exit(app.exec_())











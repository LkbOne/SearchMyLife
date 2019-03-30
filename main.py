import sys

from PyQt5.QtWidgets import QApplication

from view.GUI import FirstGUI
from view.MainShow import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstGui = FirstGUI()
    sys.exit(app.exec_())



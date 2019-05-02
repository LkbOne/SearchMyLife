import shutil

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class Second(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Get sender')

    def open_file_dialog(self):
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤
        dig.setFilter(QDir.Files)
        if dig.exec_():
            filenames = dig.selectedFiles()
            # 列表中的第一个元素即是文件路径，以只读的方式打开文件
            # f=open(filenames[0],'r')
            print("filenames:" + filenames[0])
            self.moveFileto(filenames[0], r'C:\Users\LKB\Desktop\history')
            self.close()

    def moveFileto(self, sourceDir, targetDir):
        shutil.copy(sourceDir, targetDir)

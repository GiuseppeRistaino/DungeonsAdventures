import sys
from PyQt4.QtGui import *
from Windows.MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())
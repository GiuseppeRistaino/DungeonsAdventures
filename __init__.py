import sys

from PyQt4.QtGui import *

from Windows.MainWindow import MainWindow
from Server.TCP_server import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())
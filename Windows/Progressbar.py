from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def __init__(self, Dialog, total=0):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 147)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(50, 60, 301, 23))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setMinimum(1)
        self.progressBar.setMaximum(total)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 241, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi(Dialog)
        Dialog.update()

    def update_progressbar(self, val):
        self.progressBar.setValue(val)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Caricamento in corso ...", None))
        self.label.setText(_translate("Dialog", "La tua Avventura e in fase di Caricamento ", None))




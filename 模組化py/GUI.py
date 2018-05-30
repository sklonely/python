import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class DemoImpl(QDialog):
    def __init__(self, *args):
        super(DemoImpl, self).__init__(*args)

        loadUi(sys.path[0] + '\demo.ui', self)

    @pyqtSlot()
    def on_button1_clicked(self):
        for s in "This is a demo".split(" "):
            self.list.addItem(s)


app = QApplication(sys.argv)
widget = DemoImpl()
widget.show()
sys.exit(app.exec_())

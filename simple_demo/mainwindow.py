# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_vars()
        self.connect_events()

    def init_vars(self):
        self.motore_on=QPixmap("img/button1.png")
        self.motore_off=QPixmap("img/button0.png")
        self.stato_motore=0

    def connect_events(self):
        self.ui.pulsante.clicked.connect(self.button_clicked)

    def button_clicked(self, *args):
        self.stato_motore=1-self.stato_motore
        print("motore=",self.stato_motore)
        if self.stato_motore==0:
            self.ui.motore.setPixmap(self.motore_off)
        else:
            self.ui.motore.setPixmap(self.motore_on)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

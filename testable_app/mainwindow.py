# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

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
        self.number=42
        self.ui.btnDec.clicked.connect(self.on_dec_clicked)
        self.ui.btnInc.clicked.connect(self.on_inc_clicked)

    # NOTE: bug introduced on purpose
    def on_dec_clicked(self):
        if self.number>0:
            self.number=-1
        self.updateButtonLabel()

    def on_inc_clicked(self):
        if self.number<100:
            self.number+=1
        self.updateButtonLabel()

    def updateButtonLabel(self):
        if self.number % 2 ==0 :
            self.ui.lbl_number.setStyleSheet("background-color: green")
        else:
            self.ui.lbl_number.setStyleSheet("background-color: red")
        self.ui.lbl_number.setText(str(self.number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

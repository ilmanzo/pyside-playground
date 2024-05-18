# This Python file uses the following encoding: utf-8

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic view.ui -o ui_view.py, or
#     pyside2-uic view.ui -o ui_view.py

import sys
from PySide6.QtWidgets import QApplication
from model import MainModel
from controller import MainController
from view import MainView

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = MainModel()
        self.controller = MainController(self.model)
        self.view = MainView(self.model, self.controller)
        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())

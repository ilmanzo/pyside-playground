# This Python file uses the following encoding: utf-8

# Important:
# You need to run the following command to generate the ui_form.py file
# source .qtcreator/Python_3_11_9venv/bin/activate
#     pyside6-uic view.ui -o ui_view.py, or
#     pyside2-uic view.ui -o ui_view.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from ui_view import Ui_MainWindow

class MainView(QMainWindow):
    def __init__(self, main_model, main_controller):
        super().__init__()

        self.model = main_model
        self.controller = main_controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect widgets to controller
        self.ui.spinBox_amount.valueChanged.connect(self.controller.change_amount)
        self.ui.pushButton_reset.clicked.connect(lambda: self.controller.change_amount(0))

        # listen for model event signals
        self.model.amount_sig.connect(self.slot_amount_changed)
        self.model.even_odd_sig.connect(self.slot_even_odd_changed)
        self.model.enable_reset_sig.connect(self.slot_enable_reset_changed)

        # set a default value
        self.controller.change_amount(42)

    @Slot(int)
    def slot_amount_changed(self, value):
        self.ui.spinBox_amount.setValue(value)

    @Slot(str)
    def slot_even_odd_changed(self, value):
        self.ui.label_even_odd.setText(value)

    @Slot(bool)
    def slot_enable_reset_changed(self, value):
        self.ui.pushButton_reset.setEnabled(value)
        if value:
            self.ui.pushButton_reset.setText("RESET")
        else:
            self.ui.pushButton_reset.setText("OK")


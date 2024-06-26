from PySide6.QtCore import QObject, Slot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @Slot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'dispari' if value % 2 else 'pari'

        # calculate button enabled state
        self._model.enable_reset = True if value else False

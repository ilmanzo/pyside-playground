from PySide6.QtCore import QObject, Signal

class MainModel(QObject):
    amount_sig = Signal(int)
    even_odd_sig = Signal(str)
    enable_reset_sig = Signal(bool)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_sig.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_sig.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_sig.emit(value)

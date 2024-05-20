# This Python file uses the following encoding: utf-8

import pytest
from pytestqt.qt_compat import qt_api
from mainwindow import MainWindow

@pytest.fixture
def widget(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)
    yield widget

def test_application_start(qtbot,widget):
    qtbot.addWidget(widget)
    assert widget.number == 42

def test_inc_button(qtbot,widget):
    # click in the + button and make sure it updates the numeric label
    qtbot.mouseClick(widget.ui.btnInc, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.ui.lbl_number.text()=="43"
    assert "background-color: red" in widget.ui.lbl_number.styleSheet();

def test_dec_button(qtbot,widget):
    # click in the - button and make sure it updates the numeric label
    qtbot.mouseClick(widget.ui.btnDec, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.ui.lbl_number.text()=="41"
    assert "background-color: red" in widget.ui.lbl_number.styleSheet();


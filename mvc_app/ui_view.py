# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(229, 182)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.spinBox_amount = QSpinBox(self.centralwidget)
        self.spinBox_amount.setObjectName(u"spinBox_amount")
        font = QFont()
        font.setPointSize(16)
        self.spinBox_amount.setFont(font)

        self.vboxLayout.addWidget(self.spinBox_amount)

        self.label_even_odd = QLabel(self.centralwidget)
        self.label_even_odd.setObjectName(u"label_even_odd")
        self.label_even_odd.setFont(font)

        self.vboxLayout.addWidget(self.label_even_odd)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setEnabled(False)
        self.pushButton_reset.setFont(font)

        self.vboxLayout.addWidget(self.pushButton_reset)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        pass
    # retranslateUi


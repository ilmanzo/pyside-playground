# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(257, 220)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_number = QLabel(self.centralwidget)
        self.lbl_number.setObjectName(u"lbl_number")
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.lbl_number.setFont(font)
        self.lbl_number.setStyleSheet(u"background-color: green")
        self.lbl_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_number)

        self.btnInc = QPushButton(self.centralwidget)
        self.btnInc.setObjectName(u"btnInc")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.btnInc.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnInc)

        self.btnDec = QPushButton(self.centralwidget)
        self.btnDec.setObjectName(u"btnDec")
        self.btnDec.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnDec)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CrappyCounter", None))
        self.lbl_number.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.btnInc.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.btnDec.setText(QCoreApplication.translate("MainWindow", u"-1", None))
    # retranslateUi


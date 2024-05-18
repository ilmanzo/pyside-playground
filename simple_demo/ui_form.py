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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pulsante = QPushButton(self.centralwidget)
        self.pulsante.setObjectName(u"pulsante")
        self.pulsante.setGeometry(QRect(100, 470, 151, 41))
        self.check = QCheckBox(self.centralwidget)
        self.check.setObjectName(u"check")
        self.check.setGeometry(QRect(280, 480, 92, 24))
        self.motore = QLabel(self.centralwidget)
        self.motore.setObjectName(u"motore")
        self.motore.setGeometry(QRect(110, 70, 571, 271))
        self.motore.setPixmap(QPixmap(u"img/button0.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuDEMO = QMenu(self.menubar)
        self.menuDEMO.setObjectName(u"menuDEMO")
        self.menuTAB2 = QMenu(self.menubar)
        self.menuTAB2.setObjectName(u"menuTAB2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDEMO.menuAction())
        self.menubar.addAction(self.menuTAB2.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pulsante.setText(QCoreApplication.translate("MainWindow", u"Struca", None))
        self.check.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.motore.setText("")
        self.menuDEMO.setTitle(QCoreApplication.translate("MainWindow", u"TAB1", None))
        self.menuTAB2.setTitle(QCoreApplication.translate("MainWindow", u"TAB2", None))
    # retranslateUi


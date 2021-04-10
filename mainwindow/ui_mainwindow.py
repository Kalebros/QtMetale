# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(926, 600)
        self.actionQuitar = QAction(MainWindow)
        self.actionQuitar.setObjectName(u"actionQuitar")
        self.actionConfiguracion = QAction(MainWindow)
        self.actionConfiguracion.setObjectName(u"actionConfiguracion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titlesListView = QListView(self.groupBox)
        self.titlesListView.setObjectName(u"titlesListView")

        self.verticalLayout.addWidget(self.titlesListView)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tituloLineEdit = QLineEdit(self.groupBox_2)
        self.tituloLineEdit.setObjectName(u"tituloLineEdit")

        self.gridLayout_2.addWidget(self.tituloLineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.grupoLineEdit = QLineEdit(self.groupBox_2)
        self.grupoLineEdit.setObjectName(u"grupoLineEdit")

        self.gridLayout_2.addWidget(self.grupoLineEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.yearLineEdit = QLineEdit(self.groupBox_2)
        self.yearLineEdit.setObjectName(u"yearLineEdit")

        self.gridLayout_2.addWidget(self.yearLineEdit, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_6)

        self.videoPlayerWidget = QVideoWidget(self.groupBox_2)
        self.videoPlayerWidget.setObjectName(u"videoPlayerWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.videoPlayerWidget.sizePolicy().hasHeightForWidth())
        self.videoPlayerWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.videoPlayerWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stopButton = QPushButton(self.groupBox_2)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout_2.addWidget(self.stopButton)

        self.pauseButton = QPushButton(self.groupBox_2)
        self.pauseButton.setObjectName(u"pauseButton")

        self.horizontalLayout_2.addWidget(self.pauseButton)

        self.playButton = QPushButton(self.groupBox_2)
        self.playButton.setObjectName(u"playButton")

        self.horizontalLayout_2.addWidget(self.playButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.groupBox_2)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionConfiguracion)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionQuitar)

        self.retranslateUi(MainWindow)
        self.actionQuitar.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuitar.setText(QCoreApplication.translate("MainWindow", u"Quitar", None))
#if QT_CONFIG(shortcut)
        self.actionQuitar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Canciones en la lista", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Canci\u00f3n seleccionada", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Grupo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Reproductor", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi


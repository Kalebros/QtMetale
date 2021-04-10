# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication,QMainWindow,QLineEdit,QDialog,QFileDialog
from PySide2.QtCore import QObject,Slot,SIGNAL,SLOT,QModelIndex,QByteArray
from PySide2.QtWidgets import QDataWidgetMapper,QHeaderView
from PySide2.QtCore import QSettings


from .ui_configdialog import Ui_Dialog

class ConfigDialog(QDialog):

    def __init__(self,parent = None):
        super().__init__(parent)

        self.settings = QSettings('LetterIngenieros','QtInformes')

        self.ui = Ui_Dialog()

        self.ui.setupUi(self)

        self.setupUi()
    
    def setupUi(self):

        self.ui.fileLineEdit.setText(self.settings.value('configFile'))

        self.ui.selectFileButton.clicked.connect(self.changeConfigFile)
    
    @Slot()
    def changeConfigFile(self):

        fileName = QFileDialog.getOpenFileName(
            self,
            'Archivo de configuracion', None, 'Archivos YAML (*.yml *.yaml)'
        )

        fileName = fileName[0]
        if (fileName is not None) and (fileName != ''):
            self.settings.setValue('configFile',fileName)
            self.ui.fileLineEdit.setText(fileName)
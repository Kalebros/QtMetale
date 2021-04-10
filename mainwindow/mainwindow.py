# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication,QMainWindow,QLineEdit
from PySide2.QtCore import QObject,Slot,SIGNAL,SLOT,QModelIndex,QByteArray,QSettings
from PySide2.QtWidgets import QDataWidgetMapper,QHeaderView

from .ui_mainwindow import Ui_MainWindow

from yamltitles import Title,Group,Disco

from models.yamltitles import TitleListModel,TitlesTableModel

from player.youtubeplayer import YoutubePlayer

from configdialog import ConfigDialog
import os


class MainWindow(QMainWindow):
    def __init__(self, startWithConfig: None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.__titleModel = None
        self.__dataMapper = None
        self.__ytPlayer = None

        self.__previousConfigFile = None

        self.__settings = QSettings('TallerQt','QtMetale')

        #Comprobar si el settings esta cargado o no

        if startWithConfig is not None:
            self.__settings.setValue('configFile',startWithConfig)

        if self.__settings.value('configFile') is None:
            CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

            PATH_TO_FILE = os.path.join(CURRENT_DIR,'../config.yaml')
            self.__settings.setValue('configFile',PATH_TO_FILE )

        self.__previousConfigFile = self.__settings.value('configFile')
        self.dialogoConfiguracion = None
        self.dialogoInforme = None

        self.ui.setupUi(self)

        self.__ytPlayer = YoutubePlayer(widgetToPlay=self.ui.videoPlayerWidget)

        self.prepareModels()
        self.setupUi()
    
    def setupUi(self):
    
        self.__dataMapper = QDataWidgetMapper(self)

        self.__dataMapper.setModel(self.__titleModel)

        propertyText = QByteArray(b'text')
        self.__dataMapper.addMapping(self.ui.tituloLineEdit,0,propertyText)
        self.__dataMapper.addMapping(self.ui.grupoLineEdit,1,propertyText)
        self.__dataMapper.addMapping(self.ui.yearLineEdit,2,propertyText)

        QObject.connect(
            self.ui.titlesListView.selectionModel(),
            SIGNAL('currentRowChanged(QModelIndex,QModelIndex)'),
            self,
            SLOT('changeSelectedTitle(QModelIndex,QModelIndex)'))
        
        #Dialogo de configuracion

        self.dialogoConfiguracion = ConfigDialog(self)

        self.ui.actionConfiguracion.triggered.connect(self.dialogoConfiguracion.open)

        self.dialogoConfiguracion.finished.connect(self.reloadModelos)

        self.ui.playButton.clicked.connect(self.launchCurrentVideo)
        self.ui.stopButton.clicked.connect(self.__ytPlayer.stopVideo)
        self.ui.pauseButton.clicked.connect(self.__ytPlayer.pauseVideo)
    
    def launchCurrentVideo(self):

        self.__ytPlayer.playVideo(self.__dataMapper.currentIndex())
    
    def prepareModels(self):

        list_titles = Title.readFromYAML(self.__settings.value('configFile'))

        self.__titleModel = TitlesTableModel(self,list_titles)

        self.ui.titlesListView.setModel(self.__titleModel)
        self.ui.titlesListView.setModelColumn(0)

        self.__ytPlayer.resetPlayList(list_titles)
    
    @Slot()
    def changeSelectedTitle(self,current: QModelIndex,previous: QModelIndex):
        self.__dataMapper.setCurrentIndex(current.row())

    
    @Slot()
    def reloadModelos(self,result):

        currentConfigFile = self.__settings.value('configFile')
        if currentConfigFile != self.__previousConfigFile:

            list_titles = Title.readFromYAML(self.__settings.value('configFile'))
            self.__titleModel.titles = list_titles
            self.__previousConfigFile = self.__settings.value('configFile')


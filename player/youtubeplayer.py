# -*- coding: utf-8 -*-

from PySide2.QtCore import QObject,Signal,Slot,QUrl

from PySide2.QtWidgets import QWidget

from PySide2.QtMultimedia import QMediaPlayer,QMediaPlaylist,QMediaContent
from PySide2.QtMultimediaWidgets import QVideoWidget

from yamltitles import Title

from typing import List
import pafy

class YoutubePlayer(QObject):

    titlesListChanged = Signal(list)

    def __init__(self, titles: List[Title] = [],widgetToPlay: QVideoWidget=None):
        QObject.__init__(self)

        self.__titles = titles
        self.__playlist = QMediaPlaylist(self)
        self.__player = QMediaPlayer(self)
        self.__videoWidget = widgetToPlay
        self.__player.setVideoOutput(self.__videoWidget)


        self.titlesListChanged.connect(self.resetPlayList)

    
    @property
    def titles(self):
        return self.__titles
    
    @titles.setter
    def titles(self,value):
        self.__titles = value
        self.titlesListChanged.emit(self.__titles)
    
    @Slot()
    def setTitles(self,titles: List[Title]):

        self.__titles = titles
        self.titlesListChanged.emit(self.__titles)
    
    @Slot()
    def resetPlayList(self,list_of_titles: List[Title]):
        self.__playlist.clear()

        for t in list_of_titles:
            url = t.link
            video = pafy.new(url)
            best = video.getbest()

            self.__playlist.addMedia(QMediaContent(QUrl(best.url)))
        
        self.__playlist.setCurrentIndex(0)
        self.__player.setPlaylist(self.__playlist)
    
    @Slot()
    def playVideo(self,index: int):

        self.__playlist.setCurrentIndex(index)
        self.__player.play()

    @Slot()
    def stopVideo(self):

        self.__player.stop()
    
    @Slot()
    def pauseVideo(self):
        if self.__player.state() == QMediaPlayer.PlayingState:
            self.__player.pause()
        else:
            self.__player.play()
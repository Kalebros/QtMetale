# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt,QAbstractListModel,QModelIndex

from yamltitles import Title,Group,Disco

from typing import List

class TitleListModel(QAbstractListModel):

    def __init__(self, parent,lista_titles = None):
        super().__init__(parent)

        self.__titles: List[Title] = lista_titles
    
    @property
    def titles(self):
        return self.__titles
    
    @titles.setter
    def titles(self,value: List[Title]):
        self.beginResetModel()
        self.__titles = value
        self.endResetModel()
    
    def rowCount(self,parent = QModelIndex()):
        return len(self.__titles)
    
    def data(self,index: QModelIndex,role = Qt.DisplayRole):

        if index.row() > len(self.__titles):
            return None
                        
        if (role == Qt.DisplayRole) or (role == Qt.EditRole):
            return self.__titles[index.row()].titulo
        
        return None
    

    def groupFromIndex(self, index: QModelIndex):

        if index.row() > len(self.__titles):
            return None
        
        return self.__titles[index.row()].grupo

    def discoFromIndex(self, index: QModelIndex):

        if index.row() > len(self.__titles):
            return None
        
        return self.__titles[index.row()].disco
# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt,QAbstractTableModel,QModelIndex

from yamltitles import Title,Group,Disco

from typing import List

class TitlesTableModel(QAbstractTableModel):

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
    
    def columnCount(self,parent = QModelIndex()):
        return 4 
    
    def flags(self,index: QModelIndex):

        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def setData(self,index,value,role=Qt.EditRole):

        if index.row() > len(self.__titles):
            return False
        t = self.__titles[index.row()]

        if index.column() == 0:
            t.titulo = value
        if index.column() == 1:
            t.grupo.nombre = value
        if index.column() == 2:
            t.year = value
        if index.column() == 3:
            t.link = value
        
        self.dataChanged.emit(index,index)

        return True

    def data(self,index: QModelIndex,role = Qt.DisplayRole):

        if index.row() > len(self.__titles):
            return None
        
        data = None
        if (role == Qt.DisplayRole) or (role == Qt.EditRole):

            t = self.__titles[index.row()]
            if index.column() == 0:
                data = t.titulo
            if index.column() == 1:
                data = t.grupo.nombre
            if index.column() == 2:
                data = t.year
            if index.column() == 3:
                data = t.link

        return data

    def groupFromIndex(self, index: QModelIndex):

        if index.row() > len(self.__titles):
            return None
        
        return self.__titles[index.row()].grupo
    
    def discoFromIndex(self, index: QModelIndex):

        if index.row() > len(self.__titles):
            return None
        
        return self.__titles[index.row()].disco
# -*- coding: utf-8 -*-

from typing import List,Dict

from pydantic import BaseModel
from .group import Group
from .disco import Disco

from yaml import load,dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader,Dumper

from copy import copy

class Title(BaseModel):

    titulo: str
    year: str
    link: str
    grupo: Group
    disco: Disco

    @staticmethod
    def readFromYAML(yamlFile: str):

        dataYAML = None
        with open(yamlFile,'r') as origen:
            dataYAML = load(origen,Loader=Loader)
        
        list_of_titles = dataYAML.get('titles',[])

        result = list()
        for t in list_of_titles:
            grupo = t.get('grupo')

            title = copy(t)
            title.pop('grupo')
            title['grupo'] = Group(**grupo)

            disco = t.get('disco')
            title.pop('disco')
            title['disco'] = Disco(**disco)

            result.append(Title(**title))
        
        return result
    
    @staticmethod
    def saveToYAML(yamlFile: str, list_titles: List):

        with open(yamlFile,'w') as destino:
            dump({'titles': [t.dict() for t in list_titles]},destino)
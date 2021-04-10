# -*- coding: utf-8 -*-

from typing import List,Dict

from pydantic import BaseModel

from typing import List

class Group(BaseModel):

    nombre: str
    fundacion: int
    componentes: List[str] = []
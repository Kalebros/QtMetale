# -*- coding: utf-8 -*-

from typing import List,Dict

from pydantic import BaseModel

from typing import List

class Disco(BaseModel):

    nombre: str
    release: int
    tracks: List[str] = []
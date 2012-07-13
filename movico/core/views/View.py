# -*- coding: utf-8 -*-
import BaseObject

class View(BaseObject):
    """Base View Class for all Views"""

    name = ""

    def __init__(self, name):
        self.name = name

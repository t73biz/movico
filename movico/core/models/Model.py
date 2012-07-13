# -*- coding: utf-8 -*-
class Model():
    """Base Model Class for all Models"""

    def __init__(self):
       pass

    def find(self, type):
        if type == 'all':
            print('You Found it All!')
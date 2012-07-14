# -*- coding: utf-8 -*-
from core.controllers.Controller import Controller
from core.views.View import View

__author__ = 'Ron Chaplin'

class PageController(Controller):
    """
    Default Page Controller
    """

    def display(self, page):
        v = View()
        return v.render(self.layout, page + '.pytpl')
        
# -*- coding: utf-8 -*-
from core.controllers.Controller import Controller


__author__ = 'Ron Chaplin'

class PostController(Controller):
    """
    Post Controller for Blog Example
    """

    uses = ["PostModel"]

    def __init__(self, uses = None):
        if uses != None:
            self.uses = uses

        self._parseUses(self.uses)

    def test(self):
        self.postmodel.find('all')
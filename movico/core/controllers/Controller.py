# -*- coding: utf-8 -*-
import importlib

class Controller():
    """
        Base Controller Class for all Controllers
    """
    uses = []

    def __init__(self):
        pass

    def _parseUses(self, uses):
        for model in self.uses:
            try:
                _tmp = importlib.import_module('application.models.%s' % model)
                setattr(self.__class__, str.lower(model), getattr(_tmp, model)())
            except ImportError:
                print('Can not find model %s' % model)

    def add(self):
        """
        Create action
        """
        pass

    def delete(self, id):
        """
        Delete action
        """
        pass

    def edit(self, id):
        """
        Update action
        """
        pass

    def index(self):
        """
        Read action -- all
        """
        pass

    def view(self, id):
        """
        Read action -- id specific
        """
        pass
# -*- coding: utf-8 -*-
from core.views import Pyratemp
import application.config.config as cfg

class View():
    """Base View Class for all Views"""

    def render(self, layout, view):
        """
        Render method for pages.
        """
                
        viewTemplate = Pyratemp.Template(filename=view, filepath=cfg.APP_ROOT + '/views/pages/')
        viewResult = viewTemplate()
        
        layoutTemplate = Pyratemp.Template(filename=layout, filepath=cfg.APP_ROOT + '/views/layouts/')
        layoutResult = layoutTemplate(content_for_layout=viewResult)
        
        return layoutResult
# -*- coding: utf-8 -*-
from core.itty import *

@get('/')
@get('/home')
def index(request):
    from application.controllers.PageController import PageController
    page = PageController()
    content = page.display('home')
    return content
    
run_itty()

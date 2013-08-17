# -*- coding: utf-8 -*-
"""
 website - Dev Microsystem S.A.S

 Copyright (c) 2013, Jorge A. Toro <jolthgs@gmail.com>
 All Rights Reserved.

"""
import web
from urls import urls
from view import render


class index:
    def GET (self):
        return render.base(render.index())

class contact:
    def GET (self):
        #return render.base("Contact Us", "Contáctenos")
        return render.base(render.contact("Contáctenos"), "Contáctenos")


if __name__ == "__main__":
    app = web.application(urls, globals())
    #app.internalerror = web.debugerror
    app.run()

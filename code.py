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
    def GET(self):
        return render.base(render.index())


if __name__ == "__main__":
    app = web.application(urls, globals())
    #app.internalerror = web.debugerror
    app.run()

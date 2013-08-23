# -*- coding: utf-8 -*-
"""
 website - Dev Microsystem S.A.S

 Copyright (c) 2013, Jorge A. Toro <jolthgs@gmail.com>
 All Rights Reserved.

"""
import web
from urls import urls
import view
from view import render, menu

#app = web.application(urls, globals())

#render = web.template.render("templates")
    
# Custom NotFound message
def notfound():
    #return web.notfound("Lo sentimos, la página que buscas no se ha encontrado.")
    return web.notfound(render.notfound())

#app.notfound = notfound


class index:
    def GET (self):
        #print web.ctx.path
        #return render.base(render.index())
        #return render.base(menu(iweb.ctx.path), render.index())
        return render.base(menu, web.ctx.path, render.index())

class contact:
    def GET (self):
        #return render.base("Contact Us", "Contáctenos")
        #print web.ctx.path
        #return render.base(menu(), render.contact("Contáctenos"), "Contáctenos")

        #return render.base(menu, web.ctx.path, render.contact("Contáctenos"), "Contáctenos")
        return render.base(menu, web.ctx.path, render.contact(view.listCountries()))


if __name__ == "__main__":
    app = web.application(urls, globals())
    #app.internalerror = web.debugerror
    app.notfound = notfound
    app.run()

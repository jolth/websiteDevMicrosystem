# -*- coding: utf-8 -*-
import web
import config

render = web.template.render("templates/")
#render = web.template.render("templates/", cache=config.cache)

def menu ():
    """
        Menu principal 
    """
    items = [
        ("Home","/",1),
        ("Soluciones","/solutions",2),
        ("Servicios","/services",3),
        ("Productos","/products",4),
        #"Conocimiento":"",
        ("Formación","/training",5),
        #("Sobre Dev","/about",6),
        ("Dev","/about",6),
        ("Contáctenos","/contact",7)
    ]
    return sorted(items, key=lambda item: item[2]) # sort by num

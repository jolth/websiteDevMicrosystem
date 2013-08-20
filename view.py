# -*- coding: utf-8 -*-
import web

render = web.template.render("templates/")


#def menu (item=None):
def menu ():
    #items = {
    #    "Home":"/",
    #    "Soluciones":"/solutions",
    #    "Servicios":"/services",
    #    "Productos":"/products",
        #"Conocimiento":"",
        #"Formación":"/training",
    #    "Formacion":"/training",
    #    "Sobre Dev":"/about",
        #"Contáctenos":"/contact"
    #    "Contactenos":"/contact"
    #}
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
    #return items
    return sorted(items, key=lambda item: item[2]) # sort by num

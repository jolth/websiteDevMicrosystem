# -*- coding: utf-8 -*-
import web
#import config
#import db
from config import db

render = web.template.render("templates/")
#render = web.template.render("templates/", cache=config.cache)

def menu():
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


def topic():
    """
        Temas del formulario de Contacto 
    """
    temas = (
        "",
        "",
    )
    return temas

        
def listCountries(**k):
    """
        Lista los paises.

        >>> from view import listCountries
        >>> listCountries()
        0.0 (1): SELECT * FROM countries
        <web.utils.IterBetter instance at 0x7f6490d9d440>
        >>> for i in listCountries():
        ...     print i.name
        ... 
        0.0 (2): SELECT * FROM countries
        afganistan
        albania
        alemania
        ...
        >>>

    """
    return db.select("countries", **k)

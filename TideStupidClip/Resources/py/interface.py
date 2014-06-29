# -*- coding: latin-1 -*-
"""Este archivo define los metodos expuestos del back-end."""

o = None

def update():
    """Revisa las tareas y las agrega a la lista de mensajes."""
    o.update()


def cmd(s):
    """Parsea s, ejecuta la orden especificada, y agrega su
    resultado en la lista de mensajes. Devuelve True si encuentra una accion."""
    try:
        return o.execute_command(s)
    except Exception, e:
        import traceback
        tb = traceback.format_exc()
        print "Stacktrace: " + tb
        print "Error :" + e.message
        return False


def get_new_msg():
    """Devuelve los mensajes marcados como no enviados, y
    marca todos los que envia como marcados."""
    return o.get_new_messages ()


def get_all_msg(n = None):
    """Devuelve los ultimos n mensajes en la lista, si n no esta
    especificado (o es None), devuelve todos."""
    return o.get_all_messages (n)

def options_get(key):
    """Devuelve el valor de la opcion con clave especificada."""
    return o.options_get(key)

def options_set(key, value):
    """Asigna value a la opcion con la clave especificada."""
    o.options_set(key,value)

def profile_get(key):
    """Devuelve el valor del campo de perfil con la clave especificada."""
    return o.profile_get(key)

def profile_set(key, value):
    """Asigna value al campo de perfil con la clave especificada."""
    o.profile_set(key,value)


def init(dir):
    """Informa que la aplicacion ha iniciado."""
    from main import MainClass
    global o
    o = MainClass(dir)

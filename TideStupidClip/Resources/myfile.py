# -*- coding: latin-1 -*-
counter = 122


def testPython():
    global counter
    counter += 1
    return counter


def transformString(s):
    s = s.replace('ñ', 'Ñ')
    return s.upper()

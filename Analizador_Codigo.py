import ply.lex as lex
import codecs
import os
import sys
import re

tokens = ['tok','tok']

palreservadas = {
    '':'',
    '':''
}

tokens = tokens + list(palreservadas.values())

t_ignore = ''

t_token = r'expresion reg'


dir = input("Nombre del archivo: ")
f = open(dir, "r")
while(True):
    linea = f.readline()
    print(linea)

    if not linea:
        break
f.close()
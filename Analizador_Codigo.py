import re
dir = input("Nombre del archivo: ")
f = open(dir, "r")
while(True):
    linea = f.readline()
    print(linea)

    if not linea:
        break
f.close()
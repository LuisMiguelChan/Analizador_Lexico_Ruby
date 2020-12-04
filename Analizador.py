import sys
from lexer import lexer

if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name, "r")
    data = f.read()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print ("Token --> ", tok)
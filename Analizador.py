import sys
from lexer import lexer
n=0
if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name, "r")
    data = f.read()
    lexer.input(data)

    while True:
        n=n+1
        tok = lexer.token()
        if not tok:
            break
        print ("Token ",n," --> ", tok)
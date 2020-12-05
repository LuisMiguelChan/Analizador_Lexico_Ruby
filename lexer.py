import ply.lex as lex

tokens = ['VARIABLE','EQUALS','SUMAR','RESTAR','MULTIPLICAR','DIVIDIR','NUMBER','COMMA',
'RPARENT','LPARENT','COMILLA','STRING','MENOR_QUE']

palreservadas = {
    'end':'END',
    'print':'PRINT',
    'puts':'PUTS',
    'if':'IF',
    'else':'ELSE'
}

tokens = tokens + list(palreservadas.values())

t_ignore = '\t'

t_EQUALS = r'\='
t_RESTAR = r'\-'
t_SUMAR = r'\+'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'\/'
t_COMMA = r'\,'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMILLA = r'\"'
t_MENOR_QUE = r'<'

def t_END(t):
    r'end'
    return t
def t_VARIABLE(t):
    r'[x][^\w]|[y][^\w]|sum[^\w]|res[^\w]|div[^\w]|mult[^\w]'
    return t
def t_PRINT(t):
    r'print'
    return t
def t_PUTS(t):
    r'puts'
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_espacio(t):
    r"\s"
    pass
def t_STRING(t):
    r'\w|:'
    return t

lexer = lex.lex()
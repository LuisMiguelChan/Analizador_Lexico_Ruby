import ply.lex as lex

tokens = ['SUMAR','RESTAR']

palreservadas = {
    'end':'END',
    'def':'DEF'
}

tokens = tokens + list(palreservadas.values())

t_ignore = '\t'

t_SUMAR = r'\+'

t_RESTAR = r'\-'

def t_END(t):
    r'end'
    return t

def t_DEF(t):
    r'def'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
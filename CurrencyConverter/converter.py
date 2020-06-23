from ply import lex
from CurrencyConverter.models import Cube

import ply.yacc as yacc

def t_SEPARATOR(t):
    r'en'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    # a better regex taking exponents into account:
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'    
    t.value = float(t.value)
    return t

def t_CURRENCY(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_error(t):
    # anything that gets past the other filters
    print("Illegal character '%s'" % t.value[0])

    # skip forward a character
    t.lexer.skip(1)

def p_expression(p):
    '''
    expression : FLOAT CURRENCY SEPARATOR CURRENCY
    '''
    try:
        c = Cube.objects.get(currency=p[4])
    except Cube.DoesNotExist:
        return None
    p[0] = "%.2f" % (p[1] * c.rate)
    return p

def p_error(p):
    print("Syntax error at '%s'" % p.value)

def convert(req):
    tokens = ('FLOAT', 'CURRENCY', 'SEPARATOR')
    t_ignore = ' \t'
    lexer = lex.lex()

    parser = yacc.yacc()
    response = parser.parse(req)
    if response is None:
        response = "I' sorry Dave. I'm afraid. I can't do that"
    return { "answer": response }
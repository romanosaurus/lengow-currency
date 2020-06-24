from ply import lex


class MyLexer(object):
    tokens = ('FLOAT', 'CURRENCY', 'SEPARATOR', 'INTEGER')
    t_ignore = ' \t'

    # Handles the 'en' separator
    def t_SEPARATOR(self, t):
        r"""en"""
        return t

    # Handles the conversion of float number
    def t_FLOAT(self, t):
        r"""
        (\d*\.\d+)|(\d+\.\d*)
        """
        t.value = float(t.value)
        return t

    # Handles the conversion of integer number
    def t_INTEGER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Handles the currency conversion
    def t_CURRENCY(self, t):
        r"""
        [a-zA-Z_][a-zA-Z_0-9]*
        """
        return t

    def t_error(self, t):
        # anything that gets past the other filters
        print("Illegal character '%s'" % t.value[0])

        # skip forward a character
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

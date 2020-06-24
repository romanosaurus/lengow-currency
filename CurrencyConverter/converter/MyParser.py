import ply.yacc as yacc

from CurrencyConverter.models import Cube
from CurrencyConverter.converter.MyLexer import MyLexer


class MyParser(object):
    tokens = MyLexer.tokens

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self)

    # Handle parsing logic
    def p_expression(self, p):
        """
        expression : FLOAT CURRENCY SEPARATOR CURRENCY
                   | INTEGER CURRENCY SEPARATOR CURRENCY
        """
        try:
            c = Cube.objects.get(currency=p[4])
        except Cube.DoesNotExist:
            return None
        p[0] = "%.2f" % (p[1] * c.rate)
        return p

    # Handle parsing error
    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)

    # Call parser to convert the current currency to the wanted currency
    def convert(self, request):
        response = self.parser.parse(request)
        if response is None:
            response = "I' sorry Dave. I'm afraid. I can't do that"
        return {"answer": response}

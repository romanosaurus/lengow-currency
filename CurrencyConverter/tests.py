from django.test import TestCase
from CurrencyConverter.models import Cube
from CurrencyConverter.converter.MyParser import MyParser


# Create your tests here.
class ConverterTest(TestCase):
    def setUp(self):
        self.parser = MyParser()
        Cube.objects.create(currency="USD", rate=1.32)

    def test_integer_conversion(self):
        res = "%.2f" % (10 * 1.32)
        self.assertEqual(res, self.parser.convert("10 EUR en USD")['answer'])

    def test_float_conversion(self):
        res = "%.2f" % (10.32 * 1.32)
        self.assertEqual(res, self.parser.convert("10.32 EUR en USD")['answer'])

    def test_error_conversion(self):
        self.assertEqual("I' sorry Dave. I'm afraid. I can't do that", self.parser.convert("test EUR en USD")['answer'])

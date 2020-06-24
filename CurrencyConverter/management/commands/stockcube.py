import requests

from xml.etree import ElementTree
from django.core.management.base import BaseCommand, CommandError
from CurrencyConverter.models import Cube


class Command(BaseCommand):
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
    help = 'Stock the current EUR conversions from this URL: ' + url

    @staticmethod
    def __get_cube_list(tree):
        for elem in tree:
            if 'Cube' in elem.tag:
                return elem[0]
        return None

    def handle(self, *args, **options):
        response = requests.get(self.url).content
        tree = ElementTree.fromstring(response)
        cube_list = self.__get_cube_list(tree)

        if cube_list is None:
            raise CommandError('No cube available')

        for cube in cube_list:
            c, created = Cube.objects.update_or_create(
                            currency=cube.attrib['currency'],
                            rate=cube.attrib['rate'],
                            defaults={'currency': cube.attrib['currency']}
                        )
            c.save()

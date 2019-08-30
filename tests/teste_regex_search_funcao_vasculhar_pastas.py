from unittest import TestCase
from regex_search.regex_search import vasculhar_pastas
from typing import Generator


class Testes(TestCase):
    def setUp(self):
        self.args = ('def|class', 'tests')

    def test_retornando_um_gerador(self):
        resultado = vasculhar_pastas(*self.args)
        self.assertIsInstance(resultado, Generator)

    def test_retornando_essa_classe(self):
        resultado = vasculhar_pastas(*self.args)
        esperado = '\x1b[38;5;208mclass\x1b[0m Testes(TestCase):\n'
        next(resultado)
        self.assertIn(esperado, next(resultado))

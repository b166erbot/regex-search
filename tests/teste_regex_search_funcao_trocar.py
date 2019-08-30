from unittest import TestCase
from unittest.mock import MagicMock

from regex_search.regex_search import trocar


class Testes(TestCase):
    def setUp(self):
        self.args = [MagicMock()]
        self.args[0].groups.return_value = ('oi', 'ola')
        self.args[0].group.return_value = ('oi',)

    def test_grupos_retornando_uma_string(self):
        self.args[0].group.return_value = ''
        resultado = trocar(*self.args)
        self.assertIsInstance(resultado, str)

    def test_grupo_retornando_uma_string(self):
        self.args[0].groups.return_value = ''
        resultado = trocar(*self.args)
        self.assertIsInstance(resultado, str)

    def test_se_nada_capturado_retornando_none(self):
        self.args[0].group.return_value = ''
        self.args[0].groups.return_value = tuple()
        resultado = trocar(*self.args)
        self.assertIs(resultado, None)


    def test_grupos_retornando_string_colorida(self):
        self.args[0].groups.return_value = ('a',)
        resultado = trocar(*self.args)
        self.assertEqual(resultado, '\x1b[38;5;208ma\x1b[0m')

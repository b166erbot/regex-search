from unittest import TestCase
from unittest.mock import MagicMock, patch
from typing import Generator

from regex_search.regex_search import procurarNoArquivo


class Testes(TestCase):
    def setUp(self):
        self.args = [r'teste_retornando',
                     'tests/teste_regex_search_funcao_procurar_no_arquivo.py']
        self.mocks = [MagicMock(), MagicMock()]

    def test_retornando_esse_metodo(self):
        regex = 'test_retornando_esse_metodo'
        resultado = next(procurarNoArquivo(regex, self.args[1]))
        esperado = ('    def \x1b[38;5;208mtest_retornando_esse_metodo\x1b['
                    '0m(self):\n')
        self.assertIn(esperado, resultado)

    @patch('regex_search.regex_search.open')
    def test_erro_ao_abrir_arquivo_com_unicode_decode_error(self, open):
        open.side_effect = UnicodeDecodeError('', b'', 1, 2, '')
        resultado = procurarNoArquivo(*self.mocks)
        self.assertIsInstance(resultado, Generator)

    def test_retornando_um_generator(self, ):
        resultado = procurarNoArquivo(*self.args)
        self.assertIsInstance(resultado, Generator)

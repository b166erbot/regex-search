from unittest import TestCase
from unittest.mock import patch, MagicMock
from regex_search.regex_search import procurarNoArquivo
from types import GeneratorType


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
        self.assertEqual(resultado, esperado)

    @patch('regex_search.regex_search.open')
    def test_erro_ao_abrir_arquivo_com_unicode_diferente_de_utf8(self, open):
        open.side_effect = UnicodeDecodeError('', b'', 1, 2, '')
        resultado = procurarNoArquivo(*self.mocks)
        self.assertIs(resultado, None)

    def test_retornando_um_generator(self, ):
        resultado = procurarNoArquivo(*self.args)
        self.assertIsInstance(resultado, GeneratorType)

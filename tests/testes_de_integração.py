from unittest import TestCase

from click.testing import CliRunner

from regex_search.regex_search import main


class Testes(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()
        cls.maxDiff = None
        cls.arquivo = 'tests/testes_de_integração.py'

    def test_texto_com_pipe(self):
        resultado = self.runner.invoke(main, ['oi|ola', 'oiolaoi'])
        self.assertEqual('oiolaoi\n', resultado.output)

    def test_procurando_esse_metodo_com_flag_recursivo(self):
        esperado = '    def test_recursivo_procurando_esse_metodo(self):'
        resultado = self.runner.invoke(main, ['-r', 'recursivo', '.'])
        self.assertIn(esperado, resultado.output)

    def test_procurando_esse_metodo_sem_flag_recursivo(self):
        esperado = ('    def test_procurando_esse_metodo_sem_flag_recursivo'
                    '(self):')
        resultado = self.runner.invoke(main, ['recursivo', self.arquivo])
        self.assertIn(esperado, resultado.output)

    def test_procurando_esse_modulo_com_flags_recursivo_e_so_nomes(self):
        esperado = ('    def test_procurando_esse_modulo_com_flags_recursivo_'
                    'e_so_nomes(self):')
        resultado = self.runner.invoke(main, ['-rs', 'recursivo', self.arquivo])
        self.assertIn(esperado, resultado.output)

    def test_procurando_esse_metodo_com_flag_so_nomes(self):
        resultado = self.runner.invoke(main, ['-s', 'recursivo', self.arquivo])

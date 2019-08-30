from unittest import TestCase
from click.testing import CliRunner
from regex_search.regex_search import main


class Testes(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.runner = CliRunner()
        self.maxDiff = None

    def test_texto_com_pipe(self):
        resultado = self.runner.invoke(main, ['oi|ola', 'oiolaoi'])
        self.assertEqual('oiolaoi\n', resultado.output)

    def test_com_flag_recursivo_procurando_esse_metodo(self):
        esperado = '    def test_recursivo_procurando_esse_metodo(self):'
        resultado = self.runner.invoke(main, ['-r', 'recursivo', '.'])
        self.assertIn(esperado, resultado.output)

    def test_procurando_esse_metodo_sem_flag_recursivo(self):
        esperado = ('    def test_procurando_esse_metodo_sem_flag_recursivo'
                    '(self):')
        arquivo = 'tests/testes_de_sistema.py'
        resultado = self.runner.invoke(main, ['recursivo', arquivo])
        self.assertIn(esperado, resultado.output)

from unittest import TestCase
from regex_search.regex_search import procurar
from types import GeneratorType
from colored import fg, attr
from itertools import cycle


class Testes(TestCase):
    def test_retornando_generator_caso_inserido_texto(self):
        resultado = procurar('a', 'a')
        self.assertIsInstance(resultado, GeneratorType)

    def test_retornando_generator_caso_inserido_generator(self):
        resultado = procurar('a', (x for x in 'aba'))
        self.assertIsInstance(resultado, GeneratorType)

    def test_retornando_toda_a_string_caso_regex_vazio(self):
        resultado = next(procurar('', 'oi'))
        self.assertEqual(resultado, 'oi')

    def test_retornando_erro_caso_texto_vazio(self):
        with self.assertRaises(StopIteration):
            resultado = next(procurar('oi', ''))

    def test_retornando_toda_a_string_caso_texto_e_regex_estiverem_vazios(self):
        resultado = next(procurar('', ''))
        self.assertEqual(resultado, '')

    def test_retornando_texto_laranja_caso_usando_pipe_no_regex(self):
        resultado = next(procurar('oi|ola', 'oiteste testeola oi'))
        esperado = ('\x1b[38;5;208moi\x1b[0mteste teste\x1b[38;5;208mola\x1b[0m'
                    ' \x1b[38;5;208moi\x1b[0m')
        self.assertEqual(resultado, esperado)

    def test_retornando_as_10_cores_caso_usando_grupos(self):
        regex = '(a)|(b)|(c)|(d)|(e)|(f)|(g)|(h)|(i)|(j)'
        resultado = next(procurar(regex, 'abcdefghij'))
        esperado = ('\x1b[38;5;208ma\x1b[0m\x1b[38;5;2mb\x1b[0m\x1b[38;5;1m'
                    'c\x1b[0m\x1b[38;5;4md\x1b[0m\x1b[38;5;3me\x1b[0m\x1b[38;5'
                    ';54mf\x1b[0m\x1b[38;5;6mg\x1b[0m\x1b[38;5;5mh\x1b[0m'
                    '\x1b[38;5;198mi\x1b[0m\x1b[38;5;173mj\x1b[0m')
        self.assertEqual(resultado, esperado)

    def test_cores_reiniciando_caso_ultrapasse_o_tamanho_de_10(self):
        regex = '(a)|(b)|(c)|(d)|(e)|(f)|(g)|(h)|(i)|(j)|(k)'
        resultado = next(procurar(regex, 'abcdefghijk'))
        esperado = ('\x1b[38;5;208ma\x1b[0m\x1b[38;5;2mb\x1b[0m\x1b[38;5;1m'
                    'c\x1b[0m\x1b[38;5;4md\x1b[0m\x1b[38;5;3me\x1b[0m\x1b[38;'
                    '5;54mf\x1b[0m\x1b[38;5;6mg\x1b[0m\x1b[38;5;5mh\x1b[0m\x1b'
                    '[38;5;198mi\x1b[0m\x1b[38;5;173mj\x1b[0m\x1b[38;5;208mk'
                    '\x1b[0m')
        self.assertEqual(resultado, esperado)

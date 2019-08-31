# from types import GeneratorType as Gen
from itertools import chain, cycle, dropwhile
from os import walk
from os.path import exists, isdir, isfile, join
from re import M, search, sub
from typing import Generator, Tuple, Union

from click import STRING, argument, command, echo, option
from colored import attr, fg

ajuda_opcao = ('Vasculha por todos os arquivos contidos'
                         ' dentro da [local/]pasta passada.')
ajuda_opcao2 = ('Mostra somente os nomes dos arquivos')
forma = '{}{{}}{}'
cores = [
    forma.format(fg('dark_orange'), attr(0)),
    forma.format(fg('green'), attr(0)),
    forma.format(fg('red'), attr(0)),
    forma.format(fg('blue'), attr(0)),
    forma.format(fg('yellow'), attr(0)),
    forma.format(fg('purple_4a'), attr(0)),
    forma.format(fg('cyan'), attr(0)),
    forma.format(fg('magenta'), attr(0)),
    forma.format(fg('deep_pink_1a'), attr(0)),
    forma.format(fg('light_salmon_3b'), attr(0)),
]


@command()
@argument('regex', type=STRING)
@argument('texto_arquivo', type=STRING)
@option('-r', '--recursivo', default=False, is_flag=True, help=ajuda_opcao)
@option('-s', '--so_nomes', default=False, is_flag=True, help=ajuda_opcao2)
def main(regex: str, texto_arquivo: str, recursivo: bool, so_nomes: bool):
    """
    Procure por padrões regex em um texto/arquivo.

    Usagem: regex_search [REGEX] [TEXTO | [LOCAL]ARQUIVO]

    obs: este programa só aceita arquivos gravados com unicode utf-8.
    """

    texto_arquivo = texto_arquivo.strip()
    if all((recursivo, isdir(texto_arquivo))):
        gerador = vasculhar_pastas(regex, texto_arquivo, so_nomes)
    elif len(texto_arquivo) <= 180 and isfile(texto_arquivo):
        gerador = procurarNoArquivo(regex, texto_arquivo, so_nomes)
    else:
        gerador = procurar(regex, texto_arquivo)
    for linha in gerador:
        echo(linha)


def procurar(regex: str, texto: str) -> Generator:
    if search(regex, texto, flags=M):
        yield sub(regex, trocar, texto, flags=M)
    else:
        yield


def procurarNoArquivo(regex: str, arquivo: str, so_nomes: bool) -> Generator:
    linha_str = cores[6]
    try:
        with open(arquivo) as arquivo_:
            for numero, texto in enumerate(arquivo_.readlines(), 1):
                if search(regex, texto, flags=M):
                    subs = sub(regex, trocar, texto, flags=M)
                    yield f"{linha_str.format(f'linha {numero}')}: {subs}"
    except UnicodeDecodeError:
        pass


def vasculhar_pastas(regex: str, pasta: str, so_nomes: bool) -> Generator:
    gerador = juntar_nomes_de_arquivos(pasta)
    forma = f"{cores[6].format('arquivo: ')}{{}}\n"
    for arquivo in gerador:
        resultado = procurarNoArquivo(regex, arquivo, so_nomes)
        if resultado:
            try:
                item = next(resultado)
                yield forma.format(arquivo)
                if not so_nomes:
                    yield item
                    yield from resultado
            except StopIteration:
                pass


def juntar_nomes_de_arquivos(pasta) -> Generator:
    return (join(local, arquivo)
            for local, x, arquivos in walk(pasta) for arquivo in arquivos)


def trocar(objeto_match) -> str:
    grupos = list(objeto_match.groups())
    grupo = objeto_match.group()
    if any(grupos):
        ciclo = cycle(cores)
        gerador = map(lambda x: (x, next(ciclo)), grupos)
        texto, forma = next(filter(lambda x: x[0], gerador))
        return forma.format(texto)
    elif grupo:
        return cores[0].format(grupo)


if __name__ == '__main__':
    main()


# TODO: colocar o nome do arquivo e linha na frente.
# TODO: adicionar uma opção caso a pessoa queira somente o nome do arquivo.

# TODO: colorir o texto de cor diferente caso o regex seja feito somente com pipes
# ignorar esse todo acima?

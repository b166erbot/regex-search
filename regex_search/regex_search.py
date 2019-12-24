# from types import GeneratorType as Gen
from itertools import cycle
from os import walk
from os.path import join
from re import M, search, sub
from typing import Generator

import click
from colored import attr, fg

ajuda = ('Vasculha por todos os arquivos contidos'
         ' dentro da [caminho/]pasta passada.')
ajuda2 = 'Mostra somente os nomes dos arquivos'
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


@click.command()
@click.argument('regex', type=click.STRING)
@click.option('-t', '--texto', 'texto', type=click.STRING)
@click.option('-a', '--arquivo', 'arquivo', type=click.STRING)
@click.option('-r', '--recursivo', default=False, is_flag=True, help=ajuda)
@click.option('-s', '--so_nomes', default=False, is_flag=True, help=ajuda2)
def main(regex: str, texto: str, arquivo: open, recursivo: bool, so_nomes: bool):
    """
    Procure por padrões regex em um texto/arquivo.

    Usagem: regex_search REGEX [TEXTO | [LOCAL]ARQUIVO]

    obs: este programa só aceita arquivos gravados com unicode utf-8.
    """

    if recursivo:
        gerador = vasculhar_pastas(regex, '.', so_nomes)
    elif arquivo:
        gerador = procurar_no_arquivo(regex, arquivo)
    elif texto:
        texto = texto.strip()
        gerador = procurar(regex, texto)
    else:
        raise click.UsageError('Use ao menos uma opção [-t, -a, -r].')
    for linha in gerador:
        click.echo(linha)


def procurar(regex: str, texto: str) -> Generator:
    if texto and search(regex, texto, flags=M):
        yield sub(regex, trocar, texto, flags=M)


def procurar_no_arquivo(regex: str, arquivo: open) -> Generator:
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
        resultado = procurar_no_arquivo(regex, arquivo)
        item = next(resultado, None)
        if item:
            yield forma.format(arquivo)
            if not so_nomes:
                yield item
                yield from resultado


def juntar_nomes_de_arquivos(pasta) -> Generator:
    for local, x, arquivos in walk(pasta):
        for arquivo in arquivos:
            yield join(local, arquivo)


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

from os.path import isdir, isfile, exists, join
from os import walk
from re import M, search, sub
from typing import Union, Generator, Tuple
# from types import GeneratorType as Gen
from itertools import cycle, dropwhile, chain

from click import STRING, argument, command, option, echo
from colored import attr, fg


ajuda_opcao = ('Vasculha por todos os arquivos contidos'
                         ' dentro da [local/]pasta passada.')


@command()
@argument('regex', type=STRING)
@argument('texto_arquivo', type=STRING)
@option('-r', '--recursivo', default=False, is_flag=True, help=ajuda_opcao)
def main(regex: str, texto_arquivo: str, recursivo: bool):
    """
    Procure por padrões regex em um texto/arquivo.

    Usagem: regex_search [REGEX] [TEXTO | [LOCAL]ARQUIVO]
    """

    texto_arquivo = texto_arquivo.strip()
    if len(texto_arquivo) <= 180 and exists(texto_arquivo):
        if isfile(texto_arquivo):
            gerador = procurarNoArquivo(regex, texto_arquivo)
        elif recursivo and isdir(texto_arquivo):
            gerador = (join(w, z) for w, x, y in walk(texto_arquivo) for z in y)
            gerador = chain(*(procurarNoArquivo(regex, x) for x in gerador))
    else:
        gerador = procurar(regex, texto_arquivo)
    if gerador:
        for linha in gerador:
            echo(linha)


def procurar(regex: str, texto: Union[str, Generator]) -> Generator:
    if isinstance(texto, str):
        if search(regex, texto, flags=M):
            yield sub(regex, trocar, texto, flags=M)
    else:
        # não sei o porque não funciona.
        # return (sub(regex, trocar, linha, flags=M)
        #         for linha in texto if search(regex, linha, flags=M))
        for linha in texto:
            if search(regex, linha, flags=M):
                yield sub(regex, trocar, linha, flags=M)


def procurarNoArquivo(regex: str, texto_arquivo: str) -> Generator:
    with open(texto_arquivo) as arquivo:
        return procurar(regex, (x for x in arquivo.readlines()))


def trocar(objeto_match) -> str:
    ciclo = cycle(cores)
    grupos = list(objeto_match.groups())  # or objeto_match.group()
    grupo = objeto_match.group()
    if any(grupos):
        gerador = map(lambda x: (x, next(ciclo)), grupos)
        texto, forma = next(filter(lambda x: x[0], gerador))
        return forma.format(texto)
    elif grupo:
        return next(ciclo).format(grupo)


if __name__ == '__main__':
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
    main()


# TODO: ler todos os arquivos na pasta recursivamente
# TODO: cada grupo tenha uma cor diferente, caso as cores se esgotem, começe da
# cor zero novamente.
# TODO: colocar o nome do arquivo na frente.
# TODO: adicionar uma opção caso a pessoa queira somente o nome do arquivo.

# TODO: colorir o texto de cor diferente caso o regex seja feito somente com pipes

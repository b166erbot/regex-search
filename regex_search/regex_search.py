from os.path import exists
from re import MULTILINE, search, sub
from typing import Union

from click import STRING, argument, command, echo
from colored import attr, fg


@command()
@argument('regex', type=STRING)
@argument('texto_arquivo', type=STRING)
def main(regex: str, texto_arquivo: str):
    """
    Procure por padrões regex em um texto/arquivo.

    Usagem: regex_search [REGEX] [TEXTO | [LOCAL]ARQUIVO]
    """

    regex = f"({regex})(?=\n)?"
    if len(texto_arquivo) <= 180 and exists(texto_arquivo):
        with open(texto_arquivo) as arquivo:
            texto_reformulado = procurar(regex, arquivo.read())
            if texto_reformulado:
                echo(texto_reformulado)
    else:
        texto_reformulado = procurar(regex, texto_arquivo)
        if texto_reformulado:
            echo(texto_reformulado)


def procurar(regex: str, texto_arquivo: str) -> Union[str, None]:
    substituir = f"{fg('green')}\\1{attr(0)}"
    if search(regex, texto_arquivo, MULTILINE):
        return sub(regex, substituir, texto_arquivo, MULTILINE)


if __name__ == '__main__':
    main()

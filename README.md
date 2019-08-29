# regex_search

#### procure por qualquer padrão com regex em arquivos/textos de maneira fácil.

###### Instalação:
  * git clone github.com/b166erobot/regex_search
  * cd regex_search
  * python3 setup.py install

###### Usagem:

  * $ regex_search --help
      * regex_search [expressão regular] [texto/[local]arquivo]
  * $ regex_search 'expressão com espaços' 'arquivo com espaços.txt'
      * irá procurar a expressão dentro do arquivo
  * $ regex_search -r '(oi)|(ola)' .
      * irá procurar pela expressão em todas as subpastas da pasta inserida
  * $ regex_search 'regex' `comando shell que retornará um texto`
      * é possível usar o regex_search com comandos shell menos com o pipe.
      * culpem o python por isso.

###### Todo:
  - [ ] adicionar uma função para ler todos os arquivos das pastas recursivamente.
  - [ ] cada grupo tenha uma cor diferente, caso as cores se esgotem, começe da cor zero novamente.
  - [ ] colocar o nome do arquivo e número da linha na frente.
  - [ ] adicionar uma opção caso a pessoa queira somente o nome do arquivo.

###### Versão do python:

  * 3.7.3

###### Contribuidores:

  [b166erobot](http://github.com/b166erobot)

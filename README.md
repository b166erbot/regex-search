# regex_search

#### procure por qualquer padrão com regex em arquivos/textos de maneira fácil.

###### Instalação:
  * git clone github.com/b166erobot/regex_search
  * cd regex_search
  * python3 setup.py install

###### Usagem:

  * $ regex_search.py --help
      * regex_search.py [expressão regular] [opção(ões)] [texto/[local]arquivo]
  * $ regex_search.py 'expressão com espaços' -a 'arquivo com espaços.txt'
      * irá procurar pela expressão dentro do arquivo
  * $ regex_search.py '(oi)|(ola)' -r
      * irá procurar pela expressão '(oi)|(ola)' em todas as subpastas da pasta atual
  * $ regex_search.py 'regex' -t \`comando shell que retornará um texto\`
      * é possível usar o regex_search com comandos shell, menos com o pipe. culpem o python por isso.
  * $ regex_search.py 'regex' -s -r
      * -s mostra somente os nomes dos arquivos.

###### Todo:
  - [x] ~adicionar uma função para ler todos os arquivos das pastas recursivamente.~
  - [x] ~cada grupo tenha uma cor diferente, caso as cores se esgotem, começe da cor zero novamente.~
  - [x] ~colocar o nome do arquivo e número da linha na frente.~
  - [x] ~adicionar uma opção caso a pessoa queira somente o nome do arquivo.~

###### Versão do python:

  * 3.7.3

###### Contribuidores:

  [b166erobot](http://github.com/b166erobot)

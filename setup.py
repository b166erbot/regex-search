from setuptools import find_packages, setup

setup(
    name = 'regex_search',
    version = '1.0.0',
    description = ('procure por qualquer padrão com regex em arquivos/textos'
                   ' de maneira fácil.'),
    url = 'github.com/b166erobot/regex-search',
    author = 'b166erobot',
    author_email = 'b166erobot',
    license = 'MIT',
    packages = find_packages(),
    scripts = ['regex_search/regex_search.py'],
    include_package_data = True,
    install_requires = ['click', 'colored']
)

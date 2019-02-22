# PYTHON

## Introdução

> Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
> Foi lançada por Guido van Rossum (ex-BDFL) em 1991 (28 anos). Atualmente possui um modelo de desenvolvimento comunitário,
> aberto e gerenciado pela organização sem fins lucrativos **Python Software Foundation**.

> O padrão de facto é a implementação CPython (possui também Jython, IronPython, Pypy).

> É uma linguagem de alto nível de propósito geral, multiparadigma (suporta o paradigma orientado a objetos, imperativo, funcional e procedural).
> Possui tipagem dinâmica e uma de suas principais características é permitir a fácil **leitura do código** e exigir poucas linhas de código (**produtividade**) se comparado ao mesmo programa em outras linguagens.

> O nome Python teve a sua origem no grupo humorístico britânico Monty Python, criador do programa Monty Python's Flying Circus.

![Guido Van Rossum](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Guido_van_Rossum_OSCON_2006.jpg/440px-Guido_van_Rossum_OSCON_2006.jpg "Logo Title Text 1")


Parte da cultura da linguagem gira ao redor de **The Zen of Python**, um poema que faz parte do documento "**PEP 20 (The Zen of Python)**"

```python
import this
```

## Glossário e Links:

- [Conferências](https://www.pycon.org/)
- [PEP](https://www.python.org/dev/peps/): PEP 0 -- Index of Python Enhancement Proposals (PEPs) | Python.org
- [PSF](https://www.python.org/psf/): Python Software Foundation
- [PUGPE](http://pycon.pug.pe/) - Comunidade local de Python.
- [pyc](https://pt.stackoverflow.com/questions/207379/fun%C3%A7%C3%A3o-dos-arquivos-pyc-em-python): Extensões: .py, .pyc, .pyd, .pyo, .pyw, .pyz .
- [Pycon US](https://us.pycon.org/2019/) - Conferência Americana
- [PyPI](https://pypi.org/): O "**Python Package Index (PyPI)**" é o repositório de software principal da linguagem de programação Python. Apelidado de "CheeseShop".
- [Pypy](https://pypy.org/) - Compilador JIT Python.
- [Site Oficial Python](http://www.python.org/)
- [Site Oficial da Comunidade Brasileira de Python](http://www.pythonbrasil.com.br/)
- [Python Brasil](https://2018.pythonbrasil.org.br/) - Conferência Nacional
- [Python Nordeste](https://2018.pythonnordeste.org/) - Conferência Regional
- [PyVideo](https://pyvideo.org/) - Python media Index
- [Wiki](https://wiki.python.org/moin/) - Wiki Python
- [Zen do Python](https://www.python.org/dev/peps/pep-0020/): Zen do Python (https://medium.com/@Pythonidaer/a-brief-analysis-of-the-zen-of-python-2bfd3b76edbf)
- [FAQ BR](http://www.pythonbrasil.com.br/moin.cgi/PerguntasFrequentes/SobrePython)


## Instalação

Ao final do tutorial entederemos melhor sobre o ecossistema Python e suas ferramentas.

### [PyEnv](https://github.com/pyenv/pyenv)


1. Instalar PyEnv
```bash
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

2. Adicionar no .bashrc (geralmente ele fica na pasta /home/<usuário>)

2.1 Se durante a instalação surgirem erros visite ["Common build problems"](https://github.com/pyenv/pyenv/wiki/Common-build-problems).

Exemplo para o Ubuntu.

```bash
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

2.2 Atualização dos dotfiles.

```bash
export PATH="/home/<USER>/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

3. Instalando as versões disponíveis:

3.1 Instalar Python 3, Python 2 e Miniconda:

```bash
$ pyenv install -l
```

```bash
$ pyenv install 3.7.0
$ pyenv install 2.7.15
$ pyenv install miniconda
```

3.2 Atualizar o Pip em cada versão:
```
$ pip install -U pip
```

#### Referências:
[virtualenv](https://docs.python-guide.org/dev/pip-virtualenv/)
[pyenv](https://realpython.com/python-virtual-environments-a-primer/)


4. Execute:

    4.1 Para ver as versões do Python que você tem disponível:
    ```
    $ pyenv versions
    ```

    4.2 Adicione uma versão global (*diferente da system*) para ser a versão global do Python:
    ```
    $ pyenv global 3.x.x
    ```

    4.3 Pode adicionar versões do Python dentro de uma pasta específica:

    Ele adicionará um arquivo .python-version na pasta onde foi executado o comando.

    ```
    $ pyenv local 3.x.x
    ```

6. Execute:

    - Ativar:
        ```
        $ pyenv activate nome_env
        ```

    - Desativar:
        ```
        $ pyenv deactivate
        ```

7. Se tiver perdido:

    Aquele famoso **help**
    ```
    $ pyenv
    ```


### [Pipsi](https://github.com/mitsuhiko/pipsi)

1. Instalando Pipsi

```bash
$ curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python
```

*Ele utilizará o Python configurado como global pelo **Pyenv***


2. Novamente no .bashrc, adicione:

Bloqueia o uso do pip se não for dentro de uma virtualenv.

```bash
export PIP_REQUIRE_VIRTUALENV=true

gpip() {
    PIP_REQUIRE_VIRTUALENV="" pip "$@"
}
```

3. Instalando pacotes pelo Pipsi:

Os pacotes instalados pelo Pipsi ficam acessiveis para todos os ambientes.

```bash
$ pipsi install <package>
```
*Lembrar que ele precisa de uma versão global para se apoiar. Não desinstale essa versão.*


### PIPENV

https://github.com/pypa/pipenv
https://pipenv.readthedocs.io/en/latest/
https://realpython.com/pipenv-guide/

pipsi install pipenv
pipenv install
pipenv shell
pipenv run


```bash
$ pipenv install --dev
```



### EXEMPLO DE PROJETO USANDO JUPYTER

```bash
$ pipenv shell
$ python -m ipykernel install --user --name=`basename $VIRTUAL_ENV` --display-name "My Great Env"
```

```bash
$ jupyter kernelspec list
$ jupyter nbextension list
$ jupyter contrib nbextension install --sys-prefix
$ jupyter nbextension enable widgetsnbextension --debug --sys-prefix --py
```
### Referências

[Guia do Henrique Bastos](https://medium.com/welcome-to-the-django/guia-definitivo-para-organizar-meu-ambiente-python-a16e2479b753)



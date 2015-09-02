# Instalando Python
É essencial que cada aluno tenho seu próprio laptop durante o curso.  O curso
foi desenhado para ser independente to sistema operacional, mas é altamente
recomendado o uso de de um sistema baseado em *\*nix* como o Linux.


## Módulos

Além do interpretador Python\* nos utilizaremos uma gama de pacotes
científicos.  A lista abaixo contém um mínimo necessário para começar.
**Vamos instalar tudo usando o miniconda.  Visite os sites para
conhecer os módulos mas não faça download de nada.**

- [NumPy](http://www.numpy.org/): Módulo fundamental para computação científica em Python.
- [SciPy](http://www.scipy.org/): Ecossistema em Python baseado em software livre para matemática, ciência, e engenharia.
- [matplotlib](http://www.matplotlib.org/): Biblioteca de plotagem 2D.
- [IPython](http://ipython.org/): Ambiente Python interativo

\* Nesse curso utilizaremos Python 2.7, mas a sintaxe que utilizaremos será
aproximadamente 99% compatível com Python 3.

# Instalando os requisitos para o curso

Python, e a maioria dos módulos criados para Python, são Software
licenciados de forma *Open Source*.  Por isso há mais de uma forma de obter
um conjunto "Python" para computação científica.  Entre elas a
"compile tudo você mesmo."

Para esse curso eu recomendo o instalador
[Anaconda](https://store.continuum.io/cshop/anaconda/),
ou sua versão light o [miniconda](http://conda.pydata.org/miniconda),
ambos produtos gratuitos oferecido pela
[ContinuumIO Analytics](http://continuum.io/).

## Linux

```bash
wget http://bit.ly/CursoUFBA -O requirements.txt

url=http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
wget $url -O miniconda.sh

bash miniconda.sh -b
export PATH=$HOME/miniconda/bin:$PATH
```

## Windows

1. Faça *donwload* e instale o [Miniconda para windows](http://conda.pydata.org/miniconda.html).

2. Baixe também o [arquivo](http://bit.ly/CursoUFBA) de pré-requisitos para o curso.

3. Abra um terminal do DOS. (Aperte "Tecla do Windows+R" e digite `cmd`.)

## OSX
As instruções requirem o uso da linha de comando.  Abra a aplicação do
*Terminal*, que pode ser encontrada em:
`Applications\Utilities\Terminal.app`.  É altamente recomendável que você se
familiarize com o uso do terminal em OS-X.  Caso nunca tenha usado leia esse blog:

[http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)

```bash
curl https://raw.githubusercontent.com/ocefpaf/python4oceanographers_intro_course/master/notebooks/requirements.txt -o requirements.txt

url=http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
curl $url -o miniconda.sh

bash miniconda.sh -b
export PATH=$HOME/miniconda/bin:$PATH
```

## Após a instalação do Miniconda

### Adicione um "canal" de módulos para oceanografia e faça um *update*
```bash
conda config --add channels ioos -f
conda update --yes --all
```

### Crie um ambiente para o curso
```bash
conda create --yes -n CursoUFBA --file requirements.txt python=2.7
```

### Para entrar no ambiente do curso
#### Linux e OSX
```bash
source activate CursoUFBA
```

#### Windows
```bash
activate CursoUFBA
```

### Para sair do ambiente do curso
#### Linux e OSX
```bash
source deactivate
```

#### Windows
```bash
deactivate # ou feche o terminal.
```

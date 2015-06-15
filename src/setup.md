# Instalando Python
É essencial que cada aluno tenho seu próprio laptop durante o curso.  O curso
foi desenhado para ser independente to sistema operacional, mas é altamente
recomendado o uso de de um sistema baseado em *\*nix* como o Linux.


## Módulos

Além do interpretador Python\* nos utilizaremos uma gama de pacotes
científicos.  A lista abaixo contém um mínimo necessário para começar:

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
url=http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
wget $url -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b
export PATH=$HOME/miniconda/bin:$PATH
conda update --yes conda
```

### Adicione um "canal" de módulos para oceanografia
```bash
conda config --add channels ioos -f
conda config --set show_channel_urls True
```

### Crie um ambiente para o curso
```bash
wget http://bit.ly/ioos_req -O ioos_req.txt
conda create --yes -n curso --file ioos_req.txt python=2.7
source activate curso
```
### Usar o miniconda como seu Python padrão
Caso queira usar essa instalação como seu Python padrão adicione as linhas
abaixo em seu `.bashrc`:
```bash
export PATH=$HOME/miniconda/bin:$PATH && source activate curso
```

### Para sair do ambiente do curso
```bash
source deactivate
```


## Windows

1.  Navegue para [Anaconda Python Distribution](https://store.continuum.io/cshop/anaconda/) e clique em "download Anaconda."  Depois escolha seu instalador: `Windows 64-bit Python 2.7 Graphical Installer`.  (Não clique em `I WANT PYTHON3.4` e escolha Windows 32-bit caso esteja usando uma versão antiga do WindowsXP.)

2. Depois do download, rode o programa de instalação, depois vá em: "Start => All Programs" e abra a pasta do Anaconda.

3. Clique em `Anaconda Command Prompt` para abrir uma linha de comandos.

### Crie um ambiente para o curso

4. Na linha de comando *Anaconda Command Prompt*, digite `launcher`.

5. No *Launcher*, clique em *Manage Channels* encima à direita.

6. Digite "ioos" na caixa de texto, clique em *Add Channel*.  Note que você
deve ter apenas 2 canais: `ioos` e `defaults`.  Clique em *Submit*.

7. No *Launcher*, clique em *Environment* no topo, depois em *new environment* e na caixa *New Environment Name*, digite "curso" e deixe a versão do Python em 2.7.  Clique em *submit*.

8. Depois clique em *Environment* novamente e certifique que "curso" está selecionado.

9. Abra a janela de comando do *Anaconda* e cheque o diretório que você está.

10. Faça o download do arquivo de requisitos para
[Windows](https://raw.githubusercontent.com/ioos/conda-recipes/master/00_env_requirements/ioos/ioos_req_windows64.txt)
no diretório acima.


3. Na linha de comandos digite:
```
activate curso
conda install --file ioos_req_windows64.txt --yes
```

## OSX
As instruções requirem o uso da linha de comando.  Abra a aplicação do
*Terminal*, que pode ser encontrada em:
`Applications\Utilities\Terminal.app`.  É altamente recomendável que você se
familiarize com o uso do terminal em OS-X.  Caso nunca tenha usado leia esse blog:

http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line
(Não esta aparecendo como link quando o site é rendereizado)

### Instalando em OSX com Miniconda

```bash
url=http://repo.continuum.io/miniconda/Miniconda-latest-MacOSX-x86_64.sh
curl $url -o miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b
export PATH=$HOME/miniconda/bin:$PATH
conda update --yes conda
```

### Adicione o “canal” de módulos para oceanografia
```bash
conda config --add channels ioos -f
conda config --set show_channel_urls True
```

### Crie um ambiente para o curso
```bash
curl -o ioos_req.txt http://bit.ly/ioos_req
conda create --yes -n curso --file ioos_req.txt python=2.7
source activate curso
```

### Usar o miniconda como seu Python padrão
Caso queira usar essa instalação como seu Python padrão adicione as linhas
abaixo em seu `.bash_profile`:
```
export PATH=$HOME/miniconda/bin:$PATH && source activate curso
```

### Para sair do ambiente do curso
```bash
source deactivate
```

'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Criar pastas para os arquivos serem criadoss
'''

import os.path  # Modulo usado para manipular os caminhos
import platform  # Modulo usado para identificar o SO
import sys


def start():  # Metodo que recebe uma dict, usado para nomear as pastas

    def diretorios():  # Metodo qUe criará os diretorios
        so = platform.system()
        if so == 'Linux':
            dir = os.path.expanduser('~/Documentos/')  # Pego o caminho ate a pasta Documentos
            os.makedirs(dir + 'Transfer/', exist_ok=True)  # Crio a pasta Arquivos e outra com o titulo da busca, se existir nao me retorna nenhum exeçao
            dir = os.path.expanduser('~/Documentos/Transfer/')  # Pego o caminho completo para ser retornado ao robo de texto
            return dir
        elif so == 'Windows':
            dir = os.path.expanduser('~\\OneDrive\\Documentos\\')
            os.makedirs(dir + 'Transfer\\', exist_ok=True)
            dir = os.path.expanduser('~\\OneDrive\\Documentos\\Transfer\\')
            return dir
        else:
            print('Sistema operacional não suportado')
            sys.exit()

    dir = diretorios()

    return dir

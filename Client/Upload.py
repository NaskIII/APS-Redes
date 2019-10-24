from threading import Thread
import platform
import sys
import os


class Upload(Thread):
    def __init__(self, ftp):
        Thread.__init__(self)
        self.ftp = ftp
        self.tamanho = 0
        self.nameArq = ''
        self.finish = None

    def size(self):
        path = input('Informe o caminho do arquivo: ')
        try:
            self.tamanho = os.path.getsize(path)
            return path
        except:
            print('Arquivo inexistente')
            return -1

    def run(self):

        path = self.size()
        if path == -1:
            return

        so = platform.system()
        nomeArq = ''

        if so == 'Linux':
            nomeArq = path.split('/')
            nomeArq = nomeArq[-1]
        elif so == 'Windows':
            nomeArq = path.split('\\')
            nomeArq = nomeArq[-1]
        else:
            print('Sistema Operacional não suportado!')
            sys.exit()

        self.nameArq = nomeArq

        try:
            archive = open(path, 'rb')
            self.finish = False
            self.ftp.storbinary('STOR ' + nomeArq, archive)
            self.finish = True
        except:
            print('Caminho inválido!\n')

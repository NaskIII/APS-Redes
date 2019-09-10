from ftplib import FTP
import sys
import os.path
import os
import shutil


class ClientFTP(object):
    def __init__(self, client):
        self.user = client['User']
        self.password = client['Password']

    def connect(self):
        ftp = FTP('')
        ftp.connect('localhost', 1026)
        try:
            ftp.login(user=self.user, passwd=self.password, acct='')
            #dir = os.path.expanduser('~\\OneDrive\\Documentos\\')
            return ftp
        except:
            print('Usuário e/ou senha incorretos.\n')
            sys.exit()

    def download(self, ftp):
        caminho = input('Informe o arquivo ')
        try:
            arquivo = open(caminho, 'wb')
            ftp.retrbinary('RETR ' + caminho, arquivo.write, 1024)
            arquivo.close()
        except:
            print('Caminho inválido!\n')
            self.escolha()

    def upload(self, ftp):
        caminho = input('Digite o caminho absoluto do arquivo: ')
        arq = input('Digite o nome do arquivo: ')
        try:
         shutil.copy(caminho, '/home/nask/Documentos/Repositórios/APS-Redes/')
         arquivo = open(arq, 'rb')
         ftp.storbinary('STOR ' + arq, arquivo)
         shutil.move('/home/nask/Documentos/Repositórios/APS-Redes/' + arq, caminho)
        except:
           print('Caminho inválido!\n')
           self.escolha()

    def listar(self, ftp):
        ftp.retrlines('LIST')

    def escolha(self):
        ftp = self.connect()

        escolha = ''
        while escolha != 'exit':
            escolha = input('\n1 - Download \n2 - Upload \n3 - Listar\n \n>>> ')
            self.call(escolha, ftp)

    def call(self, escolha, ftp):
       if escolha == '1':
          self.download(ftp)
       elif escolha == '2':
            self.upload(ftp)
       elif escolha == '3':
            self.listar(ftp)
       elif escolha == 'exit':
            ftp.close()

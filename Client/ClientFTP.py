from ftplib import FTP
import sys
import os.path


class ClientFTP(object):
     def __init__(self, client):
        self.user = client['User']
        self.password = client['Password']

     def connect(self):
        ftp = FTP('')
        ftp.connect('localhost', 1026)
        try:
         ftp.login(user=self.user, passwd=self.password, acct='')
         dir = os.path.expanduser('~\\OneDrive\\Documentos\\')
         ftp.cwd(dir)
         return ftp
        except:
           print('Usuário e/ou senha incorretos.')
           sys.exit()

     def download(self, ftp):
        caminho = input('Digite o caminho absoluto do arquivo: ')
        arquivo = open(caminho, 'wb')
        ftp.retrbinary('RETR ' + caminho, arquivo.write, 1024)
        ftp.quit()
        arquivo.close()

     def upload(self, ftp):
        caminho = input('Digite o caminho absoluto do arquivo: ')
        ftp.storbinary('STOR '+caminho, open(caminho, 'rb'))
        ftp.quit()

     def listar(self, ftp):
        ftp.retrlines('LIST')

     def call(self):
        ftp = self.connect()
        escolha = int(input('1 - Download \n2 - Upload \n3 - Listar\n \n>>> '))
        
        if escolha == 1:
           self.download(ftp)
        elif escolha == 2:
           self.upload(ftp)
        else:
           self.listar(ftp)

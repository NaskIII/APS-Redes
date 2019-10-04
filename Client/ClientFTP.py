from ftplib import FTP
import sys
import platform


class ClientFTP(object):
    def __init__(self, client):
        self.user = client['User']
        self.password = client['Password']
        self.ip = None

    def connect(self):
        ftp = FTP('')
        try:
            ftp.connect(self.ip, 8080)
            print('\nConexão bem sucedida!\n')
            ftp.login(user=self.user, passwd=self.password, acct='')
            print('Credenciais verificadas!\n')
            return ftp
        except:
            print('\nVerifique o IP. Se estiver tudo correto, suas credênciais estão inválidas.\n')
            sys.exit()

    def download(self, ftp):
        path = input('Informe o arquivo ')
        try:
            arq = open(path, 'wb')
            ftp.retrbinary('RETR ' + path, arq.write, 1024)
            arq.close()
        except:
            print('Caminho inválido!\n')
            self.menu(self.ip)

    def upload(self, ftp):
        path = input('Informe o caminho do arquivo: ')

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

        try:
            archive = open(path, 'rb')
            ftp.storbinary('STOR ' + nomeArq, archive)

        except:
            print('Caminho inválido!\n')
            self.menu(self.ip)

    def listar(self, ftp):
        ftp.retrlines('LIST')

    def menu(self, ip):
        self.ip = ip
        ftp = self.connect()

        escolha = ''
        while escolha != '!EXIT':
            escolha = input('\n1 - Download \n2 - Upload \n3 - Listar\n \n>>> ')
            self.call(escolha, ftp)

    def call(self, escolha, ftp):
        if escolha == '1':
            self.download(ftp)
        elif escolha == '2':
            self.upload(ftp)
        elif escolha == '3':
            self.listar(ftp)
        elif escolha == '!EXIT':
            print('\nAté logo!')
            sys.exit()

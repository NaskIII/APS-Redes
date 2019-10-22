from ftplib import FTP
import sys
from threading import Thread
import time
from Client import Upload
import os


class ClientFTP(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.user = client['User']
        self.password = client['Password']

    ip = None
    ftp = None

    def connect(self):
        global ip

        ftp = FTP('')
        try:
            ftp.connect(ip, 8080)
            print('\nConexão bem sucedida!\n')
            ftp.login(user=self.user, passwd=self.password, acct='')
            print('Credenciais verificadas!\n')
            return ftp
        except:
            print('\nVerifique o IP. Se estiver tudo correto, suas credênciais estão inválidas.\n')
            sys.exit()

    def run(self):

        def download(ftp):
            path = input('Informe o arquivo ')
            try:
                arq = open(path, 'wb')
                ftp.retrbinary('RETR ' + path, arq.write, 1024)
                arq.close()
            except:
                print('Caminho inválido!\n')
                self.menu(ip)

    def listar(self, ftp):
        ftp.retrlines('LIST')

    def menu(self, IP):
        global ip

        ip = IP
        ftp = self.connect()

        escolha = ''
        while escolha != '!EXIT':
            escolha = input('\n1 - Download \n2 - Upload \n3 - Listar\n \n>>> ')
            self.call(escolha, ftp)

    def progress_bar(self, value, max, barsize):
        chars = int(value * barsize / float(max))
        numero = max - value
        percent = int((numero * 100) / max)
        percent = 100 - percent
        sys.stdout.write("#" * chars)
        sys.stdout.write(" " * (barsize - chars + 2))
        if value >= max:
            sys.stdout.write("Done. \n\n")
        else:
            sys.stdout.write("[%3i%%]\r" % percent)
            sys.stdout.flush()

    def call(self, escolha, FTP):
        global ftp

        ftp = FTP
        if escolha == '1':
            self.download(FTP)
        elif escolha == '2':
            thread1 = Upload.Upload(FTP)
            thread1.start()
            semaforo = 0
            print()

            while True:
                if thread1.finish is False:
                    if semaforo == 0:
                        time.sleep(1)
                        semaforo = 1
                    else:
                        path = os.path.expanduser('~/Documentos/Transfer/' + thread1.nameArq)
                        size = os.path.getsize(path)
                        self.progress_bar(size, thread1.tamanho, 40)
                        time.sleep(0.1)
                elif thread1.finish is True:
                    break
        elif escolha == '3':
            self.listar(FTP)
        elif escolha == '!EXIT':
            print('\nAté logo!')
            sys.exit()

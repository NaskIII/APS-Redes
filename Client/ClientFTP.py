from ftplib import FTP
import ftplib
import sys
from threading import Thread
import time
from Client import Upload
from Client import Download
import os
import platform


class ClientFTP(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.user = client['User']
        self.password = client['Password']
        self.path = os.path.expanduser('~/')

    ip = None
    ftp = None

    def connect(self):
        global ip
        os.chdir(self.path)

        ftp = FTP('')
        try:
            ftp.connect(ip, 8080)
            ftp.login(user=self.user, passwd=self.password, acct='')
            print('\nConexão bem sucedida!\n')
            return ftp
        except:
            print('\nVerifique o IP. Se estiver tudo correto, suas credênciais estão inválidas.\n')
            sys.exit()

    def listar(self, ftp):
        ftp.retrlines('LIST')

    def menu(self, IP):
        global ip, ftp

        ip = IP
        ftp = self.connect()

        escolha = ''
        while escolha != '!EXIT':
            escolha = input('\n1 - Download \n2 - Upload \n3 - Listar\n \n>>> ')

            if escolha == '1':
                self.download(ftp)
            elif escolha == '2':
                self.upload(ftp)
            elif escolha == '3':
                self.listar(ftp)
            elif escolha == '!EXIT':
                self.exit()
            elif escolha == 'clear':
                self.clear()
            elif escolha == '!CHANGE':
                self.change()
            elif escolha == '!CWD':
                self.cwd()

    def download(self, FTP):

        thread2 = Download.Download(FTP, self.path)
        thread2.start()

        while thread2.is_alive():
            if thread2.finish is False:
                try:
                    with open(thread2.nameArq, 'r') as f:
                        size = os.path.getsize(os.path.expanduser(self.path + '/') + thread2.nameArq)
                        if size is not None:
                            tamanho = ftp.size(thread2.nameArq)
                            if tamanho is not None:
                                self.progress_bar(size, tamanho, 40)
                                time.sleep(0.1)
                        else:
                            print('Loading...\r')
                except IOError:
                    print('Loading...\r')
                except ftplib.error_perm as err:
                    pass

        if thread2.finish is True:
            self.progress_bar(100, 100, 40)

    def upload(self, FTP):
        thread1 = Upload.Upload(FTP)
        thread1.start()

        while thread1.is_alive():
            if thread1.finish is False:
                time.sleep(0.1)
                size = ftp.size(thread1.nameArq)
                if size is not None:
                    self.progress_bar(size, thread1.tamanho, 40)
                    time.sleep(0.1)
                else:
                    print('Loading...\r')
        # else:
            # self.progress_bar(100, 100, 40)

    def clear(self):
        so = platform.system()
        if so == 'Linux':
            os.system('clear')
        elif so == 'Windows':
            os.system('cls')

    def change(self):

        self.path = input('Digite o diretório completo: ')
        try:
            os.chdir(self.path)
        except:
            print('Diretório inexistente')

    def cwd(self):
        print('\nO diretório atual é: %s' % os.getcwd())

    def exit(self):
        print('\nAté logo!')
        sys.exit()

    def progress_bar(self, value, max, barsize):
        chars = int(value * barsize / float(max))
        numero = max - value
        percent = int((numero * 100) / max)
        percent = 100 - percent
        sys.stdout.write("#" * chars)
        sys.stdout.write(" " * (barsize - chars + 2))
        if value >= max:
            sys.stdout.write("Done. \n\n")
            print()
        else:
            sys.stdout.write("[%3i%%]\r" % percent)
            sys.stdout.flush()

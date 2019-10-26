from threading import Thread
import os


class Download(Thread):
    def __init__(self, ftp, cwd):
        Thread.__init__(self)
        self.ftp = ftp
        self.finish = None
        self.nameArq = ''
        self.cwd = cwd

    def run(self):

        path = input('Informe o arquivo: ')
        if path == '!exit':
            return
        print()
        self.nameArq = path
        arq = None

        try:
            arq = open(path, 'wb')
            self.finish = False
            self.ftp.retrbinary('RETR ' + path, arq.write, 1024)
            self.finish = True
            arq.close()
        except:
            arq.close()
            os.remove(self.cwd + '/'+ path)
            print('Arquivo não encontrado!\n')

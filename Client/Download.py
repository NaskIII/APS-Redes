from threading import Thread


class Download(Thread):
    def __init__(self, ftp):
        Thread.__init__(self)
        self.ftp = ftp
        self.finish = None
        self.nameArq = ''

    def run(self):

        path = input('Informe o arquivo: ')
        print()
        self.nameArq = path
        try:
            arq = open(path, 'wb')
            self.finish = False
            self.ftp.retrbinary('RETR ' + path, arq.write, 1024)
            self.finish = True
            arq.close()
        except:
            print('Caminho inválido!\n')

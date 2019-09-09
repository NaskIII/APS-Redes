from ftplib import FTP

class ClientFTP(object):
     def __init__(self, client):
        self.user = client['User']
        self.password = client['Password']

     def connect(self):
        ftp = FTP('')
        ftp.connect('localhost', 1026)
        ftp.login(user=self.user,passwd=self.password,acct='')
        ftp.retrlines('LIST')

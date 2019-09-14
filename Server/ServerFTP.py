from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class ServerFTP(object):
    def __init__(self, client, diretorio):
        self.user = client['User']
        self.password = client['Password']
        self.diretorio = diretorio
        self.ip = None

    def login(self):
        login = DummyAuthorizer()
        login.add_user(self.user, self.password, self.diretorio,perm='elradfmw', msg_login='Login Succefull', msg_quit='Goodbye')
        return login
    
    def handler(self, login):
        handler = FTPHandler
        handler.authorizer = login
        return handler
    
    def server(self, handler):
        try:
            server = FTPServer((self.ip, 8080), handler)
            print('\nConexão bem sucedida!\n')
            server.serve_forever()
        except:
            print('Impossível estabelecer a conexão')

    def caller(self, ip):
        self.ip = ip
        login = self.login()
        handler = self.handler(login)
        self.server(handler)
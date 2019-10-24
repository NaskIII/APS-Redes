from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class ServerFTP(object):
    def __init__(self, client, diretorio):
        self.user = client['User']
        self.password = client['Password']
        self.diretorio = diretorio

    ip = None
    check = False

    def login(self):
        login = DummyAuthorizer()
        login.add_user(self.user, self.password, self.diretorio, perm='elradfmwM', msg_login='Login Succefull', msg_quit='Goodbye')
        return login
    
    def handler(self, login):
        handler = FTPHandler
        handler.authorizer = login
        return handler
    
    def server(self, handler):
        global ip
        try:
            server = FTPServer((ip, 8080), handler)
            server.serve_forever()
        except:
            print('Impossível estabelecer a conexão')

    def caller(self, IP):
        global ip
        ip = IP
        login = self.login()
        handler = self.handler(login)
        self.server(handler)

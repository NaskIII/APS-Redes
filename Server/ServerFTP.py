from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class ServerFTP(object):
    def __init__(self, client, diretorio):
        self.user = client['User']
        self.password = client['Password']
        self.diretorio = diretorio

    def login(self):
        login = DummyAuthorizer()
        login.add_user(self.user, self.password, '/home/nask/Documentos/Transfer/',perm='elradfmw', msg_login='Login Succefull', msg_quit='Goodbye')
        return login
    
    def handler(self, login):
        handler = FTPHandler
        handler.authorizer = login
        return handler
    
    def server(self, handler):
        server = FTPServer(('192.168.0.15', 8080), handler)
        server.serve_forever()

    def caller(self):
        login = self.login()
        handler = self.handler(login)
        self.server(handler)
import sys
sys.path.append('/home/nask/Documentos/Repositórios/APS-Redes/')
from Client import ClientFTP


def start():
    def createUser():
        user = input('Digite seu nome de usuário: ')
        return user
    
    def createPassword():
        password = input('Digite sua senha: ')
        return password
    
    client = {
        'User': createUser(),
        'Password': createPassword()
    }

    def call():
        ClientFTP.ClientFTP(client).connect()

    call()

start()
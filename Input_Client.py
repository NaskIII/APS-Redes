from Client import ClientFTP
import sys


def start():
    ip = None

    if len(sys.argv) > 1:
        ip = sys.argv[1]

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
        ClientFTP.ClientFTP(client).menu(ip)

    call()

start()
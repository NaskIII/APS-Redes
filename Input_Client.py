from Client import ClientFTP
import sys
import platform
import os


def start():
    so = platform.system()

    if so == 'Linux':
        os.system('clear')
    elif so == 'Windows':
        os.system('cls')

    ip = None

    if len(sys.argv) > 1:
        ip = sys.argv[1]
    else:
        print('Passe como argumento um ip válido.')
        sys.exit()
        
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
        if so == 'Linux':
            os.system('clear')
        elif so == 'Windows':
            os.system('cls')
        ClientFTP.ClientFTP(client).menu(ip)

    call()

start()
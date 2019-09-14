import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from Server import ServerFTP
import Diretorios


def start():

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
        ServerFTP.ServerFTP(client, Diretorios.start()).caller(ip)

    call()

start()
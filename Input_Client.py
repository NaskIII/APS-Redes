import sys
import platform
if platform.system() == 'Linux':
    sys.path.append('/home/nask/Documentos/Repositórios/APS-Redes/')
elif platform.system() == 'Windows':
    sys.path.append('C:\\Users\\rapha\\Onedrive\\Documentos\\Repositórios\\')
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
        ClientFTP.ClientFTP(client).escolha()

    call()

start()
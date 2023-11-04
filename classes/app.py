from menu import Menu
from util import *

class App:

    def __init__(self):
        
        mn = Menu()

        while True:
            
            mn.mostrar_opcoes_inicial()
            opcao = input()
            validate_inteiro(opcao)

if __name__ == "__main__":
    App()
from login import Login
from util import *


class Menu:
    
    def __init__(self):
        
        self.mostrar_opcoes_inicial()

    def cadastrar_se(self):
        os.system('cls')
        input("Informe seu nome: ")
        input("Informe sua senha: ")


    def mostrar_opcoes_inicial(self):
        while True:
            print("O que deseja fazer?\n1-Fazer Login\n2-Cadastrar-se\n3-Sair")
            opcao = input()
            if validate_inteiro(opcao):
                if opcao == "1":
                    print("Login")
                    break
                elif opcao == "2":
                    self.cadastrar_se()
                    break
                elif opcao == "3":
                    break
                else:
                    self.opcao_invalida()
            else:
                self.opcao_invalida()



    def opcao_invalida(self):
        print("Opção inválida!")
        time.sleep(2)
        os.system('cls')
    
if __name__ == "__main__":
    
    menu = Menu()
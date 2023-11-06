from login import Login
from util import *
from comprador import Comprador


class Menu:
    
    def __init__(self):
        
        self.mostrar_opcoes_inicial()

    def cadastrar_se(self):
        os.system('cls')
        novo_comprador = Comprador()
        novo_comprador.nome = input("Informe seu nome: ")
        novo_comprador.senha = input("Informe sua senha: ")
        novo_comprador.data_de_nascimento = input("Informe sua data de nascimento: ")
        novo_comprador.email= input("Informe seu email: ")
        novo_comprador.is_ativo = True
        novo_comprador.logradouro = input("Informe seu logradouro: ")
        novo_comprador.numero = input("Informe o número do logradouro: ")
        novo_comprador.complemento = input("Informe o complemento: ")
        novo_comprador.cidade = input("Informe sua cidade: ")
        novo_comprador.uf = input("Informe o uf: ")


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
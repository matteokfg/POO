from login import Login
from util import *
from comprador import Comprador


class Menu:
    
    def __init__(self):
        
        self.mostrar_opcoes_inicial()

    def cadastrar_se(self):
        os.system('cls')
        codigo=1
        nome = input("Informe seu nome: ")
        senha = input("Informe sua senha: ")
        while True:
            data_de_nascimento = input("Informe sua data de nascimento: ")
            if validate_data(data_de_nascimento):
                break
        cpf = input("Informe seu CPF: ")
        rg = input("Informe seu RG: ")
        while True:
            email= input("Informe seu email: ")
            if validate_email(email):
                break
        is_ativo = True
        logradouro = input("Informe seu logradouro: ")
        numero = input("Informe o número do logradouro: ")
        complemento = input("Informe o complemento: ")
        cidade = input("Informe sua cidade: ")
        uf = input("Informe o uf: ")
        cep = input("Informe seu CEP: ")
        cartao = input("Informe seu número de cartão de crédito/débito: ")
        novo_comprador = Comprador(codigo=codigo,
                                   nome=nome,
                                   senha=senha,
                                   data_de_nascimento=data_de_nascimento,
                                   email=email,
                                   is_ativo=is_ativo,
                                   cpf=cpf,
                                   rg=rg,
                                   logradouro=logradouro,
                                   numero=numero,
                                   complemento=complemento,
                                   cidade=cidade,
                                   uf=uf,
                                   cep=cep,
                                   cartao=cartao)

        
        print(novo_comprador.nome)
        print(novo_comprador.senha)
        print(novo_comprador.data_de_nascimento)
        print(novo_comprador.cpf)
        print(novo_comprador.rg)
        print(novo_comprador.email)
        print(novo_comprador.is_ativo)
        print(novo_comprador.logradouro)
        print(novo_comprador.numero)
        print(novo_comprador.complemento)
        print(novo_comprador.cidade)
        print(novo_comprador.uf)
        print(novo_comprador.cep)
        print(novo_comprador.cartao)


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
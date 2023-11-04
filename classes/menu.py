from login import Login



class Menu:
    
    def __init__(self):
        
        pass

    def mostrar_opcoes_inicial(self):
        print("O que deseja fazer?\n1-Fazer Login\n2-Cadastrar-se\n3-Sair")

    def opcao_invalida(self):
        print("Opção inválida!")
    
if __name__ == "__main__":
    
    Menu()
banco_de_dados = {"Raul": "1234",
                  "Matteo": "321"}


class Login:
    
    def __init__(self):
        self.nome = None
        self.senha = None
        
    def solicita_login(self):
        
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        
        try:
            if banco_de_dados[nome] == senha:
                print("Fez login")
                self.nome = nome
                self.senha = senha
            else:
                print("Senha errada")
        except KeyError:
            print("Usuário não encontrado")
            
        
            
        

if __name__ == "__main__":
    
    login = Login()
    login.solicita_login()
    
    input()
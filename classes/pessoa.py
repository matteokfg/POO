from datetime import date
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class Pessoa:

    def __init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo):

        self.__codigo = codigo
        self.__nome = nome
        self.__senha = senha
        self.__data_de_nascimento = data_de_nascimento
        self.__email = email
        self.__is_ativo = is_ativo

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        try:
            int(novo_codigo)
            self.__codigo = novo_codigo
        except ValueError:
            print("Apenas são permitidos valores inteiros")
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento
    
    @data_de_nascimento.setter
    def data_de_nascimento(self, nova_data_de_nascimento):
        nova_data_de_nascimento = str(nova_data_de_nascimento[6:]+'-'+nova_data_de_nascimento[3:5]+'-'+nova_data_de_nascimento[0:2])
        try:
            date.fromisoformat(nova_data_de_nascimento)
            self.__data_de_nascimento = nova_data_de_nascimento
        except ValueError:
            print("Data não válida!")
        

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        if(re.fullmatch(regex, novo_email)):
            self.__email = novo_email
        else:
            print("Email Inválido!")
        

    @property
    def is_ativo(self):
        return self.__is_ativo
    
    @is_ativo.setter
    def is_ativo(self, novo_is_ativo):
        if novo_is_ativo == False or novo_is_ativo == True:
            self.__is_ativo = novo_is_ativo
        else:
            raise "Status não válido"

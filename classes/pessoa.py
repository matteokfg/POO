import sys
#sys.path.insert(1, 'POO/util')
from util import *
from connector import Connector


class Pessoa(Connector):
    def __init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo):
        Connector.__init__("../banco_de_dados.json")
        self.__codigo = codigo
        self.__nome = nome
        self.__senha = senha
        self.__data_de_nascimento = self.validate_data_de_nascimento(data_de_nascimento)
        self.__email = self.validate_novo_email(email)
        self.__is_ativo = self.validate_is_ativo(is_ativo)

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
      if validate_inteiro(novo_codigo):
            self.__codigo = novo_codigo

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
        if validate_data(nova_data_de_nascimento):
            self.__data_de_nascimento = nova_data_de_nascimento

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        if validate_email(novo_email):
            self.__email = novo_email

    @property
    def is_ativo(self):
        return self.__is_ativo
    
    @is_ativo.setter
    def is_ativo(self, novo_is_ativo):
        if validate_bool(novo_is_ativo):
            self.__is_ativo = novo_is_ativo


    def validate_is_ativo(self, is_ativo):
        if validate_bool(is_ativo):
            return is_ativo

    def validate_data_de_nascimento(self, data_de_nascimento):
        if validate_data(data_de_nascimento):
            return data_de_nascimento
        
    def validate_novo_email(self, novo_email):
        if validate_email(novo_email):
            return novo_email
        
if __name__ == "__main__":

    pessoa1 = Pessoa(1, "Raul", "1234", "18/09/1997","raul@raul.com", True)
    print(pessoa1.nome)
    print(pessoa1.data_de_nascimento)

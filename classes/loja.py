import sys
sys.path.insert(1, 'POO/util')
from util import *



class Loja:
    def __init__(self, cnpj, nome, email):
        self.__codigo_loja = None
        self.__cnpj = self.validate_cnpj(cnpj)
        self.__nome = self.validate_nome(nome)
        self.__email = self.validate_email(email)

    @property
    def codigo_loja(self):
        return self.__codigo_loja
    
    @codigo_loja.setter
    def codigo_loja(self, codigo_loja):
        if validate_inteiro(codigo_loja):
            self.__codigo_loja = codigo_loja
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        if validate_string(cnpj):
            self.__cnpj = cnpj
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if validate_string(nome):
            self.__nome = nome
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if validate_email(email):
            self.__email = email

    def validate_cnpj(self, cnpj):
        if validate_string(cnpj):
            return cnpj
        
    def validate_nome(self, nome):
        if validate_string(nome):
            return nome
        
    def validate_email(self, email):
        if validate_email(email):
            return email
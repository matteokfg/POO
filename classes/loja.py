import sys
sys.path.insert(1, 'POO/util')
from util import validate_inteiro



class Loja:
    def __init__(self, cnpj, nome, email):
        self.__codigo_loja = None
        self.__cnpj = validate_inteiro(cnpj)
        self.__nome = validate_inteiro(nome)
        self.__email = validate_inteiro(email)

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
        if validate_inteiro(cnpj):
            self.__cnpj = cnpj
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if validate_inteiro(nome):
            self.__nome = nome
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if validate_inteiro(email):
            self.__email = email
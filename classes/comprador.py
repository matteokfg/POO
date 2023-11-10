from pessoa import Pessoa
from endereco import Endereco
from util import *

class Comprador(Pessoa, Endereco):

    def __init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo,
                 logradouro, numero, complemento, cidade, uf, cep, cpf, rg, cartao):
        Pessoa.__init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo)
        Endereco.__init__(self, logradouro, numero, complemento, cidade, uf, cep)
        self.__cpf = cpf
        self.__rg = rg
        self.__cartao = cartao

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def rg(self):
        return self.__rg
    
    @rg.setter
    def rg(self, novo_rg):
        self.__rg = novo_rg
    
    @property
    def cartao(self):
        return self.__cartao
    
    @cartao.setter
    def cartao(self, novo_cartao):
        self.__cartao = novo_cartao




    
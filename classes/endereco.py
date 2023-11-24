from connector import Connector
from util import validate_inteiro, validate_cep, path_banco

class Endereco(Connector):
    def __init__(self, codigo, logradouro, numero, complemento, cidade, uf, cep, codigo_comprador):
        Connector.__init__(self, path_banco)
        self.__codigo = self.validate_codigo(codigo)
        self.__logradouro = logradouro
        self.__numero = self.validate_numero(numero)
        self.__complemento = complemento
        self.__cidade = cidade
        self.__uf = uf
        self.__cep = self.validate_this_cep(cep)
        self.__codigo_comprador = self.validate_codigo(codigo_comprador)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        if validate_inteiro(novo_codigo):
            self.__codigo = novo_codigo

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, novo_logradouro):
        self.__logradouro = novo_logradouro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        if validate_inteiro(novo_numero):
            self.__numero = novo_numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, novo_complemento):
        self.__complemento = novo_complemento

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, nova_cidade):
        self.__cidade = nova_cidade

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, novo_uf):
        self.__uf = novo_uf

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, novo_cep):
        if validate_cep(novo_cep):
            self.__cep = novo_cep

    @property
    def codigo_comprador(self):
        return self.__codigo_comprador

    @codigo_comprador.setter
    def codigo_comprador(self, novo_codigo_comprador):
        if validate_inteiro(novo_codigo_comprador):
            self.__codigo_comprador = novo_codigo_comprador

    def validate_numero(self, numero):
        if validate_inteiro(numero):
            return numero

    def validate_this_cep(self, cep):
        if validate_cep(cep):
            return cep

    def validate_codigo(self, codigo):
        if validate_inteiro(codigo):
            return codigo

    def listar(self):
        return self.listar_tabela("Endereco")
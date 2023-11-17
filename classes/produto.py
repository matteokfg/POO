from connector import Connector
from util import validate_inteiro, validate_float, path_banco

class Produto(Connector):
    def __init__(self, codigo, nome, descricao, imagem, preco_unitario, tipo, marca, quantidade, codigo_loja):
        Connector.__init__(self, path_banco)
        self.__codigo = self.validate_codigo(codigo)
        self.__nome = nome
        self.__descricao = descricao
        self.__imagem = imagem
        self.__preco_unitario = self.validate_preco_unitario(preco_unitario)
        self.__tipo = tipo
        self.__marca = marca
        self.__quantidade = self.validate_quantidade(quantidade)
        self.__codigo_loja = self.validate_codigo(codigo_loja)

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
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, novo_descricao):
        self.__descricao = novo_descricao

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, novo_imagem):
        self.__imagem = novo_imagem

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, novo_preco_unitario):
        if validate_float(novo_preco_unitario):
            self.__preco_unitario = novo_preco_unitario

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, novo_marca):
        self.__marca = novo_marca

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if validate_inteiro(nova_quantidade):
            self.__quantidade = nova_quantidade

    @property
    def codigo_loja(self):
        return self.__codigo_loja

    @codigo_loja.setter
    def codigo_loja(self, novo_codigo_loja):
        if validate_inteiro(novo_codigo_loja):
            self.__codigo_loja = novo_codigo_loja

    def validate_codigo(self, codigo):
        if validate_inteiro(codigo):
            return codigo
        
    def validate_quantidade(self, quantidade):
        if validate_inteiro(quantidade):
            return quantidade

    def validate_preco_unitario(self, preco_unitario):
        if validate_float(preco_unitario):
            return preco_unitario
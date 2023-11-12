from connector import Connector

class Produto(Connector):
    def __init__(self, codigo, nome, descricao, imagem, preco_unitario, tipo, marca, codigo_loja):
        Connector.__init__("banco_de_dados.json")
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__imagem = imagem
        self.__preco_unitario = preco_unitario
        self.__tipo = tipo
        self.__marca = marca
        self.__codigo_loja = codigo_loja

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
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
    def codigo_loja(self):
        return self.__codigo_loja
    
    @codigo_loja.setter
    def codigo_loja(self, novo_codigo_loja):
        self.__codigo_loja = novo_codigo_loja

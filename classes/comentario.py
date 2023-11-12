from connector import Connector

class Comentario(Connector):
    def __init__(self, codigo, codigo_comprador, codigo_produto, codigo_loja, descricao):
        Connector.__init__("banco_de_dados.json")
        self.__codigo = codigo
        self.__codigo_comprador = codigo_comprador
        self.__codigo_produto = codigo_produto
        self.__codigo_loja = codigo_loja
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def codigo_comprador(self):
        return self.__codigo_comprador

    @codigo_comprador.setter
    def codigo_comprador(self, novo_codigo_comprador):
        self.__codigo_comprador = novo_codigo_comprador

    @property
    def codigo_produto(self):
        return self.__codigo_produto

    @codigo_produto.setter
    def codigo_produto(self, novo_codigo_produto):
        self.__codigo_produto = novo_codigo_produto

    @property
    def codigo_loja(self):
        return self.__codigo_loja

    @codigo_loja.setter
    def codigo_loja(self, novo_codigo_loja):
        self.__codigo_loja = novo_codigo_loja

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, novo_descricao):
        self.__descricao = novo_descricao

    def comentarios_produto(self):
        pass

    def comentarios_loja(self):
        pass

    def comentarios_comprador(self):
        pass
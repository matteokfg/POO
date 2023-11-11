from connector import Connector

class Comentario(Connector):
    def __init__(self, codigo, codigo_comprador, codigo_produto, codigo_loja, descricao):
        Connector.__init__("banco_de_dados.json")
        self.__codigo = codigo
        self.__codigo_comprador = codigo_comprador
        self.__codigo_produto = codigo_produto
        self.__codigo_loja = codigo_loja
        self.__descricao = descricao

    def comentarios_produto(self):
        pass

    def comentarios_loja(self):
        pass

    def comentarios_comprador(self):
        pass
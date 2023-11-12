from connector import Connector

class Pedido(Connector):
    def __init__(self, codigo, codigos_produtos, quantidades, codigo_comprador, codigos_lojas):
        Connector.__init__("banco_de_dados.json")
        self.__codigo = codigo
        self.__codigos_produtos = codigos_produtos
        self.__quantidades = quantidades
        self.__codigo_comprador = codigo_comprador
        self.__codigos_lojas = codigos_lojas

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def codigos_produtos(self):
        return self.__codigos_produtos
    
    @codigos_produtos.setter
    def codigos_produtos(self, novo_codigos_produtos):
        self.__codigos_produtos = novo_codigos_produtos

    @property
    def quantidades(self):
        return self.__quantidades
    
    @quantidades.setter
    def quantidades(self, novo_quantidades):
        self.__quantidades = novo_quantidades

    @property
    def codigo_comprador(self):
        return self.__codigo_comprador
    
    @codigo_comprador.setter
    def codigo_comprador(self, novo_codigo_comprador):
        self.__codigo_comprador = novo_codigo_comprador

    @property
    def codigos_lojas(self):
        return self.__codigos_lojas
    
    @codigos_lojas.setter
    def codigos_lojas(self, novo_codigos_lojas):
        self.__codigos_lojas = novo_codigos_lojas

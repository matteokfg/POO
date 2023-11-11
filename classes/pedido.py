from connector import Connector

class Pedido(Connector):
    def __init__(self, codigo, codigos_produtos, quantidades, codigo_comprador, codigos_lojas):
        Connector.__init__("banco_de_dados.json")
        self.__codigo = codigo
        self.__codigos_produtos = codigos_produtos
        self.__quantidades = quantidades
        self.__codigo_comprador = codigo_comprador
        self.__codigos_lojas = codigos_lojas

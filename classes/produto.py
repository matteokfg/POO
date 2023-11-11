from connector import Connector

class Produto(Connector):
    def __init__(self, codigo, nome, descricao, imagem, preco_unitario, tipo, marca, codigo_loja):
        Connector.__init__("../banco_de_dados.json")
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__imagem = imagem
        self.__preco_unitario = preco_unitario
        self.__tipo = tipo
        self.__marca = marca
        self.__codigo_loja = codigo_loja

from connector import Connector

class Produto(Connector):
    def __init__(self, codigo, nome, descricao, imagem, preco_unitario, tipo, marca, codigo_loja):
        Connector.__init__("../banco_de_dados.json")
        
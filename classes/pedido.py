from connector import Connector
from util import validate_inteiro, validate_float

class Pedido(Connector):
    def __init__(self, codigo, codigos_produtos, quantidades, codigo_comprador, codigos_lojas):
        Connector.__init__("banco_de_dados.json")
        self.__codigo = self.validate_codigo(codigo)
        self.__codigos_produtos = self.validate_lista_codigos(codigos_produtos)
        self.__quantidades = self.validate_lista_quantidades(quantidades)
        self.__codigo_comprador = self.validate_codigo(codigo_comprador)
        self.__codigos_lojas = self.validate_lista_codigos(codigos_lojas)

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        if validate_inteiro(novo_codigo):
            self.__codigo = novo_codigo

    @property
    def codigos_produtos(self):
        return self.__codigos_produtos
    
    @codigos_produtos.setter
    def codigos_produtos(self, novo_codigos_produtos):
        for novo_codigo_produto in novo_codigos_produtos:
            if validate_inteiro(novo_codigo_produto):
                continue
        self.__codigos_produtos = novo_codigos_produtos

    @property
    def quantidades(self):
        return self.__quantidades
    
    @quantidades.setter
    def quantidades(self, novo_quantidades):
        for novo_quantidade in novo_quantidades:
            if validate_float(novo_quantidade):
                continue
        self.__quantidades = novo_quantidades

    @property
    def codigo_comprador(self):
        return self.__codigo_comprador
    
    @codigo_comprador.setter
    def codigo_comprador(self, novo_codigo_comprador):
        if validate_inteiro(novo_codigo_comprador):
            self.__codigo_comprador = novo_codigo_comprador

    @property
    def codigos_lojas(self):
        return self.__codigos_lojas
    
    @codigos_lojas.setter
    def codigos_lojas(self, novo_codigos_lojas):
        for novo_codigo_loja in novo_codigos_lojas:
            if validate_inteiro(novo_codigo_loja):
                continue
        self.__codigos_lojas = novo_codigos_lojas

    def validate_codigo(self, codigo):
        if validate_inteiro(codigo):
            return codigo
        
    def validate_lista_codigos(self, codigos):
        for codigo in codigos:
            if validate_inteiro(codigo):
                continue

    def validate_lista_quantidades(self, quantidades):
        for quantidade in quantidades:
            if validate_float(quantidade):
                continue
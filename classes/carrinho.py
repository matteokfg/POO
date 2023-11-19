from util import validate_inteiro, validate_float, validate_lista_inteiros, path_banco
from connector import Connector
from tkinter import messagebox

class Carrinho:
    def __init__(self, codigo, codigos_produtos, quantidades, codigo_comprador, codigos_lojas):
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
        validate_lista_inteiros(codigos)

    def validate_lista_quantidades(self, quantidades):
        validate_lista_inteiros(quantidades)

    def preco_total(self):
        total = 0
        lista_precos_unicos = []
        c = Connector(path_banco)
        for codigo_produto in self.__codigos_produtos:
            produto = c.procurar("Produto", codigo_produto)
            if produto is not None:
                lista_precos_unicos.append(produto['preco_unitario'])
        try:
            for preco, quantidade in zip(lista_precos_unicos, self.__quantidades):
                total += (preco * quantidade)
        except:
            print("Algum produto nao foi encontrado!")
        return total

    def adicionar_ao_carrinho(self, codigo_produto, quantidade, codigo_loja):
        if validate_inteiro(codigo_produto) and validate_inteiro(quantidade) and validate_inteiro(codigo_loja):
            self.__codigos_produtos.append(codigo_produto)
            self.__quantidades.append(quantidade)
            self.__codigos_lojas.append(codigo_loja)
        else:
            return None
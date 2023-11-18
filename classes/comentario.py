from connector import Connector
from util import validate_inteiro, path_banco

class Comentario(Connector):
    def __init__(self, codigo, codigo_comprador, codigo_produto, codigo_loja, descricao):
        Connector.__init__(path_banco)
        self.__codigo = self.validate_codigo(codigo)
        self.__codigo_comprador = self.validate_codigo(codigo_comprador)
        self.__codigo_produto = self.validate_codigo(codigo_produto)
        self.__codigo_loja = self.validate_codigo(codigo_loja)
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        if validate_inteiro(novo_codigo):
            self.__codigo = novo_codigo

    @property
    def codigo_comprador(self):
        return self.__codigo_comprador

    @codigo_comprador.setter
    def codigo_comprador(self, novo_codigo_comprador):
        if validate_inteiro(novo_codigo_comprador):
            self.__codigo_comprador = novo_codigo_comprador

    @property
    def codigo_produto(self):
        return self.__codigo_produto

    @codigo_produto.setter
    def codigo_produto(self, novo_codigo_produto):
        if validate_inteiro(novo_codigo_produto):
            self.__codigo_produto = novo_codigo_produto

    @property
    def codigo_loja(self):
        return self.__codigo_loja

    @codigo_loja.setter
    def codigo_loja(self, novo_codigo_loja):
        if validate_inteiro(novo_codigo_loja):
            self.__codigo_loja = novo_codigo_loja

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, novo_descricao):
        self.__descricao = novo_descricao

    def validate_codigo(self, codigo):
        if validate_inteiro(codigo):
            return codigo

    def comentarios_produto(self):
        comentarios = self.listar("Comentario")
        comentarios_produtos = [comentario for comentario in comentarios if comentario["codigo_produto"] == self.__codigo_produto]
        return comentarios_produtos

    def comentarios_loja(self):
        comentarios = self.listar("Comentario")
        comentarios_produtos = [comentario for comentario in comentarios if comentario["codigo_loja"] == self.__codigo_loja]
        return comentarios_produtos

    def comentarios_comprador(self):
        comentarios = self.listar("Comentario")
        comentarios_produtos = [comentario for comentario in comentarios if comentario["codigo_comprador"] == self.__codigo_comprador]
        return comentarios_produtos

    def listar(self):
        return self.listar_tabela("Comentario")
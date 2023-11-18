from pessoa import Pessoa
from util import validate_inteiro

class Vendedor(Pessoa):
    def __init__(self, codigo, nome, senha, data_nascimento, email, is_ativo, codigo_loja):
        Pessoa.__init__(self, codigo, nome, senha, data_nascimento, email, is_ativo)
        self.__codigo_loja = self.validate_codigo_loja(codigo_loja)

    @property
    def codigo_loja(self):
        return self.__codigo_loja

    @codigo_loja.setter
    def codigo_loja(self, codigo_loja):
        if validate_inteiro(codigo_loja):
            self.__codigo_loja = codigo_loja

    def validate_codigo_loja(self, codigo_loja):
        if validate_inteiro(codigo_loja):
            return codigo_loja

    def listar(self):
        return self.listar_tabela("Vendedor")
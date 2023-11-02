from pessoa import Pessoa

import sys
sys.path.insert(1, 'POO/util')

from util import validate_inteiro

class Vendedor(Pessoa):
    def __init__(self, codigo, nome, senha, data_nascimento, email, is_ativo, codigo_loja):
        super().__init__(codigo, nome, senha, data_nascimento, email, is_ativo)
        self.__codigo_loja = self.validate_codigo_loja(codigo_loja)

    def set_codigo_loja(self, codigo_loja):
        self.__codigo_loja = validate_inteiro(codigo_loja)

    def get_codigo_loja(self):
        return self.__codigo_loja
    
    def validate_codigo_loja(self, codigo_loja):
        if validate_inteiro(codigo_loja):
            return codigo_loja



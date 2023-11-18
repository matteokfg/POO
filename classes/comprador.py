from pessoa import Pessoa
from endereco import Endereco
from util import validate_cpf, validate_string

class Comprador(Pessoa, Endereco):
    def __init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo,
                 logradouro, numero, complemento, cidade, uf, cep, cpf, rg, cartao):
        Pessoa.__init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo)
        Endereco.__init__(self, logradouro, numero, complemento, cidade, uf, cep)
        self.__cpf = self.validate_this_cpf(cpf)
        self.__rg = self.validate_rg(rg)
        self.__cartao = cartao

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if validate_cpf(novo_cpf):
            self.__cpf = novo_cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, novo_rg):
        if validate_string(novo_rg):
            self.__rg = novo_rg

    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, novo_cartao):
        self.__cartao = novo_cartao

    def validate_this_cpf(self, cpf):
        if validate_cpf(cpf):
            return cpf

    def validate_rg(self, rg):
        if validate_string(rg):
            return rg

    def listar(self):
        return self.listar_tabela("Comprador")
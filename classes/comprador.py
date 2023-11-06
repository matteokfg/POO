from pessoa import Pessoa
from endereco import Endereco
from util import *

class Comprador(Pessoa, Endereco):

    def __init__(self, codigo, nome, senha, data_de_nascimento, email, is_ativo,
                 logradouro, numero, complemento, cidade, uf, cep, cpf, rg, cartao):
        Pessoa.__init__(codigo, nome, senha, data_de_nascimento, email, is_ativo)
        Endereco.__init__(logradouro, numero, complemento, cidade, uf, cep)
        self.__cpf = cpf
        self.__rg = rg
        self.__cartao = cartao

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def rg(self):
        return self.__rg
    
    @rg.setter
    def rg(self, novo_rg):
        self.__rg = novo_rg
    
    @property
    def cartao(self):
        return self.__cartao
    
    @cartao.setter
    def cartao(self, novo_cartao):
        self.__cartao = novo_cartao

    def incluir_banco(self):

        # Carregar o conteúdo do arquivo JSON em um objeto Python
        with open(dados_comprador) as f:
            data = json.load(f)

        # Imprimir todos os ids cadastrados
        for item in data:
            print(item['codigo'])

        # Insere novo cadastro
        with open(dados_comprador, 'a', encoding='utf-8') as f:
            novo_cliente = {'codigo': self.__codigo,
                            'nome': self.__nome,
                            'senha': self.__senha,
                            'data_de_nascimento': self.__data_de_nascimento,
                            'email': self.__email,
                            'is_ativo': self.__is_ativo,
                            'logradouro': self.__logradouro,
                            'numero': self.__numero,
                            'complemento': self.__complemento,
                            'cidade': self.__cidade,
                            'uf': self.__uf,
                            'cep': self.__cep,
                            'cpf': self.__cpf,
                            'rg': self.__rg,
                            'cartao': self.__cartao}
            json.dump(novo_cliente, f)



    
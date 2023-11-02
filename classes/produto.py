from loja import Loja

class Produto(Loja):

    def __init__(self, cnpj, nome, email):
        super().__init__(cnpj, nome, email)
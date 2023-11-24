from util import validate_inteiro, validate_float, validate_forma_pagamento, path_banco
from connector import Connector
from compra import Compra
from tkinter import messagebox


class Pedido(Connector, Compra):
    def __init__(self, codigo, codigos_produtos, quantidades, codigo_comprador, codigos_lojas, forma_pagamento):
        Connector.__init__(self, path_banco)
        self.__codigo = self.validate_codigo(codigo)
        self.__codigos_produtos = self.validate_lista_inteiros(codigos_produtos)
        self.__quantidades = self.validate_lista_inteiros(quantidades)
        self.__codigo_comprador = self.validate_codigo(codigo_comprador)
        self.__codigos_lojas = self.validate_lista_inteiros(codigos_lojas)
        self.__forma_pagamento = self.validate_pagamento(forma_pagamento)

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, nova_forma_pagamento):
        if validate_forma_pagamento(nova_forma_pagamento):
            self.__forma_pagamento = nova_forma_pagamento

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
        
    def validate_pagamento(self, fp):
        if validate_forma_pagamento(fp):
            return fp

    def validate_lista_inteiros(self, inteiros):
        validado = []
        for inteiro in inteiros:
            if validate_inteiro(inteiro):
                validado.append(True)
            else:
                validado.append(False)
        if False in validado:
            messagebox.showerror('',"Inteiro invalido!")
        else:
            return inteiros

    def listar(self):
        return self.listar_tabela("Pedido")
    
# Teste

if __name__ == "__main__":
        
    
    tipo = "Pedido"
    
    pedido = Pedido(codigo=0, 
                    codigos_produtos=[0], 
                    quantidades=[0], 
                    codigo_comprador=0, 
                    codigos_lojas=[0], 
                    forma_pagamento="Boleto")
    
    for ped in pedido.listar():
        if 2 in ped['codigos_lojas']:
            print(ped)
        
        
    input()
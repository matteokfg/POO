class Endereco:

    def __init__(self, logradouro, numero, complemento, cidade, uf, cep):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__uf = uf
        self.__cep = cep

    @property
    def logradouro(self):
        return self.__logradouro
    
    @logradouro.setter
    def logradouro(self, novo_logradouro):
        self.__logradouro = novo_logradouro

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    @property
    def complemento(self):
        return self.__complemento
    
    @complemento.setter
    def complemento(self, novo_complemento):
        self.__complemento = novo_complemento

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, nova_cidade):
        self.__cidade = nova_cidade

    @property
    def uf(self):
        return self.__uf
    
    @uf.setter
    def uf(self, novo_uf):
        self.__uf = novo_uf

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, novo_cep):
        self.__cep = novo_cep


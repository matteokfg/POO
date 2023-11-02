
class Loja:
    def __init__(self, cnpj, nome, email):
        self.__id_loja = None
        self.__cnpj = cnpj
        self.__nome = nome
        self.__email = email

    def get_id_loja(self):
        return self.__id_loja
    
    def set_id_loja(self, id_loja):
        self.__id_loja = id_loja
    
    def get_cnpj(self):
        return self.__cnpj
    
    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
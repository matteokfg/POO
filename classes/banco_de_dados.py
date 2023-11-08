from util import banco
import json

class Banco:

    def __init__(self):
         pass

    def inserir(self, dados, tipo):
        with open(banco, "r", encoding='utf-8') as file:
            data = json.load(file)

        data[tipo].append(dados)


        with open(banco, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

# Teste
if __name__ == "__main__":

        novo_comprador = {
            "codigo": 2,
            "nome": "Novo Comprador",
            "senha": "nova_senha",
            "data_de_nascimento": "1990-01-01",
            "email": "novo@email.com",
            "is_ativo": True,
            "cpf": "12345678901",
            "rg": "1234567",
            "logradouro": "Rua Nova, 123",
            "numero": "456",
            "complemento": "Apto 4B",
            "cidade": "Nova Cidade",
            "uf": "NC",
            "cep": "12345-678",
            "cartao": "1234-5678-9012-3456",
        }
        db = Banco()
        db.inserir(novo_comprador, "comprador")
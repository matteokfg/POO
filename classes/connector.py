# connector com o banco de dados bruto, necessário ajustar
import json

class Connector:
    def __init__(self, path_bd) -> None:
        self.__path_bd = path_bd

    @property
    def path_bd(self):
        return self.__path_bd
    
    @path_bd.setter
    def path_bd(self, nova_path):
        self.__path_bd = nova_path

    def criar(self, tipo, **kwargs):
        if tipo in ['Vendedor', 'Comprador']:
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario

            coluna_banco = data["BD"][tipo] #escolho a coluna
            try:
                codigo_ultimo = coluna_banco[-1]["Codigo"]  #pego o codigo da ultima conta
            except IndexError:
                codigo_ultimo = 0

            kwargs_to_args = list(kwargs.items())
            kwargs_to_args.insert(0, ("Codigo", codigo_ultimo + 1))
            kwargs = dict(kwargs_to_args)
            coluna_banco.append(kwargs)    #salvo a conta no ultimo lugar da coluna
            with open(self.path_bd, 'w') as bd_json:
                json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            return True
        else:
            return None

    def procurar(self, tipo, codigo):
        if tipo in ['Vendedor', 'Comprador']:
            objeto_existente = False
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario
            coluna = data["BD"][tipo] #escolho a coluna
            for objeto in coluna:
                if objeto["Codigo"] == codigo:
                    objeto_existente = objeto
            if not objeto_existente:
                print("Objeto nao encontrado!")
            return objeto_existente
        else:
            return None

    def atualizar(self, tipo, codigo, **kwargs):
        if tipo in ['Vendedor', 'Comprador']:
            certo = False
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario
            coluna = data["BD"][tipo] #escolho a coluna
            lugar = -1
            for index, objeto in enumerate(coluna):
                if objeto["Codigo"] == codigo:
                    lugar = index
            if lugar != -1:
                for key, value in enumerate(kwargs.items()):
                    objeto[lugar][key] = value
                certo = True
            else:
                print("Objeto nao encontrado!")
            with open(self.path_bd, 'w') as bd_json:
                json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            return certo
        else:
            return None

    def deletar(self, tipo, codigo):
        if tipo in ['Vendedor', 'Comprador']:
            certo = False
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario
            coluna = data["BD"][tipo] #escolho a coluna
            lugar = -1
            for index, objeto in enumerate(coluna):
                if objeto["Codigo"] == codigo:
                    lugar = index
            if lugar != -1:
                coluna.pop(lugar)
                certo = True
            else:
                print("Objeto nao encontrado!")
            with open(self.path_bd, 'w') as bd_json:
                json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            return certo
        else:
            return None

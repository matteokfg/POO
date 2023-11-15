import json

class Connector:
    def __init__(self, path_bd) -> None:
        self.__path_bd = path_bd
        self.__lista_tabelas = ["Vendedor", "Comprador", "Comentario", "Endereco", "Loja", "Pedido", "Produto"]

    @property
    def path_bd(self):
        return self.__path_bd
    
    @path_bd.setter
    def path_bd(self, nova_path):
        self.__path_bd = nova_path

    @property
    def lista_tabelas(self):
        return self.__lista_tabelas

    def criar(self, tipo, **kwargs):
        if tipo in self.__lista_tabelas:
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario

            tabela_banco = data["BD"][tipo] #escolho a tabela
            try:
                codigo_ultimo = tabela_banco[-1]["Codigo"]  #pego o codigo da ultima conta
            except IndexError:
                codigo_ultimo = 0

            kwargs_to_args = list(kwargs.items())
            kwargs_to_args.insert(0, ("Codigo", codigo_ultimo + 1)) # adiciono o Codigo ao dicionario
            kwargs = dict(kwargs_to_args)
            tabela_banco.append(kwargs)    #salvo a conta no ultimo lugar da tabela
            with open(self.path_bd, 'w') as bd_json:
                json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            return True
        else:
            return None

    def procurar(self, tipo, codigo):
        if tipo in self.__lista_tabelas:
            objeto_existente = False
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario
            tabela = data["BD"][tipo] #escolho a tabela
            for objeto in tabela:
                if objeto["Codigo"] == codigo:
                    objeto_existente = objeto
            if not objeto_existente:
                print("Objeto nao encontrado!")
            return objeto_existente
        else:
            return None

    def atualizar(self, tipo, codigo, **kwargs):
        if tipo in self.__lista_tabelas:
            atualizado = False
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario
            tabela = data["BD"][tipo] #escolho a tabela
            lugar = -1
            for index, objeto in enumerate(tabela):
                if objeto["Codigo"] == codigo:
                    lugar = index
            if lugar != -1:
                for key, value in enumerate(kwargs.items()):
                    objeto[lugar][key] = value
                atualizado = True
            else:
                print("Objeto nao encontrado!")
            with open(self.path_bd, 'w') as bd_json:
                json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            return atualizado
        else:
            return None

    def deletar(self, tipo, codigo):
        if tipo in self.__lista_tabelas:
            deletado = False
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)   #transformo json em dicionario
            tabela = data["BD"][tipo] #escolho a tabela
            lugar = -1
            for index, objeto in enumerate(tabela):
                if objeto["Codigo"] == codigo:
                    lugar = index
            if lugar != -1:
                tabela.pop(lugar)
                deletado = True
            else:
                print("Objeto nao encontrado!")
            with open(self.path_bd, 'w') as bd_json:
                json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            return deletado
        else:
            return None

    def listar(self, tipo):
        if tipo in self.__lista_tabelas:
            with open(self.path_bd) as bd_json:
                data = json.load(bd_json)
            tabela = data["BD"][tipo]
            return tabela
        else:
            return None

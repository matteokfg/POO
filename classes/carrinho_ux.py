from util_ux import *

class Carrinho:

    def __init__(self, root, master, carrinho):
        self.root = root
        self.master = master
        self.carrinho = carrinho
        self.ux()

    def ux_tabela_carrinho(self):

        coldata = [
            "Código",
            "Nome",
            "Descrição",
            "Tipo",
            "Marca",
            "Código Loja",
            "Loja",
            "Quantidade",
            "Preço unitário"
        ]

        rowdata = []

        for prod in produto.listar():
            connector = Connector(path_banco)
            result = connector.procurar("Loja", prod["codigo_loja"], coluna="codigo")
            rowdata.append((prod["codigo"],prod["nome"],prod["descricao"],prod["tipo_produto"],prod["marca"],prod["codigo_loja"],result["nome"],prod["quantidade"],prod["preco_unitario"]))


        self.dt = Tableview(
            master=frm_tabela,
            coldata=coldata,
            rowdata=rowdata,
            paginated=False,
            searchable=False,
            bootstyle="primary",
            height=20
        )
        self.dt.pack(side='left', fill='x', expand=True, anchor="w")

        verscrlbar = ttk.Scrollbar(frm_tabela, 
                           orient ="vertical", 
                           command = self.dt.view.yview)
        verscrlbar.pack(side='right', fill='y')
        self.dt.view.configure(yscrollcommand = verscrlbar.set)
        self.dt.view.bind("<<TreeviewSelect>>", lambda e: self.bind_atualiza_campos())
        self.dt.view['displaycolumns'] = ('0', '1', '2', '3', '4', '6', '7', '8')

    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        ttk.Label(self.frm_principal, text="Carrinho", font=(None,16))

        
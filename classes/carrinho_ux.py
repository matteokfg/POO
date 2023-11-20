from util_ux import *

class Tela_carrinho:

    def __init__(self, root, master, params_carrinho):
        self.root = root
        self.master = master
        self.params_carrinho = params_carrinho
        self.ux()

    def ux_tabela_carrinho(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(anchor="n", fill="both", padx=150)

        produto = Produto(codigo=0,
                    nome="Nome",
                    descricao="Descricao",
                    imagem="a",
                    preco_unitario=2.0,
                    tipo_produto="tipo",
                    marca="marca",
                    quantidade=0,
                    codigo_loja=0)

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

        for n, item in enumerate(self.params_carrinho["codigos_produto"]):

            for prod in produto.listar():
                connector = Connector(path_banco)
                result = connector.procurar("Loja", prod["codigo_loja"], coluna="codigo")
                if self.params_carrinho["codigos_produto"][n] == prod["codigo"] and self.params_carrinho["codigos_loja"][n] == prod["codigo_loja"]:
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
        #self.dt.view.bind("<<TreeviewSelect>>", lambda e: self.bind_atualiza_campos())
        self.dt.view['displaycolumns'] = ('0', '1', '2', '3', '4', '6', '7', '8')

    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        ttk.Label(self.frm_principal, text="Carrinho", font=(None,16)).pack()
        if len(self.params_carrinho) > 0:
            self.ux_tabela_carrinho()
        else:
            ttk.Label(self.frm_principal, text="Você ainda não tem produtos adicionado ao carrinho!", font=(None,10)).pack(pady=30)
            ttk.Button(self.frm_principal, text="Voltar", bootstyle="secondary-outline" ,command=self.root.destroy).pack()

        
from util_ux import *

class Tela_detalhes_pedido:

    def __init__(self, root, master, pedido, perfil):
        self.root = root
        self.root.state('zoomed')
        self.root.grab_set()
        self.master = master
        self.tipo = "Pedido"
        self.pedido = pedido
        self.perfil = perfil
        self.ux()


    def ux_tabela_detalhes(self):

        frm_tabela = ttk.Frame(self.frm_principal); frm_tabela.pack(anchor="n", fill="both", padx=150)
        preco_total = 0
        

        rowdata = []
    
        for ped in self.pedido.listar():
            if self.perfil.codigo_loja in ped['codigos_lojas']:
                connector = Connector(path_banco)
                for s, cod_produto in enumerate(ped['codigos_produtos']):
                    connector = Connector(path_banco)
                    result = connector.procurar("Produto", cod_produto, coluna="codigo")
                    result2 = connector.procurar("Comprador", ped['codigo_comprador'], coluna="codigo")
                    rowdata.append((result["codigo"],result["nome"],result["descricao"],result["tipo_produto"],result["marca"],result["codigo_loja"],result2["nome"],ped["quantidades"][s],result["preco_unitario"]))
                    preco_total = preco_total + (ped["quantidades"][s] * result["preco_unitario"])

        coldata = [
            "Código",
            "Nome",
            "Descrição",
            "Tipo",
            "Marca",
            "Código Loja",
            "Comprador",
            "Quantidade",
            "Preço unitário"
        ]

        



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

        frm_btns = ttk.Frame(self.frm_principal); frm_btns.pack(anchor="w", fill="x", padx=(150,0), pady=20)
        ttk.Label(frm_btns, text=f"Preço Total (R$): {preco_total}", font=(None,16)).pack(side="left")
        ttk.Label(frm_btns, text=f"{0}".replace('.',','), font=(None,16)).pack(side="left")
        ttk.Button(frm_btns, text="Voltar", bootstyle="dark-outline", command=self.root.destroy).pack(side="left", padx=(10,10))
        

    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        self.lbl = ttk.Label(self.frm_principal, text=f"Pedido {self.pedido.codigo}", font=(None,16)); self.lbl.pack()
        self.ux_tabela_detalhes()

        
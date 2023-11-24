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
        ttk.Label(frm_btns, text="Preço Total (R$): ", font=(None,16)).pack(side="left")
        ttk.Label(frm_btns, text=f"{0}".replace('.',','), font=(None,16)).pack(side="left")
        ttk.Button(frm_btns, text="Voltar", bootstyle="dark-outline", command=self.root.destroy).pack(side="left", padx=(10,10))
        mb=ttk.Menubutton(frm_btns,text='Ação', bootstyle="primary");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        mb.menu.add_command(label='Finalizar pedido')
        

    def ux(self):
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", anchor='n')
        ttk.Label(self.frm_principal, text="Pedido {}", font=(None,16)).pack()
        self.ux_tabela_detalhes()

        
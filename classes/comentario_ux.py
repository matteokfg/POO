from util_ux import *

class Tela_comentario:

    def __init__(self, root, master, tipo, **kwargs):
        
        self.root = root
        self.master = master
        self.root.grab_set()
        self.root.minsize(800,600)
        self.tipo = tipo
        self.kwargs = kwargs
        self.inicializa_variaveis()
        self.ux()
        self.carregar_comentarios()

    def inicializa_variaveis(self):
        self.var_comentario = ttk.StringVar()

    def carregar_comentarios(self):
        
        comentario = Comentario(codigo=0,
                                codigo_comprador=self.kwargs["perfil"].codigo,
                                codigo_produto=self.kwargs["codigo_produto"],
                                codigo_loja=self.kwargs["codigo_loja"],
                                descricao="")
        
        print('\n',
              comentario.codigo_comprador,
              '\n',
              comentario.codigo_produto,
              '\n',
              comentario.codigo_loja,
              '\n',
              comentario.descricao)

    def ux(self):

        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", padx=20, pady=20)
        ttk.Label(self.frm_principal, text="Comentários", font=(None,14)).pack()
        self.scrl = ttk.ScrolledText(self.frm_principal); self.scrl.pack(fill="both")
        frm_add_comentario = ttk.Frame(self.frm_principal); frm_add_comentario.pack(fill="x", expand=True)
        ttk.Entry(frm_add_comentario, textvariable=self.var_comentario).pack(fill="x", side="left", expand=True, pady=10)
        ttk.Button(frm_add_comentario, text="Enviar comentário").pack(padx=(10,0), side="left")
        ttk.Button(self.frm_principal, text="Voltar", bootstyle="secondary-outline", command=self.root.destroy).pack(pady=10)
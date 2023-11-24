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
        
    def fun_enviar_comentario(self):
        self.scrl['state'] = "normal"
        self.comentario.descricao = self.var_comentario.get()
        
        params_comentario= dict(
              codigo_comprador = self.comentario.codigo_comprador,
              codigo_produto = self.comentario.codigo_produto,
              codigo_loja = self.comentario.codigo_loja,
              descricao = self.comentario.descricao,
              )
        
        for dado in params_comentario:
            if params_comentario[dado] == None:
                return
            
        self.comentario.criar(self.tipo, **params_comentario)
        self.scrl.insert("insert", f"{self.kwargs['perfil'].nome}: {self.comentario.descricao}\n")
        self.scrl['state'] = "disabled"

    def carregar_comentarios(self):
        
        self.scrl['state'] = "normal"
        
        self.comentario = Comentario(codigo=0,
                                codigo_comprador=self.kwargs["perfil"].codigo,
                                codigo_produto=self.kwargs["codigo_produto"],
                                codigo_loja=self.kwargs["codigo_loja"],
                                descricao="")
        
        connector = Connector(path_banco)
        for comt in self.comentario.listar():
            busca_comprador = connector.procurar("Comprador", comt["codigo_comprador"], coluna="codigo")
            print(comt["codigo_produto"], self.comentario.codigo_produto, comt["codigo_loja"], self.comentario.codigo_loja)
            if comt["codigo_produto"] == self.comentario.codigo_produto and comt["codigo_loja"] == self.comentario.codigo_loja:
                self.scrl.insert("insert", f"{busca_comprador['nome']}: {comt['descricao']}\n")
                
        self.scrl['state'] = "disabled"

    def ux(self):
        if self.kwargs['tipo_perfil'] == "Comprador":
            estado = "normal"
        elif self.kwargs['tipo_perfil'] == "Vendedor":
            estado = "disabled"
        self.frm_principal = ttk.Frame(self.root); self.frm_principal.pack(fill="both", padx=20, pady=20)
        ttk.Label(self.frm_principal, text="Comentários", font=(None,14)).pack()
        self.scrl = ttk.ScrolledText(self.frm_principal); self.scrl.pack(fill="both")
        frm_add_comentario = ttk.Frame(self.frm_principal); frm_add_comentario.pack(fill="x", expand=True)
        ttk.Entry(frm_add_comentario, textvariable=self.var_comentario, state=estado).pack(fill="x", side="left", expand=True, pady=10)
        ttk.Button(frm_add_comentario, text="Enviar comentário", command=self.fun_enviar_comentario, state=estado).pack(padx=(10,0), side="left")
        ttk.Button(self.frm_principal, text="Voltar", bootstyle="secondary-outline", command=self.root.destroy).pack(pady=10)
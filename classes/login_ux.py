from util_ux import *
from classes.cadastro_pessoa_ux import Pagina_inicial, Cadastro_Pessoa

class Login:
    
    def __init__(self, root):
        
        self.root = root
        self.root.minsize(500,500)
        self.inicializa_variaveis()
        self.ux()

    def inicializa_variaveis(self):

        self.var_nome = ttk.StringVar()
        self.var_senha = ttk.StringVar()
        
    def fun_entrar(self):

        tipos = ["Comprador", "Vendedor"]

        for tipo in tipos:

            for pessoa in Connector(path_banco).listar_tabela(tipo):
                if self.var_nome.get() == pessoa["nome"] and self.var_senha.get() == pessoa["senha"]:

                    if tipo == "Comprador":

                        perfil = Comprador(codigo=pessoa["codigo"],
                                    nome=pessoa["nome"],
                                    senha=pessoa["senha"],
                                    data_de_nascimento=pessoa["data_de_nascimento"],
                                    email=pessoa["email"],
                                    is_ativo=pessoa["is_ativo"],
                                    logradouro=pessoa["logradouro"],
                                    numero=pessoa["numero"],
                                    complemento=pessoa["complemento"],
                                    cidade=pessoa["cidade"],
                                    uf=pessoa["uf"],
                                    cep=pessoa["cep"],
                                    cpf=pessoa["cpf"],
                                    rg=pessoa["rg"],
                                    cartao=pessoa["cartao"])
                        
                    elif tipo == "Vendedor":

                        perfil = Vendedor(codigo=pessoa["codigo"],
                                        nome=pessoa["nome"],
                                        senha=pessoa["senha"],
                                        data_de_nascimento=pessoa["data_de_nascimento"],
                                        email=pessoa["email"],
                                        is_ativo=pessoa["is_ativo"],
                                        codigo_loja=pessoa["codigo_loja"])
                    
                    destruir_elementos(self.root)
                    Pagina_inicial(self.root, tipo, perfil)
                    return
                
        messagebox.showerror('','Nome ou senha inválidos!')
        
        
        
    def ux(self):
        
        frm_principal = ttk.Frame(self.root); frm_principal.pack(fill="both", expand=True,padx=20,pady=20)
        
        ttk.Label(frm_principal, text="Login", font=(None,16)).pack()
        
        frm_usuario = ttk.Frame(frm_principal); frm_usuario.pack(pady=10, fill="x")
        ttk.Label(frm_usuario, text="Usuário").pack(anchor="w")
        ttk.Entry(frm_usuario, textvariable=self.var_nome).pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_usuario, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_senha = ttk.Frame(frm_principal); frm_senha.pack(pady=10, fill="x")
        ttk.Label(frm_senha, text="Senha").pack(anchor="w")
        ttk.Entry(frm_senha, textvariable=self.var_senha, show="*").pack(fill="x")
        self.lbl_verif_usuario = ttk.Label(frm_senha, text="", bootstyle="danger"); self.lbl_verif_usuario.pack(anchor="w")
        
        frm_botoes = ttk.Frame(frm_principal); frm_botoes.pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Entrar", bootstyle="success-outline", command=self.fun_entrar).pack(pady=10, fill="x")
        ttk.Button(frm_botoes, text="Sair", bootstyle="secondary-outline").pack(pady=10, fill="x")
        
        frm_cadastro = ttk.Frame(frm_principal); frm_cadastro.pack(pady=10, anchor="center")
        ttk.Label(frm_cadastro, text="Ainda não tem conta?").pack(side="left")
        #ttk.Button(frm_cadastro, text="Cadastrar", bootstyle="secondary-link").pack(side="left")
        mb=ttk.Menubutton(frm_cadastro,text='Cadastrar-se', bootstyle="secondary-outline");  mb.pack(side="left")
        mb.menu=ttk.Menu(mb)
        mb['menu']=mb.menu
        mb.menu.add_command(label='Sou comprador', command=lambda:Cadastro_Pessoa(ttk.Toplevel(), self.root, "Comprador"))
        mb.menu.add_command(label='Sou vendedor', command=lambda:Cadastro_Pessoa(ttk.Toplevel(), self.root, "Vendedor"))
        self.var_nome.set("Matteo")
        self.var_senha.set("123")
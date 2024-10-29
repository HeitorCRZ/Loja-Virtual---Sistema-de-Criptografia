import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from pymongo.server_api import ServerApi
# teste
#git add .
#git commit -m "Atualização automática"
#git push origin master
# Conexão com o MongoDB
def connect_to_mongo():
    try:
        uri = "mongodb+srv://DB_First:DB_Heitor060807@cluster0.xzfx3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['Loja_Virtual']
        global usuarios
        usuarios = db['usuarios']  # Coleção para armazenar usuários
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível conectar ao MongoDB: {str(e)}")

# Função para verificar login
def verificar_login(event=None):
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    usuario_existente = usuarios.find_one({"usuario": usuario, "senha": senha})
    
    if usuario_existente:
        messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {usuario}!")
        abrir_pagina_principal()
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos.")

# Função para criar novo cadastro
def criar_cadastro(event=None):
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuarios.find_one({"usuario": usuario}):
        messagebox.showerror("Erro", "Usuário já existe. Escolha um nome de usuário diferente.")
    else:
        usuarios.insert_one({"usuario": usuario, "senha": senha})
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

# Função para abrir a página principal
def abrir_pagina_principal():
    janela_login.destroy()
    
    janela_principal = tk.Tk()
    janela_principal.title("Página Principal")
    janela_principal.attributes('-fullscreen', True)  # Tela cheia automaticamente
    
    # Criar um Frame para o Painel de Controle
    painel_controle = tk.Frame(janela_principal, bg="lightgrey", padx=20, pady=20)
    painel_controle.grid(row=0, column=0, sticky="ns")

    # Criar um Frame para o Conteúdo Principal
    conteudo_principal = tk.Frame(janela_principal, bg="white", padx=20, pady=20)
    conteudo_principal.grid(row=0, column=1, sticky="nsew")

    # Configurar a grade para expansão do conteúdo principal
    janela_principal.grid_rowconfigure(0, weight=1)
    janela_principal.grid_columnconfigure(1, weight=1)

    # Título do Painel
    label_titulo_painel = tk.Label(painel_controle, text="MENU!!", font=("Helvetica", 18, "bold"), bg="lightgrey")
    label_titulo_painel.pack(pady=10)

    # Menu de Produtos
    botao_produtos = tk.Button(painel_controle, text="Produtos", command=abrir_menu_produtos, font=("Helvetica", 14), bg="blue", fg="white", width=15)
    botao_produtos.pack(pady=10)

    # Menu do Carrinho
    botao_carrinho = tk.Button(painel_controle, text="Carrinho", command=abrir_menu_carrinho, font=("Helvetica", 14), bg="green", fg="white", width=15)
    botao_carrinho.pack(pady=10)

    # Menu do Histórico de Transações
    botao_historico = tk.Button(painel_controle, text="Transações", command=abrir_historico_transacoes, font=("Helvetica", 14), bg="orange", fg="white", width=15)
    botao_historico.pack(pady=10)

    # Botão de Sair
    botao_sair = tk.Button(janela_principal, text="Sair", command=janela_principal.destroy, font=("Helvetica", 16), bg="red", fg="white", width=10)
    botao_sair.grid(row=1, column=0, columnspan=2, pady=20)

    # Exibir conteúdo inicial
    conteudo_inicial = tk.Label(conteudo_principal, text="Bem-vindo à Loja Virtual!", font=("Helvetica", 24))
    conteudo_inicial.pack(pady=100)

    # Adiciona o botão de voltar
    botao_voltar = tk.Button(janela_principal, text="Voltar", command=criar_janela_login, font=("Helvetica", 16), bg="yellow", fg="black", width=10)
    botao_voltar.grid(row=1, column=2, pady=20)

    janela_principal.mainloop()

def abrir_menu_produtos():
    janela_produtos = tk.Tk()
    janela_produtos.title("Produtos")
    janela_produtos.attributes('-fullscreen', True)  # Tela cheia automaticamente

    label_produtos = tk.Label(janela_produtos, text="Aqui será a lista de produtos.", font=("Helvetica", 20))
    label_produtos.pack(pady=50)

    botao_voltar = tk.Button(janela_produtos, text="Voltar", command=lambda: voltar_para_menu(janela_produtos), font=("Helvetica", 14), bg="yellow", fg="black")
    botao_voltar.pack(pady=20)

    janela_produtos.mainloop()

def abrir_menu_carrinho():
    janela_carrinho = tk.Tk()
    janela_carrinho.title("Carrinho")
    janela_carrinho.attributes('-fullscreen', True)  # Tela cheia automaticamente

    label_carrinho = tk.Label(janela_carrinho, text="Aqui será o seu carrinho de compras.", font=("Helvetica", 20))
    label_carrinho.pack(pady=50)

    botao_voltar = tk.Button(janela_carrinho, text="Voltar", command=lambda: voltar_para_menu(janela_carrinho), font=("Helvetica", 14), bg="yellow", fg="black")
    botao_voltar.pack(pady=20)

    janela_carrinho.mainloop()

def abrir_historico_transacoes():
    janela_historico = tk.Tk()
    janela_historico.title("Histórico de Transações")
    janela_historico.attributes('-fullscreen', True)  # Tela cheia automaticamente

    label_historico = tk.Label(janela_historico, text="Aqui será o seu histórico de transações.", font=("Helvetica", 20))
    label_historico.pack(pady=50)

    botao_voltar = tk.Button(janela_historico, text="Voltar", command=lambda: voltar_para_menu(janela_historico), font=("Helvetica", 14), bg="yellow", fg="black")
    botao_voltar.pack(pady=20)

    janela_historico.mainloop()

# Função para voltar ao menu principal
def voltar_para_menu(janela_atual):
    janela_atual.destroy()
    abrir_pagina_principal()

# Função para criar a interface de Login/Cadastro
def criar_janela_login():
    global janela_login, entry_usuario, entry_senha
    
    janela_login = tk.Tk()
    janela_login.title("Sistema de Login")
    janela_login.attributes('-fullscreen', True)  # Tela cheia automaticamente

    # Conectar ao MongoDB
    connect_to_mongo()

    # Componentes de login e cadastro com layout responsivo e tamanho aumentado
    label_titulo = tk.Label(janela_login, text="Login ou Cadastro", font=("Helvetica", 24, "bold"))
    label_titulo.place(relx=0.5, rely=0.2, anchor="center")

    label_usuario = tk.Label(janela_login, text="Usuário:", font=("Helvetica", 18))
    label_usuario.place(relx=0.35, rely=0.4, anchor="e")
    entry_usuario = tk.Entry(janela_login, font=("Helvetica", 16), width=25)
    entry_usuario.place(relx=0.5, rely=0.4, anchor="center")
    entry_usuario.focus()  # Define o foco inicial no campo de usuário

    label_senha = tk.Label(janela_login, text="Senha:", font=("Helvetica", 18))
    label_senha.place(relx=0.35, rely=0.5, anchor="e")
    entry_senha = tk.Entry(janela_login, show="*", font=("Helvetica", 16), width=25)  # `show="*"` oculta a senha
    entry_senha.place(relx=0.5, rely=0.5, anchor="center")

    # Botões de Login e Cadastro
    botao_login = tk.Button(janela_login, text="Entrar", command=verificar_login, font=("Helvetica", 14), bg="blue", fg="white", width=12)
    botao_login.place(relx=0.4, rely=0.6, anchor="center")

    botao_cadastro = tk.Button(janela_login, text="Cadastrar", command=criar_cadastro, font=("Helvetica", 14), bg="green", fg="white", width=12)
    botao_cadastro.place(relx=0.6, rely=0.6, anchor="center")

    # Botão de Sair no canto inferior direito da tela
    botao_sair = tk.Button(janela_login, text="Sair", command=janela_login.destroy, font=("Helvetica", 14), bg="red", fg="white", width=10)
    botao_sair.place(relx=0.98, rely=0.98, anchor="se")  # Posicionado com margem das bordas

    # Permitir foco nas entradas clicando nelas
    entry_usuario.bind("<Button-1>", lambda event: entry_usuario.focus())
    entry_senha.bind("<Button-1>", lambda event: entry_senha.focus())

    # Adicionando bind para a tecla de retorno
    entry_usuario.bind("<Return>", lambda event: entry_senha.focus())  # Move para a senha
    entry_senha.bind("<Return>", verificar_login)  # Aciona login ao pressionar Enter na senha

    # Desativando os botões até que haja texto nas entradas
    def update_buttons_state(*args):
        if entry_usuario.get() and entry_senha.get():
            botao_login.config(state=tk.NORMAL)
            botao_cadastro.config(state=tk.NORMAL)
        else:
            botao_login.config(state=tk.DISABLED)
            botao_cadastro.config(state=tk.DISABLED)

    # Atualiza o estado dos botões quando o texto é alterado
    entry_usuario.bind("<KeyRelease>", update_buttons_state)
    entry_senha.bind("<KeyRelease>", update_buttons_state)

    # Iniciar desabilitando os botões
    botao_login.config(state=tk.DISABLED)
    botao_cadastro.config(state=tk.DISABLED)

    janela_login.mainloop()

# Chamar a função para criar a janela de login ao iniciar o programa
criar_janela_login()

"""
Gerenciador LL
==============
Autor: Luis Leal
GitHub: github.com/luiisocl/GERENCIADOR-LL
Versão: 1.0.0
Descrição: Gerenciador de arquivos inteligente com IA integrada
Licença: Todos os direitos reservados © 2026 Luis Leal
"""
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.cofre import cofre_existe, criar_cofre, verificar_senha, adicionar_arquivo, listar_arquivos_cofre, remover_arquivo

def criar_cofre_tela(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()
    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Cofre de Arquivos", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)
    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True)
    if not cofre_existe():
        mostrar_criar_cofre(frame_conteudo, frame_principal)
    else:
        mostrar_login_cofre(frame_conteudo, frame_principal)

def mostrar_criar_cofre(frame_conteudo, frame_principal):
    frame_centro = ctk.CTkFrame(frame_conteudo, corner_radius=16)
    frame_centro.place(relx=0.5, rely=0.5, anchor="center")
    ctk.CTkLabel(frame_centro, text="🔐", font=ctk.CTkFont(size=40)).pack(pady=(30,5), padx=60)
    ctk.CTkLabel(frame_centro, text="Criar Cofre", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0,5), padx=60)
    ctk.CTkLabel(frame_centro, text="Defina uma senha para proteger seus arquivos", font=ctk.CTkFont(size=12), text_color="gray").pack(pady=(0,20), padx=60)
    entrada_senha = ctk.CTkEntry(frame_centro, placeholder_text="Digite uma senha", show="*", width=280, height=38)
    entrada_senha.pack(pady=5, padx=40)
    entrada_confirmar = ctk.CTkEntry(frame_centro, placeholder_text="Confirme a senha", show="*", width=280, height=38)
    entrada_confirmar.pack(pady=5, padx=40)
    label_erro = ctk.CTkLabel(frame_centro, text="", text_color="red", font=ctk.CTkFont(size=11))
    label_erro.pack(pady=5)
    def criar():
        senha = entrada_senha.get()
        confirmar = entrada_confirmar.get()
        if not senha:
            label_erro.configure(text="Digite uma senha!")
            return
        if senha != confirmar:
            label_erro.configure(text="As senhas não coincidem!")
            return
        criar_cofre(senha)
        messagebox.showinfo("Sucesso", "✅ Cofre criado com sucesso!")
        criar_cofre_tela(frame_principal)
    ctk.CTkButton(frame_centro, text="Criar Cofre", height=38, width=280, command=criar).pack(pady=(10,30), padx=40)

def mostrar_login_cofre(frame_conteudo, frame_principal):
    frame_login = ctk.CTkFrame(frame_conteudo, corner_radius=16)
    frame_login.place(relx=0.5, rely=0.5, anchor="center")
    ctk.CTkLabel(frame_login, text="🔒", font=ctk.CTkFont(size=40)).pack(pady=(30,5), padx=60)
    ctk.CTkLabel(frame_login, text="Cofre de Arquivos", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(0,5), padx=60)
    ctk.CTkLabel(frame_login, text="Digite sua senha para acessar", font=ctk.CTkFont(size=12), text_color="gray").pack(pady=(0,20), padx=60)
    entrada_senha = ctk.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*", width=280, height=38)
    entrada_senha.pack(pady=5, padx=40)
    label_erro = ctk.CTkLabel(frame_login, text="", text_color="red", font=ctk.CTkFont(size=11))
    label_erro.pack(pady=5)
    def acessar():
        senha = entrada_senha.get()
        if verificar_senha(senha):
            for widget in frame_conteudo.winfo_children():
                widget.destroy()
            mostrar_cofre_aberto(frame_conteudo, frame_principal, senha)
        else:
            label_erro.configure(text="❌ Senha incorreta!")
    entrada_senha.bind("<Return>", lambda e: acessar())
    ctk.CTkButton(frame_login, text="Acessar Cofre", height=38, width=280, command=acessar).pack(pady=(10,30), padx=40)

def mostrar_cofre_aberto(frame_conteudo, frame_principal, senha):
    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", padx=24, pady=(20,16))
    ctk.CTkLabel(frame_topo, text="🔓  Cofre Aberto", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
    ctk.CTkButton(frame_topo, text="➕  Adicionar Arquivo", height=36, command=lambda: adicionar()).pack(side="left", padx=(12,0))
    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True, padx=24, pady=(0,20))
    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Caminho Original", "Ação"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=280, anchor="w").pack(side="left", padx=16, pady=10)
    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)
    def atualizar_lista():
        for widget in scroll.winfo_children():
            widget.destroy()
        arquivos = listar_arquivos_cofre(senha)
        if not arquivos:
            ctk.CTkLabel(scroll, text="Nenhum arquivo no cofre ainda.", text_color="gray", font=ctk.CTkFont(size=12)).pack(pady=20)
            return
        for arquivo in arquivos:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            ctk.CTkLabel(frame_linha, text=arquivo["nome"], font=ctk.CTkFont(size=12), width=280, anchor="w").pack(side="left", padx=16, pady=10)
            ctk.CTkLabel(frame_linha, text=arquivo["original"], font=ctk.CTkFont(size=12), width=280, anchor="w").pack(side="left", padx=16, pady=10)
            ctk.CTkButton(frame_linha, text="↩️  Restaurar", width=120, height=32, command=lambda n=arquivo["nome"]: restaurar(n)).pack(side="left", padx=16)
    def adicionar():
        caminho = filedialog.askopenfilename()
        if caminho:
            adicionar_arquivo(caminho, senha)
            from utils.historico import registrar_acao
            registrar_acao("Cofre", f"Arquivo adicionado: {os.path.basename(caminho)}")
            atualizar_lista()
    def restaurar(nome):
        resposta = messagebox.askyesno("Confirmar", f"Deseja restaurar '{nome}' para o local original?")
        if resposta:
            remover_arquivo(nome, senha)
            from utils.historico import registrar_acao
            registrar_acao("Cofre", f"Arquivo restaurado: {nome}")
            atualizar_lista()
    atualizar_lista()
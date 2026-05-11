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
from core.organizador import listar_arquivos, organizar_pasta

def criar_organizar(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Organizar Arquivos", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=24, pady=20)

    pasta_var = ctk.StringVar(value="Nenhuma pasta selecionada")

    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", pady=(0,16))

    ctk.CTkButton(frame_topo, text="📁  Selecionar Pasta", height=36, command=lambda: selecionar_pasta()).pack(side="left")
    btn_organizar = ctk.CTkButton(frame_topo, text="✨  Organizar", height=36, state="disabled", fg_color=("#3B82F6", "#1f538d"))
    btn_organizar.pack(side="left", padx=(10,0))
    ctk.CTkLabel(frame_topo, textvariable=pasta_var, font=ctk.CTkFont(size=12), text_color="gray").pack(side="left", padx=16)

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Tipo", "Tamanho"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=280, anchor="w").pack(side="left", padx=16, pady=10)

    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)

    def atualizar_lista(pasta):
        for widget in scroll.winfo_children():
            widget.destroy()
        arquivos = listar_arquivos(pasta)
        for nome, tipo, tamanho in arquivos:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            for info in [nome, tipo, f"{tamanho} MB"]:
                ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=280, anchor="w").pack(side="left", padx=16, pady=8)
        return arquivos

    def confirmar_organizacao():
        from utils.historico import registrar_acao
        pasta = pasta_var.get()
        resposta = messagebox.askyesno("Confirmar", f"Deseja organizar os arquivos em:\n{pasta}\n\nOs arquivos serão movidos para subpastas por tipo!")
        if resposta:
            organizados, erros = organizar_pasta(pasta)
            registrar_acao("Organização", f"{organizados} arquivos organizados em {pasta}")
            messagebox.showinfo("Concluído", f"✅ {organizados} arquivos organizados!\n❌ {erros} erros.")
            atualizar_lista(pasta)

    def selecionar_pasta():
        pasta = filedialog.askdirectory()
        if pasta:
            pasta_var.set(pasta)
            arquivos = atualizar_lista(pasta)
            if arquivos:
                btn_organizar.configure(state="normal", command=confirmar_organizacao)
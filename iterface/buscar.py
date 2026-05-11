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
from tkinter import filedialog
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.buscador import buscar_arquivos

def criar_buscar(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Buscar Arquivos", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=24, pady=20)

    pasta_var = ctk.StringVar(value="Nenhuma pasta selecionada")

    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", pady=(0,12))
    ctk.CTkButton(frame_topo, text="📁  Selecionar Pasta", height=36, command=lambda: selecionar_pasta()).pack(side="left")
    ctk.CTkLabel(frame_topo, textvariable=pasta_var, font=ctk.CTkFont(size=12), text_color="gray").pack(side="left", padx=16)

    frame_busca = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_busca.pack(fill="x", pady=(0,16))
    entrada_busca = ctk.CTkEntry(frame_busca, placeholder_text="Digite o nome ou extensão do arquivo...", height=38, width=400)
    entrada_busca.pack(side="left", padx=(0,10))
    ctk.CTkButton(frame_busca, text="🔍  Buscar", height=38, command=lambda: realizar_busca()).pack(side="left")

    label_resultado = ctk.CTkLabel(frame_conteudo, text="", font=ctk.CTkFont(size=12), text_color="gray")
    label_resultado.pack(anchor="w", pady=(0,10))

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Caminho", "Tamanho"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=280, anchor="w").pack(side="left", padx=16, pady=10)

    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)

    def selecionar_pasta():
        pasta = filedialog.askdirectory()
        if pasta:
            pasta_var.set(pasta)

    def realizar_busca():
        pasta = pasta_var.get()
        termo = entrada_busca.get()
        if pasta == "Nenhuma pasta selecionada":
            label_resultado.configure(text="⚠️ Selecione uma pasta primeiro!")
            return
        if not termo:
            label_resultado.configure(text="⚠️ Digite um termo para buscar!")
            return
        for widget in scroll.winfo_children():
            widget.destroy()
        label_resultado.configure(text="🔍 Buscando...")
        frame_principal.update()
        resultados = buscar_arquivos(pasta, termo)
        label_resultado.configure(text=f"✅ {len(resultados)} arquivo(s) encontrado(s)")
        for nome, caminho, tamanho in resultados:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            for info in [nome, caminho, f"{tamanho} MB"]:
                ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=280, anchor="w").pack(side="left", padx=16, pady=8)
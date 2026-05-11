

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
from tkinter import messagebox
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.historico import carregar_historico, limpar_historico

def criar_historico(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Histórico de Ações", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)
    ctk.CTkButton(topbar, text="🗑️  Limpar Histórico", height=32, fg_color=("#DC2626", "#7f1d1d"), hover_color=("#B91C1C", "#6b0000"), command=lambda: confirmar_limpeza()).pack(side="right", padx=24)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=24, pady=20)

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col, w in [("Data", 160), ("Ação", 180), ("Detalhes", 500)]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=w, anchor="w").pack(side="left", padx=16, pady=10)

    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)

    def atualizar_lista():
        for widget in scroll.winfo_children():
            widget.destroy()
        historico = carregar_historico()
        if not historico:
            ctk.CTkLabel(scroll, text="Nenhuma ação registrada ainda.", text_color="gray", font=ctk.CTkFont(size=12)).pack(pady=20)
            return
        for item in historico:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            for info, w in [(item["data"], 160), (item["acao"], 180), (item["detalhes"], 500)]:
                ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=w, anchor="w").pack(side="left", padx=16, pady=8)

    def confirmar_limpeza():
        resposta = messagebox.askyesno("Confirmar", "Deseja limpar todo o histórico de ações?")
        if resposta:
            limpar_historico()
            atualizar_lista()

    atualizar_lista()
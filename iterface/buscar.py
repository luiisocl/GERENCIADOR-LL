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
from core.buscador import buscar_arquivos

def criar_buscar(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()
    topbar = ctk.CTkFrame(frame_principal, height=50, corner_radius=0, fg_color="#2b2b2b")
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Buscar Arquivos", font=ctk.CTkFont(size=15, weight="bold")).pack(side="left", padx=20, pady=15)
    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="#1a1a1a")
    frame_conteudo.pack(fill="both", expand=True, padx=20, pady=20)
    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", pady=(0,20))
    pasta_var = ctk.StringVar(value="Nenhuma pasta selecionada")
    ctk.CTkLabel(frame_topo, textvariable=pasta_var, font=ctk.CTkFont(size=12), text_color="gray").pack(side="left", padx=(0,10))
    ctk.CTkButton(frame_topo, text="📁 Selecionar Pasta", command=lambda: selecionar_pasta()).pack(side="left")
    frame_busca = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_busca.pack(fill="x", pady=(0,20))
    entrada_busca = ctk.CTkEntry(frame_busca, placeholder_text="Digite o nome do arquivo...", width=400)
    entrada_busca.pack(side="left", padx=(0,10))
    ctk.CTkButton(frame_busca, text="🔍 Buscar", command=lambda: realizar_busca()).pack(side="left")
    label_resultado = ctk.CTkLabel(frame_conteudo, text="", font=ctk.CTkFont(size=12), text_color="gray")
    label_resultado.pack(anchor="w", pady=(0,8))
    frame_lista = ctk.CTkFrame(frame_conteudo, fg_color="#2b2b2b", corner_radius=8)
    frame_lista.pack(fill="both", expand=True)
    cabecalho = ctk.CTkFrame(frame_lista, fg_color="#333333", corner_radius=0)
    cabecalho.pack(fill="x")
    for col in ["Nome", "Caminho", "Tamanho"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11), text_color="gray", width=250, anchor="w").pack(side="left", padx=14, pady=8)
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
            for info in [nome, caminho, f"{tamanho} MB"]:
                ctk.CTkLabel(linha, text=info, font=ctk.CTkFont(size=12), width=250, anchor="w").pack(side="left", padx=14, pady=6)
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
import os
import sys
import shutil
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def criar_dashboard(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Dashboard", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=24, pady=20)

    disco = shutil.disk_usage("C:/")
    espaco_livre_gb = round(disco.free / 1024 / 1024 / 1024, 1)
    espaco_total_gb = round(disco.total / 1024 / 1024 / 1024, 1)
    percentual_livre = round((disco.free / disco.total) * 100)

    frame_cards = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_cards.pack(fill="x", pady=(0,24))

    cards = [
        ("Total de arquivos", "—", "Em breve", "#3B82F6"),
        ("Duplicatas", "—", "Analise sua pasta", "#F59E0B"),
        ("Esquecidos", "—", "Analise sua pasta", "#8B5CF6"),
        ("Espaço livre", f"{espaco_livre_gb} GB", f"{percentual_livre}% de {espaco_total_gb} GB", "#10B981"),
    ]

    for titulo, valor, subtitulo, cor in cards:
        card = ctk.CTkFrame(frame_cards, corner_radius=10)
        card.pack(side="left", expand=True, fill="x", padx=6)
        barra = ctk.CTkFrame(card, width=4, corner_radius=2, fg_color=cor)
        barra.pack(side="left", fill="y", padx=(12,0), pady=12)
        frame_texto = ctk.CTkFrame(card, fg_color="transparent")
        frame_texto.pack(side="left", fill="both", expand=True, padx=12, pady=12)
        ctk.CTkLabel(frame_texto, text=titulo, font=ctk.CTkFont(size=11), text_color="gray").pack(anchor="w")
        ctk.CTkLabel(frame_texto, text=valor, font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(frame_texto, text=subtitulo, font=ctk.CTkFont(size=11), text_color="gray").pack(anchor="w")

    ctk.CTkLabel(frame_conteudo, text="Arquivos recentes", font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", pady=(0,10))

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Tipo", "Tamanho", "Modificado"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=200, anchor="w").pack(side="left", padx=16, pady=10)

    arquivos_recentes = [
        ("foto_viagem.jpg", "Imagem", "3,2 MB", "Hoje"),
        ("contrato_trabalho.pdf", "Documento", "1,1 MB", "Ontem"),
        ("apresentacao.mp4", "Vídeo", "245 MB", "3 dias atrás"),
        ("playlist_favorita.mp3", "Música", "8,4 MB", "1 semana atrás"),
    ]

    for nome, tipo, tamanho, data in arquivos_recentes:
        linha = ctk.CTkFrame(frame_lista, fg_color="transparent", corner_radius=0)
        linha.pack(fill="x")
        sep = ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20"))
        sep.pack(fill="x")
        frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
        frame_linha.pack(fill="x")
        for info in [nome, tipo, tamanho, data]:
            ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=200, anchor="w").pack(side="left", padx=16, pady=10)
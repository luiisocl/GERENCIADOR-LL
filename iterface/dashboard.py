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

def criar_dashboard(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()
    topbar = ctk.CTkFrame(frame_principal, height=50, corner_radius=0, fg_color="#2b2b2b")
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Dashboard", font=ctk.CTkFont(size=15, weight="bold")).pack(side="left", padx=20, pady=15)
    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="#1a1a1a")
    frame_conteudo.pack(fill="both", expand=True, padx=20, pady=20)
    frame_cards = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_cards.pack(fill="x", pady=(0,20))
    cards = [
        ("Total de arquivos", "4.821", "+134 este mês"),
        ("Duplicatas", "12", "2,3 GB ocupados"),
        ("Esquecidos", "87", "Sem uso há +1 ano"),
        ("Espaço livre", "76 GB", "38% do total"),
    ]
    for titulo, valor, subtitulo in cards:
        card = ctk.CTkFrame(frame_cards, fg_color="#2b2b2b", corner_radius=8)
        card.pack(side="left", expand=True, fill="x", padx=6)
        ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=11), text_color="gray").pack(anchor="w", padx=14, pady=(12,0))
        ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=14)
        ctk.CTkLabel(card, text=subtitulo, font=ctk.CTkFont(size=11), text_color="gray").pack(anchor="w", padx=14, pady=(0,12))
    ctk.CTkLabel(frame_conteudo, text="Arquivos recentes", font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", pady=(0,8))
    frame_lista = ctk.CTkFrame(frame_conteudo, fg_color="#2b2b2b", corner_radius=8)
    frame_lista.pack(fill="x")
    cabecalho = ctk.CTkFrame(frame_lista, fg_color="#333333", corner_radius=0)
    cabecalho.pack(fill="x")
    for col in ["Nome", "Tipo", "Tamanho", "Modificado"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11), text_color="gray", width=200, anchor="w").pack(side="left", padx=14, pady=8)
    arquivos_recentes = [
        ("foto_viagem.jpg", "Imagem", "3,2 MB", "Hoje"),
        ("contrato_trabalho.pdf", "Documento", "1,1 MB", "Ontem"),
        ("apresentacao.mp4", "Vídeo", "245 MB", "3 dias atrás"),
        ("playlist_favorita.mp3", "Música", "8,4 MB", "1 semana atrás"),
    ]
    for nome, tipo, tamanho, data in arquivos_recentes:
        linha = ctk.CTkFrame(frame_lista, fg_color="transparent", corner_radius=0)
        linha.pack(fill="x")
        for info in [nome, tipo, tamanho, data]:
            ctk.CTkLabel(linha, text=info, font=ctk.CTkFont(size=12), width=200, anchor="w").pack(side="left", padx=14, pady=8)
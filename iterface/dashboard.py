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
import threading
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

    cards_info = [
        ("Total de arquivos", "⏳", "Carregando...", "#3B82F6"),
        ("Duplicatas", "⏳", "Carregando...", "#F59E0B"),
        ("Esquecidos", "⏳", "Carregando...", "#8B5CF6"),
        ("Espaço livre", f"{espaco_livre_gb} GB", f"{percentual_livre}% de {espaco_total_gb} GB", "#10B981"),
    ]

    labels_valores = []
    labels_subtitulos = []

    for titulo, valor, subtitulo, cor in cards_info:
        card = ctk.CTkFrame(frame_cards, corner_radius=10)
        card.pack(side="left", expand=True, fill="x", padx=6)
        barra = ctk.CTkFrame(card, width=4, corner_radius=2, fg_color=cor)
        barra.pack(side="left", fill="y", padx=(12,0), pady=12)
        frame_texto = ctk.CTkFrame(card, fg_color="transparent")
        frame_texto.pack(side="left", fill="both", expand=True, padx=12, pady=12)
        ctk.CTkLabel(frame_texto, text=titulo, font=ctk.CTkFont(size=11), text_color="gray").pack(anchor="w")
        lv = ctk.CTkLabel(frame_texto, text=valor, font=ctk.CTkFont(size=22, weight="bold"))
        lv.pack(anchor="w")
        ls = ctk.CTkLabel(frame_texto, text=subtitulo, font=ctk.CTkFont(size=11), text_color="gray")
        ls.pack(anchor="w")
        labels_valores.append(lv)
        labels_subtitulos.append(ls)

    ctk.CTkLabel(frame_conteudo, text="Arquivos recentes", font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", pady=(0,10))

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Tipo", "Tamanho", "Modificado"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=200, anchor="w").pack(side="left", padx=16, pady=10)

    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)

    def carregar_arquivos_recentes():
        pasta_usuario = os.path.expanduser("~")
        pastas = [
            os.path.join(pasta_usuario, "Downloads"),
            os.path.join(pasta_usuario, "Documents"),
            os.path.join(pasta_usuario, "Desktop"),
        ]
        arquivos = []
        for pasta in pastas:
            if not os.path.exists(pasta):
                continue
            try:
                for nome in os.listdir(pasta):
                    caminho = os.path.join(pasta, nome)
                    if os.path.isfile(caminho):
                        mod = os.path.getmtime(caminho)
                        tamanho = round(os.path.getsize(caminho) / 1024 / 1024, 2)
                        arquivos.append((nome, caminho, tamanho, mod))
            except:
                continue
        arquivos.sort(key=lambda x: x[3], reverse=True)
        return arquivos[:10]

    def identificar_tipo(nome):
        ext = os.path.splitext(nome)[1].lower()
        tipos = {
            "Imagem": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
            "Documento": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
            "Vídeo": [".mp4", ".avi", ".mov", ".mkv"],
            "Música": [".mp3", ".wav", ".flac", ".aac"],
            "Programa": [".exe", ".msi"],
            "Compactado": [".zip", ".rar", ".7z"],
        }
        for tipo, exts in tipos.items():
            if ext in exts:
                return tipo
        return "Outro"

    def formatar_data(timestamp):
        import datetime
        agora = datetime.datetime.now()
        data = datetime.datetime.fromtimestamp(timestamp)
        diff = (agora - data).days
        if diff == 0:
            return "Hoje"
        elif diff == 1:
            return "Ontem"
        elif diff < 7:
            return f"{diff} dias atrás"
        else:
            return data.strftime("%d/%m/%Y")

    def contar_total_arquivos():
        pasta = os.path.expanduser("~")
        pastas_ignoradas = ["AppData", "__pycache__", ".git"]
        total = 0
        try:
            for raiz, dirs, arquivos in os.walk(pasta):
                dirs[:] = [d for d in dirs if d not in pastas_ignoradas]
                total += len(arquivos)
        except:
            pass
        return total

    def buscar_dados_background():
        from utils.historico import carregar_stats
        stats = carregar_stats()
        if "duplicatas" in stats:
            frame_principal.after(0, lambda: labels_valores[1].configure(text=stats["duplicatas"]["valor"]))
            frame_principal.after(0, lambda: labels_subtitulos[1].configure(text=stats["duplicatas"]["subtitulo"]))
        else:
            frame_principal.after(0, lambda: labels_valores[1].configure(text="—"))
            frame_principal.after(0, lambda: labels_subtitulos[1].configure(text="Analise em Duplicatas"))
        if "esquecidos" in stats:
            frame_principal.after(0, lambda: labels_valores[2].configure(text=stats["esquecidos"]["valor"]))
            frame_principal.after(0, lambda: labels_subtitulos[2].configure(text=stats["esquecidos"]["subtitulo"]))
        else:
            frame_principal.after(0, lambda: labels_valores[2].configure(text="—"))
            frame_principal.after(0, lambda: labels_subtitulos[2].configure(text="Analise em Esquecidos"))

    def mostrar_arquivos_recentes(arquivos):
        for widget in scroll.winfo_children():
            widget.destroy()
        for nome, caminho, tamanho, mod in arquivos:
            tipo = identificar_tipo(nome)
            data = formatar_data(mod)
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            for info in [nome, tipo, f"{tamanho} MB", data]:
                ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=200, anchor="w").pack(side="left", padx=16, pady=10)

    threading.Thread(target=buscar_dados_background, daemon=True).start()
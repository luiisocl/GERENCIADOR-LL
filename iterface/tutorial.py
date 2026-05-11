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
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ARQUIVO_TUTORIAL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".tutorial_visto")

def tutorial_ja_visto():
    return os.path.exists(ARQUIVO_TUTORIAL)

def marcar_tutorial_visto():
    with open(ARQUIVO_TUTORIAL, "w") as f:
        f.write("visto")

def mostrar_tutorial(app, callback):
    if tutorial_ja_visto():
        callback()
        return

    janela = ctk.CTkToplevel(app)
    janela.title("Bem-vindo ao Gerenciador LL")
    janela.geometry("600x500")
    janela.resizable(False, False)
    janela.grab_set()

    passos = [
        ("👋 Bem-vindo ao Gerenciador LL!", "O Gerenciador LL é um programa completo para organizar, limpar e proteger seus arquivos de forma simples e inteligente.\n\nVamos fazer um tour rápido pelas funcionalidades!"),
        ("📊 Dashboard", "O Dashboard é sua tela principal.\n\nAqui você vê um resumo completo: espaço livre no disco, arquivos duplicados, arquivos esquecidos e muito mais."),
        ("📁 Organizar Arquivos", "A tela de Organização permite selecionar qualquer pasta e organizar automaticamente os arquivos em subpastas por tipo:\n\nImagens, Documentos, Vídeos, Músicas, Programas e Outros."),
        ("🔍 Buscador Inteligente", "O Buscador encontra qualquer arquivo no seu computador.\n\nDigite o nome ou a extensão (ex: .pdf, .jpg) e ele varre toda a pasta selecionada incluindo subpastas."),
        ("👥 Duplicatas & 💤 Esquecidos", "O Detector de Duplicatas encontra arquivos idênticos que ocupam espaço desnecessário.\n\nJá os Arquivos Esquecidos mostra arquivos que você não abre há muito tempo."),
        ("🧹 Limpeza & 🔐 Cofre", "A Limpeza Rápida remove arquivos temporários do sistema liberando espaço.\n\nO Cofre protege seus arquivos importantes com senha e criptografia real."),
        ("🤖 Assistente IA Premium", "O Assistente IA é uma funcionalidade exclusiva do plano Premium.\n\nEle permite gerenciar seus arquivos usando linguagem natural — é só digitar o que precisa!"),
        ("✅ Tudo pronto!", "Você já conhece todas as funcionalidades do Gerenciador LL!\n\nSempre que precisar rever o tutorial, acesse o menu e clique em 'Ver Tutorial'.\n\nBoa organização! 😊"),
    ]

    passo_atual = [0]

    frame_main = ctk.CTkFrame(janela, corner_radius=0, fg_color="transparent")
    frame_main.pack(fill="both", expand=True, padx=30, pady=30)

    label_emoji = ctk.CTkLabel(frame_main, text="", font=ctk.CTkFont(size=48))
    label_emoji.pack(pady=(0,10))

    label_titulo = ctk.CTkLabel(frame_main, text="", font=ctk.CTkFont(size=20, weight="bold"))
    label_titulo.pack(pady=(0,16))

    label_texto = ctk.CTkLabel(frame_main, text="", font=ctk.CTkFont(size=13), wraplength=500, justify="center", text_color="gray")
    label_texto.pack(pady=(0,30), padx=20)

    frame_botoes = ctk.CTkFrame(frame_main, fg_color="transparent")
    frame_botoes.pack(fill="x", side="bottom")

    label_progresso = ctk.CTkLabel(frame_botoes, text="", font=ctk.CTkFont(size=11), text_color="gray")
    label_progresso.pack(pady=(0,10))

    progress = ctk.CTkProgressBar(frame_botoes, height=6)
    progress.pack(fill="x", pady=(0,16))

    frame_btns = ctk.CTkFrame(frame_botoes, fg_color="transparent")
    frame_btns.pack(fill="x")

    btn_pular = ctk.CTkButton(frame_btns, text="Pular Tutorial", fg_color="transparent", hover_color=("gray85", "gray25"), text_color="gray", command=lambda: fechar(True))
    btn_pular.pack(side="left")

    btn_anterior = ctk.CTkButton(frame_btns, text="← Anterior", fg_color="transparent", hover_color=("gray85", "gray25"), state="disabled", command=lambda: mudar_passo(-1))
    btn_anterior.pack(side="left", padx=(10,0))

    btn_proximo = ctk.CTkButton(frame_btns, text="Próximo →", command=lambda: mudar_passo(1))
    btn_proximo.pack(side="right")

    def atualizar_passo():
        idx = passo_atual[0]
        titulo_completo = passos[idx][0]
        partes = titulo_completo.split(" ", 1)
        if len(partes) > 1 and len(partes[0]) <= 2:
            label_emoji.configure(text=partes[0])
            label_titulo.configure(text=partes[1])
        else:
            label_emoji.configure(text="")
            label_titulo.configure(text=titulo_completo)
        label_texto.configure(text=passos[idx][1])
        label_progresso.configure(text=f"Passo {idx + 1} de {len(passos)}")
        progress.set((idx + 1) / len(passos))
        btn_anterior.configure(state="normal" if idx > 0 else "disabled")
        btn_proximo.configure(text="Concluir ✅" if idx == len(passos) - 1 else "Próximo →")

    def mudar_passo(direcao):
        idx = passo_atual[0] + direcao
        if idx >= len(passos):
            fechar(True)
            return
        passo_atual[0] = idx
        atualizar_passo()

    def fechar(marcar=False):
        if marcar:
            marcar_tutorial_visto()
        janela.destroy()
        callback()

    janela.protocol("WM_DELETE_WINDOW", lambda: fechar(True))
    atualizar_passo()
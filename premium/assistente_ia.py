
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
import threading
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CHAVE_API = ""

def criar_assistente_ia(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Assistente IA", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)
    ctk.CTkLabel(topbar, text="✨ Premium", font=ctk.CTkFont(size=11, weight="bold"), text_color="#FFD700").pack(side="left", pady=15)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True)

    if not CHAVE_API:
        mostrar_tela_premium(frame_conteudo)
    else:
        mostrar_chat(frame_conteudo, frame_principal)

def mostrar_tela_premium(frame_conteudo):
    frame_centro = ctk.CTkFrame(frame_conteudo, corner_radius=16)
    frame_centro.place(relx=0.5, rely=0.5, anchor="center")
    ctk.CTkLabel(frame_centro, text="🤖", font=ctk.CTkFont(size=48)).pack(pady=(30,5), padx=80)
    ctk.CTkLabel(frame_centro, text="Assistente IA", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(0,4), padx=80)
    ctk.CTkLabel(frame_centro, text="Funcionalidade exclusiva do plano Premium", font=ctk.CTkFont(size=12), text_color="gray").pack(pady=(0,24), padx=80)

    beneficios = [
        "✅  Busca arquivos em linguagem natural",
        "✅  Sugestões inteligentes de organização",
        "✅  Responde perguntas sobre seus arquivos",
        "✅  Assistente disponível 24 horas por dia",
    ]
    for b in beneficios:
        ctk.CTkLabel(frame_centro, text=b, font=ctk.CTkFont(size=12), anchor="w").pack(anchor="w", padx=40, pady=3)

    ctk.CTkFrame(frame_centro, height=1, fg_color="gray30").pack(fill="x", padx=40, pady=(20,10))
    ctk.CTkLabel(frame_centro, text="R$ 19,90/mês  •  R$ 97,00 vitalício", font=ctk.CTkFont(size=13, weight="bold"), text_color="#FFD700").pack(pady=(0,10), padx=80)
    ctk.CTkButton(frame_centro, text="🔓  Ativar Premium", height=40, width=280, fg_color=("#534AB7", "#3d3589"), hover_color=("#4338CA", "#312e81"), command=mostrar_ativacao).pack(pady=(0,30), padx=80)

def mostrar_ativacao():
    janela = ctk.CTkToplevel()
    janela.title("Ativar Premium")
    janela.geometry("420x220")
    janela.resizable(False, False)
    ctk.CTkLabel(janela, text="🔑  Código de Ativação", font=ctk.CTkFont(size=15, weight="bold")).pack(pady=(24,4), padx=24)
    ctk.CTkLabel(janela, text="Digite o código recebido após o pagamento", font=ctk.CTkFont(size=12), text_color="gray").pack(pady=(0,16), padx=24)
    entrada = ctk.CTkEntry(janela, placeholder_text="GELL-XXXX-XXXX", width=320, height=38)
    entrada.pack(pady=5, padx=24)
    label_msg = ctk.CTkLabel(janela, text="", font=ctk.CTkFont(size=11))
    label_msg.pack(pady=4)
    def ativar():
        codigo = entrada.get().strip()
        if not codigo:
            label_msg.configure(text="⚠️ Digite um código!", text_color="orange")
            return
        label_msg.configure(text="⚠️ Validação online em breve.", text_color="orange")
    ctk.CTkButton(janela, text="Ativar", height=38, width=320, command=ativar).pack(pady=(4,24))

def mostrar_chat(frame_conteudo, frame_principal):
    historico_chat = []

    frame_mensagens = ctk.CTkScrollableFrame(frame_conteudo, fg_color="transparent")
    frame_mensagens.pack(fill="both", expand=True, padx=24, pady=(16,0))

    frame_input = ctk.CTkFrame(frame_conteudo, corner_radius=0)
    frame_input.pack(fill="x", padx=24, pady=16)
    entrada = ctk.CTkEntry(frame_input, placeholder_text="Digite sua mensagem...", height=42)
    entrada.pack(side="left", fill="x", expand=True, padx=(12,8), pady=10)
    ctk.CTkButton(frame_input, text="Enviar", width=90, height=42, command=lambda: enviar()).pack(side="left", padx=(0,12), pady=10)

    def adicionar_mensagem(texto, lado="usuario"):
        frame_msg = ctk.CTkFrame(frame_mensagens, corner_radius=10, fg_color=("gray80", "gray25") if lado == "usuario" else ("#3B82F6", "#1f538d"))
        frame_msg.pack(anchor="e" if lado == "usuario" else "w", pady=4, padx=10)
        ctk.CTkLabel(frame_msg, text=texto, font=ctk.CTkFont(size=12), wraplength=500, justify="left").pack(padx=14, pady=10)

    def enviar():
        mensagem = entrada.get().strip()
        if not mensagem:
            return
        entrada.delete(0, "end")
        adicionar_mensagem(mensagem, "usuario")
        historico_chat.append({"role": "user", "content": mensagem})
        adicionar_mensagem("⏳ Pensando...", "ia")
        def chamar_ia():
            try:
                import urllib.request
                import json
                dados = json.dumps({
                    "model": "claude-sonnet-4-20250514",
                    "max_tokens": 1000,
                    "system": "Você é um assistente de gerenciamento de arquivos chamado Gerenciador LL. Ajude o usuário a organizar, buscar e gerenciar seus arquivos de forma simples e objetiva. Responda sempre em português.",
                    "messages": historico_chat
                }).encode()
                req = urllib.request.Request(
                    "https://api.anthropic.com/v1/messages",
                    data=dados,
                    headers={
                        "Content-Type": "application/json",
                        "x-api-key": CHAVE_API,
                        "anthropic-version": "2023-06-01"
                    }
                )
                with urllib.request.urlopen(req) as resp:
                    resposta = json.loads(resp.read())
                    texto = resposta["content"][0]["text"]
                    historico_chat.append({"role": "assistant", "content": texto})
                    frame_principal.after(0, lambda: atualizar_resposta(texto))
            except Exception as e:
                frame_principal.after(0, lambda: atualizar_resposta(f"❌ Erro ao conectar: {e}"))
        threading.Thread(target=chamar_ia, daemon=True).start()

    def atualizar_resposta(texto):
        widgets = frame_mensagens.winfo_children()
        if widgets:
            widgets[-1].destroy()
        adicionar_mensagem(texto, "ia")

    adicionar_mensagem("Olá! Sou o Assistente IA do Gerenciador LL. Como posso te ajudar a organizar seus arquivos hoje? 😊", "ia")
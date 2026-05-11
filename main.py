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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iterface.dashboard import criar_dashboard
from iterface.organizar import criar_organizar
from iterface.buscar import criar_buscar
from iterface.duplicatas import criar_duplicatas
from iterface.esquecidos import criar_esquecidos
from iterface.limpeza import criar_limpeza
from iterface.cofre import criar_cofre_tela
from iterface.historico import criar_historico
from iterface.tutorial import mostrar_tutorial
from premium.assistente_ia import criar_assistente_ia

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Gerenciador LL")
largura = app.winfo_screenwidth()
altura = app.winfo_screenheight()
app.geometry(f"{int(largura * 0.85)}x{int(altura * 0.85)}")
app.minsize(900, 600)

frame_menu = ctk.CTkFrame(app, width=230, corner_radius=0)
frame_menu.pack(side="left", fill="y")
frame_menu.pack_propagate(False)
frame_principal = ctk.CTkFrame(app, corner_radius=0)
frame_principal.pack(side="left", fill="both", expand=True)

modo_atual = {"valor": "dark"}
botao_ativo = {"btn": None}

def destacar_botao(btn):
    if botao_ativo["btn"]:
        botao_ativo["btn"].configure(fg_color="transparent")
    btn.configure(fg_color=("gray70", "#2b2b2b"))
    botao_ativo["btn"] = btn

def alternar_modo():
    if modo_atual["valor"] == "dark":
        ctk.set_appearance_mode("light")
        modo_atual["valor"] = "light"
        btn_modo.configure(text="🌙  Modo Escuro")
    else:
        ctk.set_appearance_mode("dark")
        modo_atual["valor"] = "dark"
        btn_modo.configure(text="☀️  Modo Claro")

def navegar(tela, btn=None):
    if btn:
        destacar_botao(btn)
    if tela == "dashboard":
        criar_dashboard(frame_principal)
    elif tela == "organizar":
        criar_organizar(frame_principal)
    elif tela == "buscar":
        criar_buscar(frame_principal)
    elif tela == "duplicatas":
        criar_duplicatas(frame_principal)
    elif tela == "esquecidos":
        criar_esquecidos(frame_principal)
    elif tela == "limpeza":
        criar_limpeza(frame_principal)
    elif tela == "cofre":
        criar_cofre_tela(frame_principal)
    elif tela == "historico":
        criar_historico(frame_principal)
    elif tela == "ia":
        criar_assistente_ia(frame_principal)
    elif tela == "tutorial":
        from iterface.tutorial import ARQUIVO_TUTORIAL
        if os.path.exists(ARQUIVO_TUTORIAL):
            os.remove(ARQUIVO_TUTORIAL)
        mostrar_tutorial(app, lambda: criar_dashboard(frame_principal))

def criar_btn(parent, texto, tela):
    btn = ctk.CTkButton(
        parent, text=texto, anchor="w",
        fg_color="transparent",
        hover_color=("gray70", "#2b2b2b"),
        text_color=("gray10", "gray90"),
        corner_radius=6, height=36
    )
    btn.configure(command=lambda t=tela, b=btn: navegar(t, b))
    btn.pack(pady=2, padx=8, fill="x")
    return btn

frame_logo = ctk.CTkFrame(frame_menu, corner_radius=0, fg_color="transparent")
frame_logo.pack(fill="x", padx=16, pady=(20,10))
ctk.CTkLabel(frame_logo, text="Gerenciador LL", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w")
ctk.CTkLabel(frame_logo, text="v1.0.0", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w")

ctk.CTkFrame(frame_menu, height=1, fg_color="gray30").pack(fill="x", padx=16, pady=(0,10))
ctk.CTkLabel(frame_menu, text="PRINCIPAL", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w", padx=16, pady=(8,2))
criar_btn(frame_menu, "📊  Dashboard", "dashboard")
criar_btn(frame_menu, "📁  Organizar", "organizar")
criar_btn(frame_menu, "🔍  Buscar", "buscar")

ctk.CTkFrame(frame_menu, height=1, fg_color="gray30").pack(fill="x", padx=16, pady=(10,2))
ctk.CTkLabel(frame_menu, text="LIMPEZA", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w", padx=16, pady=(4,2))
criar_btn(frame_menu, "👥  Duplicatas", "duplicatas")
criar_btn(frame_menu, "💤  Esquecidos", "esquecidos")
criar_btn(frame_menu, "🧹  Limpeza", "limpeza")

ctk.CTkFrame(frame_menu, height=1, fg_color="gray30").pack(fill="x", padx=16, pady=(10,2))
ctk.CTkLabel(frame_menu, text="EXTRAS", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w", padx=16, pady=(4,2))
criar_btn(frame_menu, "🔐  Cofre", "cofre")
criar_btn(frame_menu, "🕒  Histórico", "historico")
criar_btn(frame_menu, "🤖  Assistente IA 🔒", "ia")

ctk.CTkFrame(frame_menu, height=1, fg_color="gray30").pack(fill="x", padx=16, pady=(10,2), side="bottom")
btn_modo = ctk.CTkButton(
    frame_menu, text="☀️  Modo Claro", anchor="w",
    fg_color="transparent",
    hover_color=("gray70", "#2b2b2b"),
    text_color=("gray10", "gray90"),
    corner_radius=6, height=36, command=alternar_modo
)
btn_modo.pack(pady=2, padx=8, fill="x", side="bottom")
btn_tutorial = ctk.CTkButton(
    frame_menu, text="🎓  Ver Tutorial", anchor="w",
    fg_color="transparent",
    hover_color=("gray70", "#2b2b2b"),
    text_color=("gray10", "gray90"),
    corner_radius=6, height=36, command=lambda: navegar("tutorial")
)
btn_tutorial.pack(pady=2, padx=8, fill="x", side="bottom")

def iniciar():
    criar_dashboard(frame_principal)
    mostrar_tutorial(app, lambda: None)

app.after(500, iniciar)

from utils.tray import minimizar_para_tray

icon_ref = [None]

def ao_fechar():
    minimizar_para_tray(app, icon_ref)

app.protocol("WM_DELETE_WINDOW", ao_fechar)


app.mainloop()
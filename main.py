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
from iterface.dashboard import criar_dashboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.title("Gerenciador LL")
largura = app.winfo_screenwidth()
altura = app.winfo_screenheight()
app.geometry(f"{int(largura * 0.85)}x{int(altura * 0.85)}")
app.minsize(900, 600)
frame_menu = ctk.CTkFrame(app, width=220, corner_radius=0)
frame_menu.pack(side="left", fill="y")
frame_menu.pack_propagate(False)
ctk.CTkLabel(frame_menu, text="Gerenciador LL", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=16, padx=16, anchor="w")
ctk.CTkLabel(frame_menu, text="PRINCIPAL", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w", padx=16, pady=(8,2))
frame_principal = ctk.CTkFrame(app, corner_radius=0, fg_color="#1a1a1a")
frame_principal.pack(side="left", fill="both", expand=True)
for botao in ["📊 Dashboard", "📁 Organizar", "🔍 Buscar"]:
    btn = ctk.CTkButton(frame_menu, text=botao, anchor="w", fg_color="transparent", hover_color="#2b2b2b", corner_radius=6)
    btn.pack(pady=2, padx=8, fill="x")
ctk.CTkLabel(frame_menu, text="LIMPEZA", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w", padx=16, pady=(12,2))
for botao in ["👥 Duplicatas", "💤 Esquecidos", "🧹 Limpeza"]:
    btn = ctk.CTkButton(frame_menu, text=botao, anchor="w", fg_color="transparent", hover_color="#2b2b2b", corner_radius=6)
    btn.pack(pady=2, padx=8, fill="x")
ctk.CTkLabel(frame_menu, text="EXTRAS", font=ctk.CTkFont(size=10), text_color="gray").pack(anchor="w", padx=16, pady=(12,2))
for botao in ["🔐 Cofre", "🕒 Histórico", "🤖 Assistente IA 🔒"]:
    btn = ctk.CTkButton(frame_menu, text=botao, anchor="w", fg_color="transparent", hover_color="#2b2b2b", corner_radius=6)
    btn.pack(pady=2, padx=8, fill="x")


app.mainloop()



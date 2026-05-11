
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
import threading
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.limpeza import listar_arquivos_temporarios, limpar_temporarios

def criar_limpeza(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Limpeza Rápida", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=24, pady=20)

    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", pady=(0,16))
    ctk.CTkButton(frame_topo, text="🔍  Analisar", height=36, command=lambda: analisar()).pack(side="left")
    ctk.CTkButton(frame_topo, text="🧹  Limpar Temporários", height=36, fg_color=("#3B82F6", "#1f538d"), command=lambda: confirmar_limpeza()).pack(side="left", padx=(10,0))

    label_resultado = ctk.CTkLabel(frame_conteudo, text="Clique em Analisar para ver os arquivos temporários", font=ctk.CTkFont(size=12), text_color="gray")
    label_resultado.pack(anchor="w", pady=(0,8))

    progress = ctk.CTkProgressBar(frame_conteudo, height=6)
    progress.pack(fill="x", pady=(0,16))
    progress.set(0)

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Caminho", "Tamanho"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=280, anchor="w").pack(side="left", padx=16, pady=10)

    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)

    def analisar():
        for widget in scroll.winfo_children():
            widget.destroy()
        label_resultado.configure(text="🔍 Analisando arquivos temporários...")
        try:
            progress.stop()
        except:
            pass
        progress.set(0)
        progress.start()
        def _analisar():
            arquivos, total_real = listar_arquivos_temporarios()
            frame_principal.after(0, lambda: mostrar_resultados(arquivos, total_real))
        threading.Thread(target=_analisar, daemon=True).start()

    def mostrar_resultados(arquivos, total_real):
        progress.stop()
        progress.set(1)
        tamanho_total = sum(a[2] for a in arquivos)
        if total_real > 200:
            label_resultado.configure(text=f"✅ Exibindo 200 de {total_real} arquivo(s) temporário(s) — {round(tamanho_total, 2)} MB ocupados")
        else:
            label_resultado.configure(text=f"✅ {total_real} arquivo(s) temporário(s) — {round(tamanho_total, 2)} MB ocupados")
        for nome, caminho, tamanho in arquivos:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            for info in [nome, caminho, f"{tamanho} MB"]:
                ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=280, anchor="w").pack(side="left", padx=16, pady=8)

    def confirmar_limpeza():
        from utils.historico import registrar_acao
        resposta = messagebox.askyesno("Confirmar", "Deseja limpar todos os arquivos temporários do sistema?\n\nEssa ação não pode ser desfeita!")
        if resposta:
            deletados, erros, espaco = limpar_temporarios()
            registrar_acao("Limpeza", f"{deletados} arquivos temporários deletados — {espaco} MB liberados")
            messagebox.showinfo("Concluído", f"✅ {deletados} arquivo(s) deletado(s)!\n💾 {espaco} MB liberados!\n❌ {erros} erros.")
            analisar()

    analisar()
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
from tkinter import filedialog, messagebox
import os
import threading
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.duplicatas import encontrar_duplicatas

def criar_duplicatas(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    topbar = ctk.CTkFrame(frame_principal, height=55, corner_radius=0)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Detector de Duplicatas", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=24, pady=15)

    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="transparent")
    frame_conteudo.pack(fill="both", expand=True, padx=24, pady=20)

    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", pady=(0,16))
    ctk.CTkButton(frame_topo, text="📁  Selecionar Pasta", height=36, command=lambda: selecionar_pasta()).pack(side="left")
    btn_deletar = ctk.CTkButton(frame_topo, text="🗑️  Deletar Duplicatas", height=36, fg_color=("#DC2626", "#7f1d1d"), hover_color=("#B91C1C", "#6b0000"), state="disabled", command=lambda: deletar_duplicatas())
    btn_deletar.pack(side="left", padx=(10,0))

    label_resultado = ctk.CTkLabel(frame_conteudo, text="Selecione uma pasta para analisar", font=ctk.CTkFont(size=12), text_color="gray")
    label_resultado.pack(anchor="w", pady=(0,8))

    progress = ctk.CTkProgressBar(frame_conteudo, height=6)
    progress.pack(fill="x", pady=(0,16))
    progress.set(0)

    frame_lista = ctk.CTkFrame(frame_conteudo, corner_radius=10)
    frame_lista.pack(fill="both", expand=True)

    cabecalho = ctk.CTkFrame(frame_lista, corner_radius=0, fg_color=("gray85", "gray20"))
    cabecalho.pack(fill="x")
    for col in ["Nome", "Caminho", "Tamanho", "Original"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11, weight="bold"), text_color="gray", width=200, anchor="w").pack(side="left", padx=16, pady=10)

    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)
    duplicatas_encontradas = []

    def selecionar_pasta():
        pasta = filedialog.askdirectory()
        if pasta:
            for widget in scroll.winfo_children():
                widget.destroy()
            label_resultado.configure(text="🔍 Analisando em segundo plano...")
            progress.set(0)
            progress.start()
            btn_deletar.configure(state="disabled")
            def buscar():
                duplicatas = encontrar_duplicatas(pasta)
                duplicatas_encontradas.clear()
                duplicatas_encontradas.extend(duplicatas)
                frame_principal.after(0, lambda: mostrar_resultados(duplicatas))
            threading.Thread(target=buscar, daemon=True).start()

    def mostrar_resultados(duplicatas):
        progress.stop()
        progress.set(1)
        tamanho_total = sum(d[2] for d in duplicatas)
        label_resultado.configure(text=f"✅ {len(duplicatas)} duplicata(s) — {round(tamanho_total, 2)} MB ocupados")
        from utils.historico import salvar_stats
        salvar_stats("duplicatas", str(len(duplicatas)), f"{round(tamanho_total, 2)} MB ocupados")
        for nome, caminho, tamanho, original in duplicatas:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            ctk.CTkFrame(linha, height=1, fg_color=("gray85", "gray20")).pack(fill="x")
            frame_linha = ctk.CTkFrame(linha, fg_color="transparent")
            frame_linha.pack(fill="x")
            for info in [nome, caminho, f"{tamanho} MB", original]:
                ctk.CTkLabel(frame_linha, text=info, font=ctk.CTkFont(size=12), width=200, anchor="w").pack(side="left", padx=16, pady=8)
        if duplicatas:
            btn_deletar.configure(state="normal")

    def deletar_duplicatas():
        from utils.historico import registrar_acao
        if not duplicatas_encontradas:
            return
        resposta = messagebox.askyesno("Confirmar", f"Deseja deletar {len(duplicatas_encontradas)} arquivo(s) duplicado(s)?\n\nEssa ação não pode ser desfeita!")
        if resposta:
            deletados = 0
            erros = 0
            for nome, caminho, tamanho, original in duplicatas_encontradas:
                try:
                    os.remove(caminho)
                    deletados += 1
                except:
                    erros += 1
            registrar_acao("Duplicatas", f"{deletados} arquivos duplicados deletados")
            messagebox.showinfo("Concluído", f"✅ {deletados} arquivo(s) deletado(s)!\n❌ {erros} erros.")
            selecionar_pasta()
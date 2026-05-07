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
from core.esquecidos import encontrar_esquecidos

def criar_esquecidos(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()
    topbar = ctk.CTkFrame(frame_principal, height=50, corner_radius=0, fg_color="#2b2b2b")
    topbar.pack(fill="x")
    topbar.pack_propagate(False)
    ctk.CTkLabel(topbar, text="Arquivos Esquecidos", font=ctk.CTkFont(size=15, weight="bold")).pack(side="left", padx=20, pady=15)
    frame_conteudo = ctk.CTkFrame(frame_principal, corner_radius=0, fg_color="#1a1a1a")
    frame_conteudo.pack(fill="both", expand=True, padx=20, pady=20)
    frame_topo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_topo.pack(fill="x", pady=(0,20))
    pasta_var = ctk.StringVar(value="Nenhuma pasta selecionada")
    ctk.CTkLabel(frame_topo, textvariable=pasta_var, font=ctk.CTkFont(size=12), text_color="gray").pack(side="left", padx=(0,10))
    ctk.CTkButton(frame_topo, text="📁 Selecionar Pasta", command=lambda: selecionar_pasta()).pack(side="left")
    ctk.CTkLabel(frame_topo, text="Sem uso há mais de:", font=ctk.CTkFont(size=12)).pack(side="left", padx=(20,5))
    opcao_dias = ctk.CTkOptionMenu(frame_topo, values=["180 dias", "365 dias", "730 dias", "1825 dias"])
    opcao_dias.pack(side="left")
    opcao_dias.set("365 dias")
    btn_deletar = ctk.CTkButton(frame_topo, text="🗑️ Deletar Selecionados", fg_color="#8b0000", hover_color="#6b0000", state="disabled", command=lambda: deletar_esquecidos())
    btn_deletar.pack(side="left", padx=(10,0))
    label_resultado = ctk.CTkLabel(frame_conteudo, text="", font=ctk.CTkFont(size=12), text_color="gray")
    label_resultado.pack(anchor="w", pady=(0,8))
    progress = ctk.CTkProgressBar(frame_conteudo)
    progress.pack(fill="x", pady=(0,10))
    progress.set(0)
    frame_lista = ctk.CTkFrame(frame_conteudo, fg_color="#2b2b2b", corner_radius=8)
    frame_lista.pack(fill="both", expand=True)
    cabecalho = ctk.CTkFrame(frame_lista, fg_color="#333333", corner_radius=0)
    cabecalho.pack(fill="x")
    for col in ["Nome", "Caminho", "Tamanho", "Sem uso há"]:
        ctk.CTkLabel(cabecalho, text=col, font=ctk.CTkFont(size=11), text_color="gray", width=200, anchor="w").pack(side="left", padx=14, pady=8)
    scroll = ctk.CTkScrollableFrame(frame_lista, fg_color="transparent")
    scroll.pack(fill="both", expand=True)
    esquecidos_encontrados = []

    def verificar_tamanho(pasta):
        tamanho = 0
        try:
            for raiz, dirs, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    tamanho += os.path.getsize(os.path.join(raiz, arquivo))
                    if tamanho > 20 * 1024 * 1024 * 1024:
                        return tamanho
        except:
            pass
        return tamanho

    def buscar(pasta):
        for widget in scroll.winfo_children():
            widget.destroy()
        dias = int(opcao_dias.get().split()[0])
        label_resultado.configure(text="🔍 Analisando arquivos...")
        progress.set(0)
        progress.start()
        btn_deletar.configure(state="disabled")
        def atualizar_progresso(total):
            frame_principal.after(0, lambda: label_resultado.configure(text=f"🔍 Analisando... {total} arquivos verificados"))
        def _buscar():
            esquecidos = encontrar_esquecidos(pasta, dias, callback=atualizar_progresso)
            esquecidos_encontrados.clear()
            esquecidos_encontrados.extend(esquecidos)
            frame_principal.after(0, lambda: mostrar_resultados(esquecidos))
        threading.Thread(target=_buscar, daemon=True).start()

    def selecionar_pasta():
        pasta = filedialog.askdirectory()
        if pasta:
            pasta_var.set(pasta)
            tamanho = verificar_tamanho(pasta)
            if tamanho > 20 * 1024 * 1024 * 1024:
                resposta = messagebox.askquestion("Atenção", "A pasta selecionada é muito grande (mais de 20 GB).\n\nA análise pode demorar bastante.\n\nDeseja continuar mesmo assim?", icon="warning")
                if resposta == "yes":
                    buscar(pasta)
            else:
                buscar(pasta)

    opcao_dias.configure(command=lambda _: buscar(pasta_var.get()) if pasta_var.get() != "Nenhuma pasta selecionada" else None)

    def mostrar_resultados(esquecidos):
        progress.stop()
        progress.set(1)
        tamanho_total = sum(e[2] for e in esquecidos)
        label_resultado.configure(text=f"✅ {len(esquecidos)} arquivo(s) encontrado(s) — {round(tamanho_total, 2)} MB ocupados")
        for nome, caminho, tamanho, dias in esquecidos:
            linha = ctk.CTkFrame(scroll, fg_color="transparent", corner_radius=0)
            linha.pack(fill="x")
            for info in [nome, caminho, f"{tamanho} MB", f"{dias} dias"]:
                ctk.CTkLabel(linha, text=info, font=ctk.CTkFont(size=12), width=200, anchor="w").pack(side="left", padx=14, pady=6)
        if esquecidos:
            btn_deletar.configure(state="normal")

    def deletar_esquecidos():
        if not esquecidos_encontrados:
            return
        resposta = messagebox.askyesno("Confirmar", f"Deseja deletar {len(esquecidos_encontrados)} arquivo(s) esquecido(s)?\n\nEssa ação não pode ser desfeita!")
        if resposta:
            deletados = 0
            erros = 0
            for nome, caminho, tamanho, dias in esquecidos_encontrados:
                try:
                    os.remove(caminho)
                    deletados += 1
                except Exception as e:
                    erros += 1
            messagebox.showinfo("Concluído", f"✅ {deletados} arquivo(s) deletado(s)!\n❌ {erros} erros.")
            buscar(pasta_var.get())
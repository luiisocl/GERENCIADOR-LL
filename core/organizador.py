"""
Gerenciador LL
==============
Autor: Luis Leal
GitHub: github.com/luiisocl/GERENCIADOR-LL
Versão: 1.0.0
Descrição: Gerenciador de arquivos inteligente com IA integrada
Licença: Todos os direitos reservados © 2026 Luis Leal
"""
import os
import shutil

def identificar_tipo(arquivo):
    extensoes = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
        "Musicas": [".mp3", ".wav", ".flac", ".aac"],
        "Programas": [".exe", ".msi", ".bat"],
        "Compactados": [".zip", ".rar", ".7z", ".tar"],
    }
    _, ext = os.path.splitext(arquivo.lower())
    for tipo, lista in extensoes.items():
        if ext in lista:
            return tipo
    return "Outros"

def listar_arquivos(pasta):
    resultado = []
    try:
        for arquivo in os.listdir(pasta):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                tamanho = os.path.getsize(caminho)
                tamanho_mb = round(tamanho / 1024 / 1024, 2)
                tipo = identificar_tipo(arquivo)
                resultado.append((arquivo, tipo, tamanho_mb))
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")
    return resultado

def organizar_pasta(pasta, callback=None):
    arquivos = listar_arquivos(pasta)
    organizados = 0
    erros = 0
    for nome, tipo, tamanho in arquivos:
        try:
            pasta_destino = os.path.join(pasta, tipo)
            os.makedirs(pasta_destino, exist_ok=True)
            origem = os.path.join(pasta, nome)
            destino = os.path.join(pasta_destino, nome)
            shutil.move(origem, destino)
            organizados += 1
            if callback:
                callback(nome)
        except Exception as e:
            erros += 1
            print(f"Erro ao mover {nome}: {e}")
    return organizados, erros
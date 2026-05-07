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

def buscar_arquivos(pasta, termo, callback=None):
    resultado = []
    try:
        for raiz, dirs, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if termo.lower() in arquivo.lower():
                    caminho = os.path.join(raiz, arquivo)
                    tamanho = os.path.getsize(caminho)
                    tamanho_mb = round(tamanho / 1024 / 1024, 2)
                    resultado.append((arquivo, caminho, tamanho_mb))
                    if callback:
                        callback(arquivo)
    except Exception as e:
        print(f"Erro ao buscar: {e}")
    return resultado
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

PASTAS_TEMPORARIAS = [
    os.environ.get("TEMP", ""),
    os.environ.get("TMP", ""),
    os.path.join(os.environ.get("LOCALAPPDATA", ""), "Temp"),
]

def listar_arquivos_temporarios(limite=200):
    arquivos = []
    total_real = 0
    for pasta in PASTAS_TEMPORARIAS:
        if not pasta or not os.path.exists(pasta):
            continue
        try:
            for nome in os.listdir(pasta):
                caminho = os.path.join(pasta, nome)
                try:
                    if os.path.isfile(caminho):
                        total_real += 1
                        if len(arquivos) < limite:
                            tamanho = round(os.path.getsize(caminho) / 1024 / 1024, 2)
                            arquivos.append((nome, caminho, tamanho))
                except:
                    continue
        except:
            continue
    return arquivos, total_real

def limpar_temporarios():
    deletados = 0
    erros = 0
    espaco = 0
    for pasta in PASTAS_TEMPORARIAS:
        if not pasta or not os.path.exists(pasta):
            continue
        try:
            for nome in os.listdir(pasta):
                caminho = os.path.join(pasta, nome)
                try:
                    if os.path.isfile(caminho):
                        espaco += os.path.getsize(caminho)
                        os.remove(caminho)
                        deletados += 1
                except:
                    erros += 1
        except:
            continue
    return deletados, erros, round(espaco / 1024 / 1024, 2)

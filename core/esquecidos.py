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
import datetime
PASTAS_IGNORADAS = [
    "Windows", "Program Files", "Program Files (x86)",
    "ProgramData", "AppData", "System Volume Information",
    "$Recycle.Bin", "Recovery", "Boot", "__pycache__",
    ".git", "node_modules"
]

def encontrar_esquecidos(pasta, dias=365, callback=None):
    esquecidos = []
    agora = datetime.datetime.now()
    total_analisados = 0
    try:
        for raiz, dirs, arquivos in os.walk(pasta):
            dirs[:] = [d for d in dirs if d not in PASTAS_IGNORADAS]
            for arquivo in arquivos:
                caminho = os.path.join(raiz, arquivo)
                try:
                    ultimo_acesso = os.path.getatime(caminho)
                    data_acesso = datetime.datetime.fromtimestamp(ultimo_acesso)
                    diferenca = (agora - data_acesso).days
                    if diferenca >= dias:
                        tamanho = round(os.path.getsize(caminho) / 1024 / 1024, 2)
                        esquecidos.append((arquivo, caminho, tamanho, diferenca))
                    total_analisados += 1
                    if callback and total_analisados % 100 == 0:
                        callback(total_analisados)
                except:
                    continue
    except Exception as e:
        print(f"Erro ao buscar esquecidos: {e}")
    esquecidos.sort(key=lambda x: x[3], reverse=True)
    return esquecidos
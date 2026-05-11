"""
Gerenciador LL
==============
Autor: Luis Leal
GitHub: github.com/luiisocl/GERENCIADOR-LL
Versão: 1.0.0
Descrição: Gerenciador de arquivos inteligente com IA integrada
Licença: Todos os direitos reservados © 2026 Luis Leal
"""
import json
import os
from datetime import datetime

ARQUIVO_HISTORICO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".historico.json")

def registrar_acao(acao, detalhes=""):
    historico = carregar_historico()
    historico.insert(0, {
        "acao": acao,
        "detalhes": detalhes,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    })
    historico = historico[:100]
    with open(ARQUIVO_HISTORICO, "w") as f:
        json.dump(historico, f, ensure_ascii=False)

def carregar_historico():
    if not os.path.exists(ARQUIVO_HISTORICO):
        return []
    try:
        with open(ARQUIVO_HISTORICO, "r") as f:
            return json.load(f)
    except:
        return []

def limpar_historico():
    with open(ARQUIVO_HISTORICO, "w") as f:
        json.dump([], f)
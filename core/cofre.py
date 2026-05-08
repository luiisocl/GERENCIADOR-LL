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
import json
import hashlib
import shutil
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

PASTA_COFRE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".cofre")
ARQUIVO_CONFIG = os.path.join(PASTA_COFRE, "config.json")
SALT = b"gerenciador_ll_salt_2026"

def inicializar_cofre():
    if not os.path.exists(PASTA_COFRE):
        os.makedirs(PASTA_COFRE)

def gerar_chave(senha):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=SALT, iterations=100000)
    chave = base64.urlsafe_b64encode(kdf.derive(senha.encode()))
    return chave

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cofre_existe():
    return os.path.exists(ARQUIVO_CONFIG)

def criar_cofre(senha):
    inicializar_cofre()
    config = {"senha": hash_senha(senha), "arquivos": []}
    with open(ARQUIVO_CONFIG, "w") as f:
        json.dump(config, f)
    return True

def verificar_senha(senha):
    if not cofre_existe():
        return False
    with open(ARQUIVO_CONFIG, "r") as f:
        config = json.load(f)
    return config["senha"] == hash_senha(senha)

def adicionar_arquivo(caminho_original, senha):
    if not verificar_senha(senha):
        return False
    chave = gerar_chave(senha)
    fernet = Fernet(chave)
    with open(caminho_original, "rb") as f:
        dados = f.read()
    dados_criptografados = fernet.encrypt(dados)
    nome = os.path.basename(caminho_original)
    destino = os.path.join(PASTA_COFRE, nome + ".enc")
    with open(destino, "wb") as f:
        f.write(dados_criptografados)
    os.remove(caminho_original)
    with open(ARQUIVO_CONFIG, "r") as f:
        config = json.load(f)
    config["arquivos"].append({"nome": nome, "original": caminho_original})
    with open(ARQUIVO_CONFIG, "w") as f:
        json.dump(config, f)
    return True

def listar_arquivos_cofre(senha):
    if not verificar_senha(senha):
        return None
    with open(ARQUIVO_CONFIG, "r") as f:
        config = json.load(f)
    return config["arquivos"]

def remover_arquivo(nome, senha):
    if not verificar_senha(senha):
        return False
    chave = gerar_chave(senha)
    fernet = Fernet(chave)
    with open(ARQUIVO_CONFIG, "r") as f:
        config = json.load(f)
    for arquivo in config["arquivos"]:
        if arquivo["nome"] == nome:
            origem = os.path.join(PASTA_COFRE, nome + ".enc")
            with open(origem, "rb") as f:
                dados_criptografados = f.read()
            dados = fernet.decrypt(dados_criptografados)
            with open(arquivo["original"], "wb") as f:
                f.write(dados)
            os.remove(origem)
            config["arquivos"].remove(arquivo)
            with open(ARQUIVO_CONFIG, "w") as f:
                json.dump(config, f)
            return True
    return False
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
import hashlib

def calcular_hash(caminho):
    try:
        hash_md5 = hashlib.md5()
        with open(caminho, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Erro ao calcular hash: {e}")
        return None

def encontrar_duplicatas(pasta):
    tamanhos = {}
    duplicatas = []
    try:
        for raiz, dirs, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                caminho = os.path.join(raiz, arquivo)
                try:
                    tamanho = os.path.getsize(caminho)
                    if tamanho == 0:
                        continue
                    if tamanho in tamanhos:
                        tamanhos[tamanho].append(caminho)
                    else:
                        tamanhos[tamanho] = [caminho]
                except:
                    continue
        for tamanho, caminhos in tamanhos.items():
            if len(caminhos) < 2:
                continue
            hashes = {}
            for caminho in caminhos:
                hash_arquivo = calcular_hash(caminho)
                if hash_arquivo:
                    if hash_arquivo in hashes:
                        nome = os.path.basename(caminho)
                        tamanho_mb = round(tamanho / 1024 / 1024, 2)
                        duplicatas.append((nome, caminho, tamanho_mb, hashes[hash_arquivo]))
                    else:
                        hashes[hash_arquivo] = caminho
    except Exception as e:
        print(f"Erro ao buscar duplicatas: {e}")
    return duplicatas
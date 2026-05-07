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

pasta = "C:/Users/Luis Guilherme/Documents"

arquivos  = os.listdir(pasta)

print("=== Gerenciador LL ===")
print(f"Arquivos encontrados: {len(arquivos)}")
print("-----------------------------")


for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_completo):
        tamanho = os.path.getsize(caminho_completo)
        tamanho_mb = round(tamanho /1024/ 1024, 2)

        data_modificacao = os.path.getmtime(caminho_completo)
        data= datetime.datetime.fromtimestamp(data_modificacao)

        data_formatada = data.strftime("%d/%m/%Y")


        print(f"Arquivo: {arquivo} | Tamanho: {tamanho_mb} MB | Data de Modificação: {data_formatada}")
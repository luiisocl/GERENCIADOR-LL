"""
Gerenciador LL
==============
Autor: Luis Leal
GitHub: github.com/luiisocl/GERENCIADOR-LL
Versão: 1.0.0
Descrição: Gerenciador de arquivos inteligente com IA integrada
Licença: Todos os direitos reservados © 2026 Luis Leal
"""
import pystray
from PIL import Image, ImageDraw
import threading
import os
import sys

def criar_icone_tray():
    img = Image.new("RGB", (64, 64), color="#1a1a1a")
    draw = ImageDraw.Draw(img)
    draw.rectangle([8, 8, 56, 56], fill="#3B82F6")
    draw.text((20, 20), "GL", fill="white")
    return img

def iniciar_tray(app, mostrar_callback, fechar_callback):
    icone_img = criar_icone_tray()

    def mostrar(icon, item):
        icon.stop()
        app.after(0, mostrar_callback)

    def fechar(icon, item):
        icon.stop()
        app.after(0, fechar_callback)

    menu = pystray.Menu(
        pystray.MenuItem("Abrir Gerenciador LL", mostrar, default=True),
        pystray.MenuItem("Fechar", fechar)
    )

    icon = pystray.Icon("Gerenciador LL", icone_img, "Gerenciador LL", menu)
    threading.Thread(target=icon.run, daemon=True).start()
    return icon

def minimizar_para_tray(app, icon_ref):
    app.withdraw()
    if not icon_ref[0]:
        def mostrar():
            app.deiconify()
            icon_ref[0].stop()
            icon_ref[0] = None
        def fechar():
            app.quit()
        icon_ref[0] = iniciar_tray(app, mostrar, fechar)
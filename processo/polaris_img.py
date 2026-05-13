import pywhatkit
import pyautogui
import time
import os

contatos = [
    "+5541998938623",
    "+5541988400905"
]

caminho_foto = os.path.abspath("images.jfif")  # Caminho absoluto da foto

legenda = """Mousse de maracujá hoje no cursinho! 😋
R$8,00"""

for numero in contatos:
    try:
        print(f"Enviando foto pra {numero}...")

        pywhatkit.sendwhats_image(
            receiver=numero,
            img_path=caminho_foto,
            caption=legenda,
            wait_time=30,  # Aumentado para 30 segundos
            tab_close=False,
            close_time=3
        )

        print("Aguardando carregamento da imagem...")
        time.sleep(15)  # Aumentado para 15 segundos

        # ENTER envia
        pyautogui.press("enter")

        print(f"Foto enviada pra {numero}")

    except Exception as e:
        print(f"Erro com {numero}: {e}")
        time.sleep(10)

print("Tudo enviado 🎉")
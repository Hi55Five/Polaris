import pywhatkit
import pyautogui
import time

# Lista de contatos
contatos = [
    "+5541998938623",
    "+5541988400905"
]

mensagem = """Oii, tudo bem? 😊
Passando pra avisar que estarei vendendo mousse de maracujá no cursinho!
Tenho maracujá com biscoito e maracujá com chocolate por R$8,00
Já separa o seu!"""

def disparar_mousse():
    for i, numero in enumerate(contatos):
        try:
            print(f"Enviando {i+1}/{len(contatos)} para {numero}...")

            pywhatkit.sendwhatmsg_instantly(
                phone_no=numero,
                message=mensagem,
                wait_time=20,
                tab_close=False
            )

            time.sleep(5)

            pyautogui.press("enter")

            print(f"Enviado com sucesso pra {numero}")

            time.sleep(5)

        except Exception as erro:
            print(f"Moiou com {numero}: {erro}")
            time.sleep(10)

    print("Acabou! Todos os mousses foram divulgados 🎉")

if __name__ == "__main__":
    disparar_mousse()
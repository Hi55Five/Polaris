import time
import pywhatkit


numero_destino = "+5541998938623" 
mensagem = "Oii, tudo bem?" \
"Passando pra avisar que estarei vendendo mousse de maracujá no cursinho!" \
"Tenho maracujá com biscoito e maracujá com chocolate por R$8,00" \
""
pywhatkit.sendwhatmsg_instantly(numero_destino, mensagem, 30, True, 3)

print("Comando enviado! O robô vai começar a trabalhar no horário marcado.")

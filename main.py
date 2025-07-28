import google.generativeai as genai
import time
import sys
from colorama import Fore, Style, init
import pyttsx3
from datetime import datetime

init(autoreset=True)

API_KEY = "sua_api"
genai.configure(api_key=API_KEY)

modelo = genai.GenerativeModel("gemini-2.5-flash")
chat = modelo.start_chat()
chat.send_message("Responda sempre em português.")

voz = pyttsx3.init()
voices = voz.getProperty('voices')
for v in voices:
    if 'female' in v.name.lower() or 'female' in v.id.lower():
        voz.setProperty('voice', v.id)
        break

voz.setProperty('rate', 180)
voz.setProperty('volume', 1)

usar_audio = input(Fore.CYAN + "\n🔈 Deseja ouvir as respostas com voz? (s/n): " + Style.RESET_ALL).strip().lower() == "s"

mensagem_inicio = Style.BRIGHT + "\n\t\t🤖 Olá! Sou o Gemini. Estou pronto para te ajudar.\n\t\tDigite 'sair' a qualquer momento para encerrar.\n"
print(Fore.MAGENTA + mensagem_inicio + Style.RESET_ALL)
if usar_audio:
    voz.say("Olá! Eu sou o Gemini. Estou pronto para te ajudar. Você pode digitar sair a qualquer momento para encerrar.")
    voz.runAndWait()

data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
historico = []
inicio = time.time()

while True:
    mensagem = input(Fore.GREEN + "[ 👨🏻‍💻 Você ] ➤  " + Style.RESET_ALL)
    if mensagem.strip().lower() == "sair":
        print(Fore.MAGENTA + "👋🏻 Até logo!")
        fim = time.time()
        duracao = int(fim - inicio)
        minutos = duracao // 60
        segundos = duracao % 60
        print(Fore.YELLOW + f"\n🕒 Sessão encerrada. Duração: {minutos} min {segundos} seg." + Style.RESET_ALL)
        if usar_audio:
            voz.say(f"A sessão durou {minutos} minutos e {segundos} segundos.")
            voz.runAndWait()
        break

    resposta = chat.send_message(mensagem)
    print("🤖 Gemini está digitando...", end="\r")
    for _ in range(3):
        time.sleep(0.5)
        print(Fore.MAGENTA + ".", end="")
        sys.stdout.flush()
    time.sleep(0.5)
    print(" " * 50, end="\r")

    print(Fore.MAGENTA + "[  🤖 Gemini ] ➤  " + resposta.text + Style.RESET_ALL)

    if usar_audio:
        voz.say(resposta.text)
        voz.runAndWait()

    historico.append(f"[ 👨🏻‍💻 Você ] ➤  {mensagem}")
    historico.append(f"[  🤖 Gemini ] ➤  {resposta.text}")

with open("chat.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"📌 NOVA CONVERSA 📌- {data_hora}\n\n")
    arquivo.write("\n".join(historico))
    arquivo.write("\n" + "-" * 50 + "\n")

mensagem_final = Style.BRIGHT + "📄 A conversa foi salva no nosso banco de dados com sucesso!"
print(Fore.YELLOW + mensagem_final + Style.RESET_ALL)
voz.say("Seu bate-papo foi arquivado com sucesso.")
voz.runAndWait()

import random
import time
import os

def boas_vindas():
    print("Olá, sou o AunascBot, seu assistente de educação financeira")
    print("Vou te ajudar a entender economia e investimentos de forma simples!\n")

def dica_financeira():
    dicas = [
        "Comece criando uma reserva de emergência.",
        "Evite parcelar compras desncessárias.",
        "Invista de forma constante, mesmo que pouco.",
        "Reinvista seus lucros para acelerar  crescimento.",
        "Acompanhe gastos e monte um orçamento mensal."
    ]
    print(random.choice(dicas))

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(segundos=2):
    time.sleep(segundos)
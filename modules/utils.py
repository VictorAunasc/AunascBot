import random
import time
import os
import json

def boas_vindas():
    print("Olá, sou o AunascBot, seu assistente de educação financeira")
    print("Vou te ajudar a entender economia e investimentos de forma simples!\n")

def dica_financeira():
    """Dica usada tanto no menu quanto de forma automática."""
    dicas = [
        "Comece criando uma reserva de emergência.",
        "Evite parcelar compras desnecessárias.",
        "Invista de forma constante, mesmo que pouco.",
        "Reinvista seus lucros para acelerar o crescimento.",
        "Acompanhe seus gastos e monte um orçamento mensal."
    ]
    print("\n💡 Dica financeira:")
    print(random.choice(dicas))

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(segundos=2):
    time.sleep(segundos)

def obter_usuario():
    caminho_arquivo = os.path.join("data", "usuario.json")

    if os.path.isfile(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return dados.get("nome")
        except (json.JSONDecodeError, FileNotFoundError):
            pass

    nome = input("Olá! Qual o seu nome?: ")
    os.makedirs("data", exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump({"nome": nome}, f, ensure_ascii=False, indent=2)
    return nome


def boas_vindas_personalizadas():
    nome = obter_usuario()
    print(f"\n👋 Olá, {nome}! Seja bem-vindo(a) ao AunascBot 💰")
    print("Eu vou te ajudar a entender economia e investimentos de forma simples!\n")


def dica_automatica_inicio():
    """Dica automática exibida assim que o bot inicia."""
    print("\n🔔 Antes de começar, aqui vai uma dica automática pra você:")
    dica_financeira()
    pausar(2)

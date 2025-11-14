import os
import json
from datetime import datetime
import matplotlib.pyplot as plt


def simular_poupanca():
    print("\n--- Simulação de Poupança ---")

    try:
        valor_mensal = float(input("Digite quanto você quer guardar por mês (R$): "))
        meses = int(input("Por quantos meses pretende guardar? "))
        rendimento_mensal = float(input("Qual o rendimento mensal esperado? (%): "))

        # converte percentual para número decimal
        taxa = rendimento_mensal / 100
        total = 0
        historico = []

        for _ in range(meses):
            total = (total + valor_mensal) * (1 + taxa)
            historico.append(total)

        print(f"\nSe você guardar R${valor_mensal:.2f} por {meses} meses a {rendimento_mensal}% ao mês,")
        print(f"terá aproximadamente R${total:,.2f} ao final.")
        print(f"Somente em juros, você teria ganho cerca de R${total - (valor_mensal * meses):,.2f} 💸")

        # registrar simulação no histórico
        registrar_simulacao(valor_mensal, meses, rendimento_mensal, total)

        # sugerir conquistas com base no total
        sugerir_conquistas(total)

        # exibir gráfico
        exibir_grafico(historico, meses, valor_mensal, rendimento_mensal)

    except ValueError:
        print("\n⚠️ Entrada inválida! Digite apenas números.")


def registrar_simulacao(valor_mensal, meses, rendimento_mensal, total):
    """
    Registra cada simulação em data/historico_simulacoes.json
    para acompanhar a evolução do usuário ao longo do tempo.
    """
    os.makedirs("data", exist_ok=True)
    caminho_arquivo = os.path.join("data", "historico_simulacoes.json")

    registro = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "valor_mensal": valor_mensal,
        "meses": meses,
        "rendimento_mensal": rendimento_mensal,
        "total_final": total
    }

    historico = []
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                historico = json.load(f)
        except json.JSONDecodeError:
            historico = []

    historico.append(registro)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def sugerir_conquistas(total):
    """
    Lê data/conquistas.json e sugere objetivos que cabem
    dentro do valor total acumulado.
    """
    caminho_arquivo = os.path.join("data", "conquistas.json")
    if not os.path.exists(caminho_arquivo):
        return

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conquistas = json.load(f)
    except json.JSONDecodeError:
        print("\nNão foi possível carregar a lista de conquistas.")
        return

    possiveis = {nome: valor for nome, valor in conquistas.items() if valor <= total}

    print("\n🎯 Com esse valor, você já poderia considerar:")
    if not possiveis:
        print("- Ainda nenhuma conquista da nossa lista. Continue firme que você chega lá! 💪")
    else:
        for nome, valor in possiveis.items():
            print(f"- {nome} (aprox. R${valor:,.2f})")


def exibir_grafico(historico, meses, valor_mensal, rendimento_mensal):
    """
    Exibe um gráfico de linha com a evolução da poupança mês a mês.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, meses + 1), historico, marker='o', linestyle='-', linewidth=2)
    plt.title(f"Evolução da Poupança ({rendimento_mensal}% ao mês)")
    plt.xlabel("Meses")
    plt.ylabel("Valor acumulado (R$)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

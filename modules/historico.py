import json
import os

def ver_historico():
    caminho_arquivo = os.path.join("data", "historico_simulacoes.json")

    if not os.path.exists(caminho_arquivo):
        print("\nAinda não há histórico de simulações. Faça uma simulação primeiro. 🙂")
        return

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            historico = json.load(f)
    except json.JSONDecodeError:
        print("\nNão foi possível ler o histórico de simulações.")
        return

    if not historico:
        print("\nO histórico está vazio no momento.")
        return

    print("\n--- Histórico de Simulações ---")
    print(f"Total de simulações registradas: {len(historico)}\n")

    # Mostra as últimas 5 simulações (ou menos, se tiver poucas)
    ultimas = historico[-5:]

    for idx, sim in enumerate(ultimas, start=1):
        print(f"Simulação {idx}:")
        print(f" - Data/hora:          {sim.get('data_hora')}")
        print(f" - Valor mensal:       R${sim.get('valor_mensal', 0):.2f}")
        print(f" - Meses:              {sim.get('meses')}")
        print(f" - Rendimento mensal:  {sim.get('rendimento_mensal')}%")
        print(f" - Total final:        R${sim.get('total_final', 0):.2f}")
        print("-" * 40)

    # Estatísticas simples
    totais = [s.get("total_final", 0) for s in historico]
    if totais:
        maior = max(totais)
        menor = min(totais)
        media = sum(totais) / len(totais)

        print("\n📊 Resumo geral:")
        print(f" - Maior total simulado: R${maior:,.2f}")
        print(f" - Menor total simulado: R${menor:,.2f}")
        print(f" - Média dos totais:     R${media:,.2f}\n")

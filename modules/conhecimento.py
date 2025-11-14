import json
import os
import textwrap

def pesquisar_conceito():
    print("\n--- Pesquisa de Conceitos Financeiros ---")
    consulta = input("Digite sua dúvida ou palavra-chave (ex: inflação, PIB, renda fixa): ").strip()

    if not consulta:
        print("Nenhuma consulta informada. Voltando ao menu...\n")
        return

    caminho_arquivo = os.path.join("data", "base_conhecimento.json")

    if not os.path.exists(caminho_arquivo):
        print("Base de conhecimento não encontrada. Fale com o desenvolvedor.")
        return

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            base = json.load(f)
    except json.JSONDecodeError:
        print("Erro ao ler a base de conhecimento. Verifique o arquivo JSON.")
        return

    consulta_lower = consulta.lower()
    respostas_encontradas = []

    for item in base:
        termos = item.get("termos", [])
        resposta = item.get("resposta", "")

        for termo in termos:
            termo_lower = termo.lower()
            if termo_lower in consulta_lower or consulta_lower in termo_lower:
                respostas_encontradas.append(resposta)
                break  # evita duplicar a mesma resposta

    if not respostas_encontradas:
        print("\nAinda não tenho uma resposta específica para isso.")
        print("Tente usar outra palavra-chave como 'inflação', 'juros compostos' ou 'renda fixa'.\n")
        return

    print("\n Encontrei o seguinte para você:\n")
    for resposta in respostas_encontradas:
        print(textwrap.fill(resposta, width=80))
        print()

def explicar_investimentos():
    print("\n Tipos de investimentos:")
    print("1 - Renda Fixa")
    print("2 - Renda Variável")
    print("3 - Fundos Imobiliarios (FIIs)")
    print("4 - Comparar Renda Fixa e Renda Variável")
    print("0 - Voltar")

    escolha = input("Escolha uma opção:")

    investimentos = {
         "1": "💵 Renda Fixa: você sabe quanto vai receber e quando. Exemplos: CDB, Tesouro Direto, LCI/LCA. "
             "Indicada para quem busca segurança e previsibilidade.",

        "2": "📈 Renda Variável: o retorno depende do mercado, podendo variar para mais ou para menos. "
             "Exemplos: ações, ETFs e criptomoedas. Indicada para quem aceita mais risco buscando maiores ganhos.",

        "3": "🏢 Fundos Imobiliários (FIIs): reúnem investidores para aplicar em imóveis e distribuem parte dos lucros mensalmente. "
             "São negociados na bolsa e combinam renda com potencial de valorização.",
    }

    if escolha in investimentos:
        print (investimentos[escolha])

    elif escolha == "4":
        comparar_investimentos()

    elif escolha == "0":
        print("Voltando ao Menu principal...\n")

    else:
        print("Opção Inválida. Tente novamente.")


def comparar_investimentos():
    print("\n--- Comparativo: Renda Fixa x Renda Variável ---")
    print("""
    📊 Renda Fixa:
     - Menor risco
     - Retornos previsíveis
     - Ideal para reserva de emergência ou curto prazo

    📈 Renda Variável:
     - Maior risco
     - Retornos imprevisíveis
     - Ideal para longo prazo e aumento de patrimônio
    """)



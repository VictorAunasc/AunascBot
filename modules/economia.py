# modules/economia.py

def explicar_conceito():
    print("\n--- Conceitos de Economia ---")
    print("1 - Inflação")
    print("2 - PIB")
    print("3 - Juros Compostos")
    print("4 - Oferta e Demanda")
    print("5 - Câmbio")
    print("0 - Voltar")

    escolha = input("Escolha um conceito: ")

    conceitos = {
        "1": "📈 Inflação é o aumento geral dos preços, diminuindo o poder de compra do dinheiro.",
        "2": "💰 PIB (Produto Interno Bruto) é o valor total de bens e serviços produzidos por um país em um período.",
        "3": "💸 Juros compostos são juros calculados sobre o valor inicial + os juros acumulados anteriormente.",
        "4": "⚖️ Oferta e demanda determinam os preços: quando algo é escasso e muito procurado, seu preço tende a subir.",
        "5": "🌎 Câmbio é o valor da moeda de um país em relação à moeda de outro, como o real frente ao dólar."
    }

    if escolha in conceitos:
        print("\n" + conceitos[escolha])
    elif escolha == "0":
        print("Voltando ao menu principal...\n")
    else:
        print("Opção inválida. Tente novamente.")

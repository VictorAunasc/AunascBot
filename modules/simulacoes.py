def simular_poupanca():
    print("\n Simulação de Poupança")

    try:
        valor_mensal = float(input("Digite quanto você quer guardar por mês: "))
        meses = int(input("Por quantos meses pretende guardar? "))
        rendimento_mensal = float(input("Qual o rendimento mensal esperado? (%):"))

        #converte percential para número decimal
        taxa = rendimento_mensal/100

        total = 0
        for _ in range(meses):
            total = (total + valor_mensal) * (1+taxa)

        print(f"\nSe você guardar R${valor_mensal:.2f} por {meses} meses a {rendimento_mensal}% ao mês,")
        print(f"terá aproximadamente R${total:,.2f} ao final.")
        print(f"Somente em juros, você teria ganho cerca de R${total - (valor_mensal * meses):,.2f} 💸")

    except ValueError:
        print("\n⚠️ Entrada inválida! Digite apenas números.")
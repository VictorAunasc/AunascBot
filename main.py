# main.py - ponto de entrada do AunasBot

from modules import economia, investimentos, simulacoes, utils #importa os modulos

def exibir_menu():
    print("\n === AunascBot $$$ Educação Financeira===")
    print("1 - Conceitos de Economia")
    print("2 - Tipos de Investimentos")
    print("3 - Simular Poupança")
    print("4 - Dica Financeira Aleatória")
    print("0 - Sair")

def main():
    utils.boas_vindas()

    while True:
        exibir_menu()
        opcao = input("Escolja uma opção: ")
        if opcao == "1":
            economia.explicar_conceito()
        elif opcao == "2":
            investimentos.explicar_investimentos()
        elif opcao == "3":
            simulacoes.simular_poupanca()
        elif opcao == "4":
            utils.dica_financeira()
            utils.pausar()
            utils.limpar_tela()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()
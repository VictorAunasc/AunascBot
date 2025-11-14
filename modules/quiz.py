# modules/quiz.py

def quiz_financeiro():
    print("\n--- Quiz de Educação Financeira ---")

    perguntas = [
        {
            "pergunta": "1) O que é reserva de emergência?",
            "opcoes": [
                "A) Dinheiro guardado para qualquer investimento arriscado.",
                "B) Dinheiro guardado para imprevistos, como desemprego ou problemas de saúde.",
                "C) Um tipo de investimento em ações.",
                "D) Um empréstimo feito no banco."
            ],
            "correta": "B",
            "explicacao": "Reserva de emergência é um valor guardado para imprevistos, em aplicações seguras e com alta liquidez."
        },
        {
            "pergunta": "2) Qual das opções abaixo é um exemplo de renda fixa?",
            "opcoes": [
                "A) Ações de empresas listadas na bolsa.",
                "B) Fundos imobiliários (FIIs).",
                "C) CDB de um banco.",
                "D) Moedas digitais (criptomoedas)."
            ],
            "correta": "C",
            "explicacao": "CDB é um investimento de renda fixa emitido por bancos, normalmente atrelado ao CDI."
        },
        {
            "pergunta": "3) O que são juros compostos?",
            "opcoes": [
                "A) Juros calculados apenas sobre o valor inicial.",
                "B) Juros calculados sobre o valor inicial e sobre os juros acumulados.",
                "C) Juros que nunca mudam.",
                "D) Juros cobrados apenas em empréstimos."
            ],
            "correta": "B",
            "explicacao": "Juros compostos são o famoso 'juros sobre juros', gerando efeito bola de neve ao longo do tempo."
        },
        {
            "pergunta": "4) Qual é a prioridade antes de começar a investir em renda variável?",
            "opcoes": [
                "A) Pagar dívidas caras e montar uma reserva de emergência.",
                "B) Abrir conta em várias corretoras.",
                "C) Comprar o máximo de ações possível.",
                "D) Viver só com cartão de crédito."
            ],
            "correta": "A",
            "explicacao": "Antes de correr mais riscos, é importante estar com dívidas sob controle e ter reserva de emergência."
        }
    ]

    pontuacao = 0

    for item in perguntas:
        print("\n" + item["pergunta"])
        for opcao in item["opcoes"]:
            print(opcao)

        resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()

        if resposta == item["correta"]:
            print("✅ Correto!")
            pontuacao += 1
        else:
            print(f"❌ Incorreto. A resposta certa era: {item['correta']}.")
        print("💡", item["explicacao"])

    print(f"\nVocê acertou {pontuacao} de {len(perguntas)} perguntas.")
    if pontuacao == len(perguntas):
        print("Excelente! Seu conhecimento financeiro está em ótimo nível! 💰")
    elif pontuacao >= 2:
        print("Muito bom! Você já tem uma boa base, mas ainda pode evoluir mais. 😉")
    else:
        print("Tudo bem, o importante é aprender. Continue estudando com o AunascBot! 📚")

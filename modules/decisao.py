# modules/decisao.py

def assistente_decisao():
    print("\n--- Assistente de Decisão Financeira ---")

    print("\nVou te fazer algumas perguntas rápidas. Responda com 's' para sim ou 'n' para não.\n")

    tem_dividas = input("Você tem dívidas com juros altos (ex: cartão, cheque especial)? [s/n]: ").strip().lower()
    tem_reserva = input("Você já tem uma reserva de emergência (3 a 6 meses de despesas)? [s/n]: ").strip().lower()
    aceita_risco = input("Você se sente confortável com variações no valor dos investimentos (subir e descer)? [s/n]: ").strip().lower()
    prazo_longo = input("Seu objetivo é para longo prazo (acima de 5 anos)? [s/n]: ").strip().lower()

    print("\n📊 Analisando suas respostas...\n")

    # Regra 1: Dívidas caras vêm primeiro
    if tem_dividas == "s":
        print("🧯 Prioridade: pagar dívidas caras.")
        print("Enquanto você tiver dívidas com juros altos, normalmente faz mais sentido focar em quitá-las antes de investir pesado.")
        print("Depois de reduzir ou eliminar essas dívidas, você pode focar em montar sua reserva e investir com mais tranquilidade.")
        return

    # Regra 2: Sem reserva ainda
    if tem_reserva == "n":
        print("🛡️ Prioridade: montar uma reserva de emergência.")
        print("Antes de se expor a riscos maiores, é importante ter uma reserva de 3 a 6 meses das suas despesas em investimentos seguros e com alta liquidez, como Tesouro Selic ou CDB com liquidez diária.")
        return

    # Regra 3: Já tem reserva, pensa em risco
    if aceita_risco == "n":
        print("⚖️ Perfil mais conservador.")
        print("Você já tem reserva, mas não gosta de muita oscilação. Faz sentido focar em investimentos de renda fixa, como Tesouro Direto, CDBs e fundos conservadores.")
        return

    # Regra 4: Já tem reserva, aceita risco, prazo longo
    if aceita_risco == "s" and prazo_longo == "s":
        print("🚀 Perfil com foco em longo prazo.")
        print("Você já tem reserva, aceita oscilações e pensa no longo prazo. Isso abre espaço para investir parte do capital em renda variável, como ações, ETFs e FIIs, sempre de forma diversificada.")
        print("Ainda assim, é importante manter uma parte em renda fixa para equilibrar o risco.")
        return

    # Regra 5: Já tem reserva, aceita algum risco, mas prazo curto/médio
    print("📈 Perfil moderado.")
    print("Você já tem reserva e aceita algum risco, mas o prazo não é tão longo.")
    print("Uma combinação de renda fixa (CDBs, Tesouro) com uma pequena parte em renda variável pode fazer sentido, sempre respeitando seus objetivos e limites.")

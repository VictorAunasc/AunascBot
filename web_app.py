# web_app.py - Interface Web em formato de chatbot para o AunascBot

from flask import Flask, render_template_string, request
import json
import os
import threading
import webbrowser
import time

app = Flask(__name__)

# Armazena a conversa enquanto o servidor estiver rodando
conversa = []  # cada item: {"autor": "user"|"bot", "texto": "..."}


# ===================== LÓGICA DE NEGÓCIO =====================

def calcular_poupanca(valor_mensal: float, meses: int, rendimento_mensal: float):
    """Calcula total e juros de uma poupança com aportes mensais e juros compostos."""
    taxa = rendimento_mensal / 100
    total = 0.0
    for _ in range(meses):
        total = (total + valor_mensal) * (1 + taxa)
    juros = total - (valor_mensal * meses)
    return total, juros


def buscar_conceito(consulta: str):
    """Busca explicações na base_de_conhecimento.json com base na consulta."""
    caminho_arquivo = os.path.join("data", "base_conhecimento.json")
    if not os.path.exists(caminho_arquivo):
        return ["Base de conhecimento não encontrada."]

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            base = json.load(f)
    except json.JSONDecodeError:
        return ["Erro ao ler a base de conhecimento. Verifique o arquivo JSON."]

    consulta_lower = consulta.lower()
    respostas = []

    for item in base:
        termos = item.get("termos", [])
        resposta = item.get("resposta", "")
        for termo in termos:
            termo_lower = termo.lower()
            if termo_lower in consulta_lower or consulta_lower in termo_lower:
                respostas.append(resposta)
                break

    if not respostas:
        return [
            "Ainda não tenho uma resposta específica para isso.",
            "Tente usar outra palavra-chave como 'inflação', 'juros compostos' ou 'renda fixa'."
        ]

    return respostas


def resposta_inicial():
    return [
        "👋 Olá! Eu sou o AunascBot Web.",
        "Sou um chatbot de educação financeira.",
        "Digite /menu para ver o que eu sei fazer."
    ]


def montar_menu():
    return (
        "📋 Menu de opções:\n"
        "1️⃣ /economia      - Conceitos de economia\n"
        "2️⃣ /investimentos - Tipos de investimentos\n"
        "3️⃣ /simular v m t - Simular poupança (ex: /simular 500 12 0.8)\n"
        "4️⃣ /conceito x    - Pesquisar conceito financeiro (ex: /conceito inflação)\n"
        "5️⃣ /ajuda         - Ver dicas de uso do bot\n"
    )


def processar_mensagem_usuario(texto: str):
    """Recebe o texto digitado pelo usuário e devolve uma lista de respostas do bot."""
    texto_bruto = texto
    texto = texto.strip()
    if not texto:
        return ["Digite alguma coisa 🙂"]

    lower = texto.lower()

    # Comandos principais
    if lower in ("/menu", "menu"):
        return [montar_menu()]

    if lower in ("/ajuda", "ajuda"):
        return [
            "Você pode usar:",
            "• /menu → ver opções",
            "• /economia → ver conceitos básicos",
            "• /investimentos → tipos de investimentos",
            "• /simular 500 12 0.8 → R$500/mês, 12 meses, 0,8% ao mês",
            "• /conceito inflação → buscar explicação na base de conhecimento"
        ]

    if lower in ("/economia", "1", "opção 1"):
        return [
            "Alguns conceitos básicos de economia:\n"
            "• Inflação: aumento generalizado dos preços.\n"
            "• PIB: soma de todos os bens e serviços finais produzidos no país.\n"
            "• Juros: custo do dinheiro no tempo, podendo trabalhar a favor (investimentos) ou contra (dívidas)."
        ]

    if lower in ("/investimentos", "2", "opção 2"):
        return [
            "Tipos principais de investimentos:\n"
            "• Renda fixa: CDB, Tesouro Direto, LCI/LCA (mais previsíveis, menor risco).\n"
            "• Renda variável: ações, FIIs, ETFs (maior risco, maior potencial de retorno no longo prazo).\n"
            "• Reserva de emergência: geralmente em renda fixa com alta liquidez."
        ]

    # /simular 500 12 0.8
    if lower.startswith("/simular"):
        partes = texto.split()
        if len(partes) != 4:
            return [
                "Formato esperado: /simular valor_mensal meses rendimento_mensal",
                "Exemplo: /simular 500 12 0.8"
            ]
        try:
            valor = float(partes[1])
            meses = int(partes[2])
            taxa = float(partes[3])
            total, juros = calcular_poupanca(valor, meses, taxa)
            return [
                "Simulação de poupança:",
                f"Valor mensal: R${valor:.2f}",
                f"Meses: {meses}",
                f"Rendimento: {taxa}% ao mês",
                "",
                f"Total aproximado: R${total:,.2f}",
                f"Juros ganhos:     R${juros:,.2f} 💸"
            ]
        except ValueError:
            return ["Não consegui entender os números. Tente algo como: /simular 500 12 0.8"]

    # /conceito inflação
    if lower.startswith("/conceito"):
        partes = texto.split(maxsplit=1)
        if len(partes) == 1:
            return ["Você pode usar: /conceito inflação, /conceito renda fixa, /conceito pib, etc."]
        termo = partes[1]
        return buscar_conceito(termo)

    # Comando não reconhecido
    return [
        f"Não entendi o comando: {texto_bruto}",
        "Tente usar /menu para ver as opções disponíveis."
    ]


# ===================== INTERFACE HTML (CHAT) =====================

HTML_CHAT = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>AunascBot Web (Chat)</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #020617;
      color: #e5e7eb;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      height: 100vh;
    }
    header {
      background-color: #0f172a;
      padding: 12px 16px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }
    header h1 {
      margin: 0;
      font-size: 1.2rem;
    }
    header p {
      margin: 4px 0 0;
      font-size: 0.9rem;
      color: #9ca3af;
    }
    .chat-container {
      flex: 1;
      padding: 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .msg {
      max-width: 70%;
      padding: 8px 12px;
      border-radius: 12px;
      white-space: pre-wrap;
    }
    .user {
      align-self: flex-end;
      background-color: #1d4ed8;
    }
    .bot {
      align-self: flex-start;
      background-color: #111827;
      border: 1px solid #1f2937;
    }
    .input-area {
      display: flex;
      gap: 8px;
      padding: 12px 16px;
      background-color: #020617;
      border-top: 1px solid #1f2937;
    }
    .input-area input[type="text"] {
      flex: 1;
      padding: 8px;
      border-radius: 8px;
      border: 1px solid #374151;
      background-color: #020617;
      color: #e5e7eb;
    }
    .input-area button {
      padding: 8px 16px;
      border-radius: 8px;
      border: none;
      background-color: #22c55e;
      color: #022c22;
      font-weight: bold;
      cursor: pointer;
    }
    .input-area button:hover {
      background-color: #16a34a;
    }
    .hint {
      font-size: 0.8rem;
      color: #9ca3af;
      padding: 0 16px 8px;
    }
    code {
      background-color: #111827;
      padding: 2px 4px;
      border-radius: 4px;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <header>
    <h1>AunascBot 💰 – Chat Web Local</h1>
    <p>Use comandos como <code>/menu</code>, <code>/economia</code>, <code>/simular 500 12 0.8</code>, <code>/conceito inflação</code></p>
  </header>

  <div class="chat-container">
    {% for msg in conversa %}
      <div class="msg {{ msg.autor }}">
        {{ msg.texto }}
      </div>
    {% endfor %}
  </div>

  <form method="post" class="input-area">
    <input type="text" name="mensagem" placeholder="Digite uma mensagem ou comando..." autocomplete="off" autofocus>
    <button type="submit">Enviar</button>
  </form>
  <div class="hint">
    Comandos úteis: <code>/menu</code>, <code>/economia</code>, <code>/investimentos</code>, <code>/simular 500 12 0.8</code>, <code>/conceito inflação</code>, <code>/ajuda</code>.
  </div>
</body>
</html>
"""


# ===================== ROTAS FLASK =====================

@app.route("/", methods=["GET", "POST"])
def chat():
    global conversa

    # Primeira visita: manda mensagem inicial
    if not conversa:
        for texto in resposta_inicial():
            conversa.append({"autor": "bot", "texto": texto})

    if request.method == "POST":
        msg_usuario = request.form.get("mensagem", "").strip()
        if msg_usuario:
            conversa.append({"autor": "user", "texto": msg_usuario})
            respostas = processar_mensagem_usuario(msg_usuario)
            for resp in respostas:
                conversa.append({"autor": "bot", "texto": resp})

    return render_template_string(HTML_CHAT, conversa=conversa)


# ===================== INICIALIZAÇÃO =====================

def abrir_navegador():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000/")


if __name__ == "__main__":
    threading.Thread(target=abrir_navegador, daemon=True).start()
    app.run(host="127.0.0.1", port=5000, debug=False)

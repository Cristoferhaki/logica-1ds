perguntas = [
    ("Qual a capital da russia?", "moscou"),
    ("Quanto é 5 + 5?", "10"),
    ("Cor primária que começa com V?", "verde")
]

pontos = 0

for pergunta, resposta_correta in perguntas:
    resposta = input(pergunta + " ").lower()
    if resposta == resposta_correta:
        print("✅ Correto!")
        pontos += 1
    else:
        print("❌ Errado!")

print(f"Você fez {pontos} ponto(s) de {len(perguntas)}.")

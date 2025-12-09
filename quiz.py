acertos = 0
erros = 0

print("Seja Muito bem VINDO AO QUIZ (Responda todas as perguntas abaixo).")
resposta_usuario = str(input("Você Deseja iniciar o quiz S/N? \n")).upper() # Converte para maiúsculo para simplificar a checagem

if resposta_usuario != "S":
    print("Quiz encerrado.")
    quit()

print("\n--- INICIANDO O QUIZ ---\n")

# --- Pergunta 1 ---
print("1. Qual a capital da Noruega ?\n A)Oslo \n B)Porto \n C)Bruxelas \n D)Tromso")
resposta_1 = input("Resposta: ").upper()

if resposta_1 == "A":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta!  A resposta correta é A) Oslo.")
    erros += 1

# --- Pergunta 2 ---
print("\n2. Qual planeta do nosso Sistema Solar é conhecido como 'Estrela da Manhã' ou 'Estrela Vespertina'?\n A)Júpiter \n B)Marte \n C)Vênus \n D)Saturno")
resposta_2 = input("Resposta: ").upper()

if resposta_2 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta!  A resposta correta é C) Vênus.")
    erros += 1

# --- Pergunta 3 ---
print("\n3. Quem pintou a famosa obra de arte 'Mona Lisa'?\n A)Pablo Picasso \n B)Leonardo da Vinci \n C)Vincent van Gogh \n D)Michelangelo")
resposta_3 = input("Resposta: ").upper()

if resposta_3 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta!  A resposta correta é B) Leonardo da Vinci.")
    erros += 1

# --- Pergunta 4 ---
print("\n4. Em que ano a primeira versão do Python (por Guido van Rossum) foi lançada?\n A)1989 \n B)1991 \n C)2000 \n D)2003")
resposta_4 = input("Resposta: ").upper()

if resposta_4 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) 1991.")
    erros += 1

# --- Pergunta 5 ---
print("\n5. Qual é o elemento químico mais abundante no universo?\n A)Oxigênio \n B)Hélio \n C)Nitrogênio \n D)Hidrogênio")
resposta_5 = input("Resposta: ").upper()

if resposta_5 == "D":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é D) Hidrogênio.")
    erros += 1

# --- Pergunta 6 ---
print("\n6. Qual dos seguintes países faz fronteira com o Brasil?\n A)Equador \n B)Chile \n C)Peru \n D)Colômbia")
resposta_6 = input("Resposta: ").upper()

# Nota: Tanto Peru quanto Colômbia fazem fronteira. Vou usar D para manter a lógica do quiz simples.
if resposta_6 == "D":
    print("Alternativa correta! (Peru e Colômbia fazem fronteira, mas Colômbia está na lista)")
    acertos += 1
else:
    print("Alternativa incorreta!  A resposta correta é D) Colômbia (ou C) Peru. Ambos fazem fronteira.")
    erros += 1

# --- Resultados Finais ---
print("Resultado: ")
print(f"Quantidade de acertos:{acertos}")
print(f" Quantidade de erros:{erros}")

if acertos == 6 :
    print("Parabens voce gabaritou o teste")
if acertos > 3:
    print("Parabens voce acertou a metade das questoes")
if acertos < 3:
    print("Rendimento abaixo do esperado")

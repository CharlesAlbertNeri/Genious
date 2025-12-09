acertos = 0
erros = 0
total_perguntas = 30 # --- Utilizado posteriormente para obter a % de acertos e metrificação de desempenho --- #

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
    print("Alternativa incorreta! A resposta correta é A) Oslo.")
    erros += 1

# --- Pergunta 2 ---
print("\n2. Qual planeta do nosso Sistema Solar é conhecido como 'Estrela da Manhã' ou 'Estrela Vespertina'?\n A)Júpiter \n B)Marte \n C)Vênus \n D)Saturno")
resposta_2 = input("Resposta: ").upper()
if resposta_2 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Vênus.")
    erros += 1

# --- Pergunta 3 ---
print("\n3. Quem pintou a famosa obra de arte 'Mona Lisa'?\n A)Pablo Picasso \n B)Leonardo da Vinci \n C)Vincent van Gogh \n D)Michelangelo")
resposta_3 = input("Resposta: ").upper()
if resposta_3 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) Leonardo da Vinci.")
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
if resposta_6 == "D":
    print("Alternativa correta! (Peru e Colômbia fazem fronteira, mas Colômbia está na lista)")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é D) Colômbia (ou C) Peru. Ambos fazem fronteira.")
    erros += 1

# --- Pergunta 7 ---
print("\n7. Qual é o maior oceano do mundo em área e volume?\n A)Oceano Atlântico \n B)Oceano Índico \n C)Oceano Pacífico \n D)Oceano Antártico")
resposta_7 = input("Resposta: ").upper()
if resposta_7 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Oceano Pacífico.")
    erros += 1

# --- Pergunta 8 ---
print("\n8. Qual gás as plantas absorvem primariamente da atmosfera para realizar a fotossíntese?\n A)Oxigênio \n B)Nitrogênio \n C)Dióxido de Carbono \n D)Monóxido de Carbono")
resposta_8 = input("Resposta: ").upper()
if resposta_8 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Dióxido de Carbono.")
    erros += 1

# --- Pergunta 9 ---
print("\n9. Qual metal é líquido à temperatura ambiente?\n A)Cobre \n B)Ferro \n C)Mercúrio \n D)Alumínio")
resposta_9 = input("Resposta: ").upper()
if resposta_9 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Mercúrio.")
    erros += 1

# --- Pergunta 10 ---
print("\n10. Quantos lados tem um heptágono?\n A)5 \n B)6 \n C)7 \n D)8")
resposta_10 = input("Resposta: ").upper()
if resposta_10 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) 7.")
    erros += 1

# ---------------- NOVAS PERGUNTAS (11 a 30) ----------------

# --- Pergunta 11 ---
print("\n11. Quem escreveu a obra 'Dom Casmurro'?\n A)Machado de Assis \n B)José de Alencar \n C)Carlos Drummond de Andrade \n D)Monteiro Lobato")
resposta_11 = input("Resposta: ").upper()
if resposta_11 == "A":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é A) Machado de Assis.")
    erros += 1

# --- Pergunta 12 ---
print("\n12. Qual é a fórmula química da água?\n A)CO2 \n B)O2 \n C)H2O \n D)NaCl")
resposta_12 = input("Resposta: ").upper()
if resposta_12 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) H2O.")
    erros += 1

# --- Pergunta 13 ---
print("\n13. Qual país sediou a Copa do Mundo de Futebol em 2014?\n A)Alemanha \n B)Brasil \n C)Rússia \n D)África do Sul")
resposta_13 = input("Resposta: ").upper()
if resposta_13 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) Brasil.")
    erros += 1

# --- Pergunta 14 ---
print("\n14. O que significa a sigla 'URL' na internet?\n A)Universal Resource Locator \n B)Uniform Resource Link \n C)Unidade de Recurso Local \n D)User Reference Line")
resposta_14 = input("Resposta: ").upper()
if resposta_14 == "A":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é A) Universal Resource Locator.")
    erros += 1

# --- Pergunta 15 ---
print("\n15. Qual é o nome do menor osso do corpo humano?\n A)Fêmur \n B)Estribo \n C)Tíbia \n D)Rádio")
resposta_15 = input("Resposta: ").upper()
if resposta_15 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) Estribo.")
    erros += 1

# --- Pergunta 16 ---
print("\n16. Qual cidade é conhecida como 'A Cidade Eterna'?\n A)Paris \n B)Londres \n C)Roma \n D)Atenas")
resposta_16 = input("Resposta: ").upper()
if resposta_16 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Roma.")
    erros += 1

# --- Pergunta 17 ---
print("\n17. Qual é a unidade de medida padrão de resistência elétrica?\n A)Volt \n B)Ampère \n C)Ohm \n D)Watt")
resposta_17 = input("Resposta: ").upper()
if resposta_17 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Ohm.")
    erros += 1

# --- Pergunta 18 ---
print("\n18. Qual animal é o símbolo da sabedoria na cultura ocidental?\n A)Leão \n B)Cobra \n C)Coruja \n D)Elefante")
resposta_18 = input("Resposta: ").upper()
if resposta_18 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Coruja.")
    erros += 1

# --- Pergunta 19 ---
print("\n19. Em que ano ocorreu a Proclamação da República no Brasil?\n A)1822 \n B)1889 \n C)1891 \n D)1900")
resposta_19 = input("Resposta: ").upper()
if resposta_19 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) 1889.")
    erros += 1

# --- Pergunta 20 ---
print("\n20. Qual é a capital da Austrália?\n A)Sydney \n B)Melbourne \n C)Canberra \n D)Perth")
resposta_20 = input("Resposta: ").upper()
if resposta_20 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Canberra.")
    erros += 1

# --- Pergunta 21 ---
print("\n21. Quantos dias leva para a Terra dar uma volta completa em torno do Sol (aproximadamente)?\n A)24 \n B)30 \n C)365 \n D)366")
resposta_21 = input("Resposta: ").upper()
if resposta_21 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) 365.")
    erros += 1

# --- Pergunta 22 ---
print("\n22. Qual dos seguintes não é um tipo primitivo de dado em Java?\n A)int \n B)float \n C)string \n D)boolean")
resposta_22 = input("Resposta: ").upper()
if resposta_22 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) string (String é uma classe).")
    erros += 1

# --- Pergunta 23 ---
print("\n23. Qual instrumento musical é conhecido como 'o rei dos instrumentos'?\n A)Violino \n B)Piano \n C)Órgão \n D)Trompete")
resposta_23 = input("Resposta: ").upper()
if resposta_23 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Órgão.")
    erros += 1

# --- Pergunta 24 ---
print("\n24. Quantos fusos horários o Brasil possui (oficialmente)?\n A)2 \n B)3 \n C)4 \n D)5")
resposta_24 = input("Resposta: ").upper()
if resposta_24 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) 4.")
    erros += 1

# --- Pergunta 25 ---
print("\n25. Qual montanha é o ponto mais alto da África?\n A)Monte Atlas \n B)Monte Kilimanjaro \n C)Monte Everest \n D)Monte Branco")
resposta_25 = input("Resposta: ").upper()
if resposta_25 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) Monte Kilimanjaro.")
    erros += 1

# --- Pergunta 26 ---
print("\n26. Qual gás inerte é frequentemente usado em letreiros luminosos (neons)?\n A)Hélio \n B)Argônio \n C)Neônio \n D)Xenônio")
resposta_26 = input("Resposta: ").upper()
if resposta_26 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Neônio.")
    erros += 1

# --- Pergunta 27 ---
print("\n27. Qual o maior estado do Brasil em área territorial?\n A)São Paulo \n B)Minas Gerais \n C)Amazonas \n D)Pará")
resposta_27 = input("Resposta: ").upper()
if resposta_27 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Amazonas.")
    erros += 1

# --- Pergunta 28 ---
print("\n28. Qual o nome da estrutura que armazena informações genéticas em todas as células?\n A)Proteína \n B)Ribossomo \n C)Mitocôndria \n D)DNA")
resposta_28 = input("Resposta: ").upper()
if resposta_28 == "D":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é D) DNA (Ácido Desoxirribonucleico).")
    erros += 1

# --- Pergunta 29 ---
print("\n29. Quantos andares tem o Empire State Building em Nova York?\n A)88 \n B)102 \n C)110 \n D)120")
resposta_29 = input("Resposta: ").upper()
if resposta_29 == "B":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é B) 102.")
    erros += 1

# --- Pergunta 30 ---
print("\n30. Qual artista ficou conhecido por cortar a própria orelha?\n A)Paul Gauguin \n B)Claude Monet \n C)Vincent van Gogh \n D)Edgar Degas")
resposta_30 = input("Resposta: ").upper()
if resposta_30 == "C":
    print("Alternativa correta! ")
    acertos += 1
else:
    print("Alternativa incorreta! A resposta correta é C) Vincent van Gogh.")
    erros += 1

# --- Resultados Finais ---
print("\n------------------------------")
print("FIM DO QUIZ!")
print(f"Acertos: {acertos}")
print(f"Erros: {erros}")
print("------------------------------")

# Lógica de feedback final ajustada para 30 perguntas
if acertos == total_perguntas:
    print("Parabens voce gabaritou o teste")
elif acertos >= total_perguntas * 0.7: # 70% ou mais (21+ acertos)
    print("Parabens voce teve um excelente desempenho")
elif acertos >= total_perguntas / 2: # 50% a 70% (15 a 20 acertos)
    print("Parabens voce acertou a metade ou mais das questoes")
else: # Menos de 50% (14 ou menos acertos)
    print("Rendimento abaixo do esperado")
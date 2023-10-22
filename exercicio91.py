'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"'''

# Faça 5 perguntas
pergunta1 = input("Telefonou para a vítima? (sim/não): ").strip().lower()
pergunta2 = input("Esteve no local do crime? (sim/não): ").strip().lower()
pergunta3 = input("Mora perto da vítima? (sim/não): ").strip().lower()
pergunta4 = input("Devia para a vítima? (sim/não): ").strip().lower()
pergunta5 = input("Já trabalhou com a vítima? (sim/não): ").strip().lower()

# Conte as respostas positivas
respostas_positivas = 0

if pergunta1 == "sim":
    respostas_positivas += 1

if pergunta2 == "sim":
    respostas_positivas += 1

if pergunta3 == "sim":
    respostas_positivas += 1

if pergunta4 == "sim":
    respostas_positivas += 1

if pergunta5 == "sim":
    respostas_positivas += 1

# Emita uma classificação com base nas respostas
if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")

import random

numeros = []
i = 0
acertos = 0

# LEITURA NUMEROS USUARIO
while i < 6:
    numeroDigitado = int(input("Digite um numero entre 1-60: "))
    
    if numeroDigitado <= 0 or numeroDigitado > 60:
        print("Numero invalido, por favor digite um numero entre 1 e 60!")
    else:
        if numeroDigitado not in numeros:
            numeros.append(numeroDigitado)
            i += 1
        else:
            print("Numero ja digitado")

# SORTEIO
numerosSorteados = []
print("\n\n NUMEROS SORTEADOS: ")
i = 0
while i < 6:
    numeroSorteado = random.randint(1, 60)
    if numeroSorteado not in numerosSorteados:
        numerosSorteados.append(numeroSorteado)
        i += 1
        print(numeroSorteado, end=" ")

# VERIFICAR O TOTAL DE ACERTOS
for numero in numeros:
    if numero in numerosSorteados:
        acertos += 1

print("\nTOTAL DE ACERTOS:", acertos)

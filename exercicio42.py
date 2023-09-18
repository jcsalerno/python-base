#Faça um programa que faça o computador pensar em um número inteiro entre 0 e 5, tente descobrir qual foi o núemro escolhido pelo usuário. Escreve na tela se o usuário acertou ou não o número.

import random

numerosorteado = random.randint (0,5)

n1 = int(input('Digite um numero: '))
if n1 == numerosorteado:
    print(f'Parabéns, você acertou o número')
else:
    print(f'Você não acertou')
print(f'O número sorteado foi: {numerosorteado}')        

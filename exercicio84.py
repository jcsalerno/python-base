# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = int (input('Digite um número: '))

if n1 >= 0:
    print(f'O número digitado é positivo: {n1}')
elif n1 < 0:
    print(f'O número digitado é negativo: {n1}')
else:
    print('Digite um número válido')

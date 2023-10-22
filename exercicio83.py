# Faça um Programa que peça dois números e imprima o maior deles. 

n1 = int(input('Digite um número '))
n2 = int(input('Digite um segundo número '))

if n1 > n2:
    print(f'O primeiro número é o maior digitado {n1}')
elif n2 > n1:
    print(f'O segundo número é maior número digitado: {n2}')
elif n1 == n2:
    print(f'Os numéros digitados são iguais: {n1}')
else:
    print('Digite um número válido: ')        

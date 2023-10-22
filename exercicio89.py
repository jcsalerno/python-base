#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = float (input ('Digite o valor do produto: '))
n2 = float (input ('Digite o valor do segundo produto: '))
n3 = float (input ('Digite o terceiro valor do produto: '))

menor = min(n1, n2, n3)

print(f'O menor valor é o R$: {menor}')

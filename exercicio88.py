#Faça um Programa que leia três orçamentos e mostre o maior e o menor deles.

n1 = float (input('Digite seu orçamento: '))
n2 = float (input('Digite seu orçamento: '))
n3 = float (input('Digite seu orçamento: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f'O mair orçamento é o {maior} e o menor: {menor} ')


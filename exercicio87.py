#Faça um Programa que leia o orçamento de 3 empresas e mostre o maior deles.

n1 = float (input('Digite seu orçamento: '))
n2 = float (input('Digite seu orçamento: '))
n3 = float (input('Digite seu orçamaneto: '))

maior = max(n1, n2, n3)

print(f'O maior orçamento é o: {maior}')

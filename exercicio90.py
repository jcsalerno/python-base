#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int (input ('Digite o número: '))
n2 = int (input ('Digite o segundo número: '))
n3 = int (input ('Digite o terceiro número: '))

ordem = [n1, n2, n3]
desc = sorted(ordem, reverse=True)

print(f'Os números em ordem decrescente são: {desc}')

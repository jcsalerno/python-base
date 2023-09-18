#Faça um programa que leia três núemros e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número '))
n2 = int(input('Digite um número '))
n3 = int(input('Digite um número '))

#Verifica quem é o menor!
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3    

#Verifica quem é o maior:
maior = n1 
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor é: {menor}')    
print(f'O maior número é: {maior}')    

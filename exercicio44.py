#Faça um programa que leia um número e mostre na tela se é par ou impar.

n1 = int(input('Digite um número: '))
resto = n1 % 2 
if resto == 0:
    print(f'Seu número é par')
else:
    print(f'Numero impar')    
    
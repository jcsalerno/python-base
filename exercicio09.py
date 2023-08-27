#faça um programa que leia um número e mostre o seu dobro triplo e raiz quadrada.

import math
n1 = float((input)('Digite um número:'))
dobro = n1 * 2 
triplo = n1 * 3 
raiz = math.sqrt(n1)
print(f'O dobro do número digitado é: {dobro} \n o triplo é: {triplo} \n e a raiz quadrada é: {raiz:.2f}')
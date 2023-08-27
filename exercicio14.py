#faça um programa que leia um valor e der 5% de desconto
import math
n1 = float ((input)('Digite um valor para ter um desconto de 5%:'))
desconto = (n1 * 5) / 100 
valorfinal = n1 - desconto
print(f'O desconto foi de REAIS: {desconto}. O valor final é R$: {valorfinal}')
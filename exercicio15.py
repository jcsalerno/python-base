#faça um programa que mostre que um funciário teve 15% de aumento no seu salário.
import math
n1 = float((input)('Digite seu salário para o aumento em 15%:'))
aumento = n1 * 1.15
valor = aumento - n1
print(f'O seu aumento foi de R$: {valor:.2f}, seu salario final é: {aumento:.2f}')
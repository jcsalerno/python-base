#faça um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Exemplo: o usuário digitou 6.127, a parte inteira são 6
import math
num1 = float((input)('Digite um número real: '))
num1 = math.trunc(num1)
print(f'A parte inteira desse número é: {num1}')
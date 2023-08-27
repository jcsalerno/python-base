#faça um programa que calcule a área e depois use a tinta pra pintar e cada litro utiliza 2m²
import math 
base = float((input)('Digite a base da parede:'))
altura = float((input)('Digite a altura da parede:'))
area = (base * altura)
tinta = area / 2
print(f'A área da parede é: {area:.2f} m². Quantidade de tinta necessária são: {tinta} litros')


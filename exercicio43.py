#Escreva um programa que leia a velocidade de um carro. Se ele ultrapssar 80Km/h, mostre uma mensagem dizendo que ele foi mutado.
#A multa vai custar R$7,00 por cada Km acima do limite.

import math

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print(f'Multado')
    multa = (velocidade - 80) * 7
    print(f'Pague o valor da multa de: {multa} reais')
else:
    print(f'Siga, você não foi multado')
print(f'Tenha um bom dia, dirija com segurança')



   


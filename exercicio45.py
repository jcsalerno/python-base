#Faça um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando 0,50 centados por KM para viagens até 200Km e 0,45 para viagens mais longas.

import math

viagem = float(input('Digite a distância da sua viagem: '))

if viagem <= 200:
    print(f'Parabéns pela sua viagem:')
    calulador = viagem * 0.50
    print(f'Você tera que pegar R$ {calulador}')

else: 
    print(f'Parabéns pela viagem:')
    calulador2 = viagem * 0.45
    print(f'Você terá que pagar pela passagem R$ {calulador2}')
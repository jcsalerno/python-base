#Faça um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(f'''Sua opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      ''' )
jogador = int(input('Qual é a sua jogada? '))
print(f'JO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PO!!!')
print('-=' * 15)
print(f'O jogador jogou {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('-=' * 15)


if computador == 0: #computador jogou pedra
    if jogador == 0:
        print(f'EMPATE!')
    elif jogador == 1:
        print(f'JOGADOR VENCEU!')
    elif jogador == 2:
        print(f'COMPUTADOR VENCEU!')
    else:
        print(f'JOGADA INVÁLIDA! ')

elif computador == 1: #coputador jogou papel
    if jogador == 0:
        print(f'COMPUTADOR VENCEU')
    elif jogador == 1:
        print(f'EMPATE!')
    elif jogador == 2: 
        print(f'JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA! ')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2: 
        print(f'EMPATE!')
    else:
        print('JOGADA INVÁLIDA! ')

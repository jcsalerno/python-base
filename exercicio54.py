#Faça um programa que leia o ano nascimento de uma pessoa e informe: 1)se ele  vai alistar ao serviço militar 2)Se a hora de se alistar 3) se já passou o tempo de alistamento. Seu também deverá mostrar o tempo que falta ou que passou o prazo.

from datetime import date

atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano 


print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}')

if idade == 18:
    print(f'Você precisa se alistar ao serviço militar! ')
elif idade > 18:
    saldo = ano + 18
    print(f'Já passou o seu tempo de se alistar! ') 
    print(f'Você deveria se apresentar em: {saldo}')   
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda NÃO tem idade para servir faltam: {saldo} anos')
        
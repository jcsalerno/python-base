#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


salario = float(input('Quanto você ganha por hora? '))
horas = float(input('Números de horas trabalhadas no mês '))
total = salario * horas 
print(f'Seu salário no mês é R$: {total}')
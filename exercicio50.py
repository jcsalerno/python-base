#Faça um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode excerder 30% do salário ou então o empréstimo será negado. 

valorCasa = float(input('Digite o valor da casa: '))
seusalario = float(input('Digite o valor do seu salário:'))
anos = int(input('Quantos anos você pretende pagar? '))
prestacao = valorCasa / (anos * 12)
minimo = seusalario * 30 / 100

print(f'Para pagar uma casa de {valorCasa:.2f} em {anos} a prestação será de R$ {prestacao:.2f}')

if prestacao <= minimo:
    print(f'Empréstimo pode ser concedido! ')
else:
    print(f'Empréstimo NEGADO! ')    
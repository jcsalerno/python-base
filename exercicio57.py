#Faça um programa: que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Você está abaixo do peso. Seu IMC é: {imc:.1f}')
elif imc <= 25:
    print(f'Você está com o peso ideal. Seu IMC é: {imc:.1f}')
elif imc <= 30:
    print(f'Você está com sobrepeso. Seu IMC é: {imc:.1f}')
elif imc <= 40:
    print(f'Você está obeso. Seu IMC é: {imc:.1f}')
else:
    print(f'Obesida mórbida. Seu IMC é {imc:.1f}')            



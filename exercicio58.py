#Faça um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

compra = float(input('Qual é o valor da sua compra? '))
print(f'''Escolha umas das opções abaixo:
       [1] à vista dinheiro/cheque: 10% de desconto
       [2] à vista no cartão: 5% de desconto
       [3] em até 2x no cartão: preço formal
       [4] 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Sua opção? '))

avista = (compra / 10) 
cartao = (compra / 5)
credito = compra + (compra * 20 / 100)

if opcao == 1:
    print(f'Sua compra foi no valor de {compra:.1f}. Você teve um desconto de 10%. Valor total a ser pago é R$ {compra - avista:.1f}')
elif opcao == 2:
    print(f'Sua compra foi no valor de {compra:.1f}. Você teve um desconto de 5%. Valor total a ser pago é R$ {compra - cartao:.1f}')
elif opcao == 4:
    print(f'Sua compra foi no valor de {compra:.1f}. Você pagou 20% de juros! Valor total a ser pago é R$ {credito:.1f}')
else:
    print(f'Sua compra não teve desconto. Total R$ {compra:.1f} ')


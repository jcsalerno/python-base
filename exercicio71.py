#Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
#Obs: faça tudo usando variáveis.
#Valores do último ano:

#Quantidade de Vendas de Coca = 1500
#Quantidade de Vendas de Pepsi = 1300
#Preço Unitário da Coca = 1,50 
#Preço Unitário da Pepsi = 1,50
#Custo da Loja: 2.500,00
#Use o bloco abaixo para criar todas as variáveis que precisar.

quant_coca = 1500
quant_pepsi = 1300
preco_refri = 1.50 
custo_loja = 2500 

faturament_pepsi = quant_pepsi * preco_refri

faturament_coca = quant_coca * preco_refri 

faturamento = faturament_coca + faturament_pepsi 
lucro = faturamento - custo_loja

margem = lucro / faturamento


#1. Qual foi o faturamento de Pepsi da Loja?
print(f'O faturamento da loja em Pepsi foi R$ {faturament_pepsi:.2f}')



#2. Qual foi o faturamento de Coca da Loja?
print(f'O faturamento da loja em Coca foi R$ {faturament_coca:.2f}')



#3. Qual foi o Lucro da loja?
print(f'O lucro da loja foi R$: {lucro:.2f}')



#4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual
print(f'A margem da loja foi R$: {margem:.2f}')



### Parte 2 - Inputs e Strings

#A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
#Ex: 
#Coca -> Código: BEB1300543<br>
#Pepsi -> Código: BEB1300545<br>
#Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
#Vodka Smirnoff -> Código: BAC17675002<br>

#Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

#Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

#Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.

cod = (input('Qual é seu código da bebida? '))
cod = cod.upper()
print ('BAC' in cod)



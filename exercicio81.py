# Comparações Contraintuitivas

#Existem algumas comparações no Python que não são tão intuitivas quando vemos pela primeira vez, mas que são muito usadas, principalmente por programadores mais experientes.

#É bom sabermos alguns exemplos e buscar sempre entender o que aquela comparação está buscando verificar.

### Exemplo 1:

#Digamos que você está construindo um sistema de controle de vendas e precisa de algumas informações para fazer o cálculo do resultado da loja no fim de um mês.

faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de {} reais".format(lucro))
else:
    print('Preencha o faturamento e o lucro corretamente')

## Resumo

#Algumas comparações contraintuitivas muito usadas:

#If 0:

#If '': 

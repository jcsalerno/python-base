#Operadores Compostos
a, b = 1, 2
print ('Antes da troca')
print(f'O valor das variáveis: a = {a}, b = {b}')
#primeira troca
aux = a
a = b 
b = aux
print('Primeira troca')
print(f'O valor das variáveis depois da troca são: a = {a}, b = {b}')
#segunda troca
a, b = b, a
print('Segunda troca')
print(f'O valor das variáveis depois da troca são: a = {a}, b = {b}')
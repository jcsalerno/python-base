#Faça que leia dois números inteiros e compare-os mostrando na tela uma mensagem::
#O primeiro valor é maior o segundo valor é maior, não existe valor, os dois são iguais.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O primeiro valor é MAIOR')
elif n2 > n1:
    print(f'O segundo valor é MAIOR')
else:
    print(f'Os dois valores são IGUAIS!') 
       
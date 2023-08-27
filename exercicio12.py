#faça um programa que calcule a tabuada de um numero
n = int(input('n = '))
i = 0
while i <= 10:
    print('%2d x %2d = %2d' % (n, i, (n*i)))
    
    i = i + 1
sair = input('\nTecle ENTER para sair...')
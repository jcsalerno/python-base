#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0 
cont = 0
for c in range(1, 501, 2):
    #print(c, end= ' ')
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(f'A soma de todos os {cont} valores solicitados é: {s}')    
    
#Faça um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

s = 0
for c in range(1,7):
    c = int(input('Digite seis números: '))
    if c % 2 == 0:
        c += s
        print(f'A soma dos números digitados são: {s}')
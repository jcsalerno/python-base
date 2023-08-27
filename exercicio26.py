#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
nome = input('Digite o nome da sua cidade: ')

if nome.upper().split()[0] == 'SANTO':
    print('O nome da cidade começa com "SANTO".')
else:
    print('O nome da cidade não começa com "SANTO".')

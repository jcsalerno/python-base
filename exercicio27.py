#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome: ')

# Converte o nome para letras minúsculas para facilitar a comparação
nome_minusculo = nome.lower()

# Verifica se "silva" está presente no nome
if 'silva' in nome_minusculo:
    print('O nome contém "SILVA".')
else:
    print('O nome não contém "SILVA".')

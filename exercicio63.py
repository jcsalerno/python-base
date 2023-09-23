#Faça tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver sua tabuada '))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
sair = input('\nTecle ENTER para sair...')

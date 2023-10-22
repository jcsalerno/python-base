# 3. Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil, exemplo:
#Usuário digita: C
#Seu programa deve responder:
# C - Casado

categorias = "Categorias:\nCasado\nSolteiro\nDivorcidado\nViúvo\nOutros"
print(categorias)
estado = str(input('Digite a letra inicial do seu estado civil: '))
estado = estado.upper()

if estado == 'C':
    print(f'Seu estado civil é casado: C')
elif estado == 'S':
    print(f'Seu estado civil é solteiro: S')
elif estado == 'D':
    print('Seu estado civil é divorcidado: D ')
elif estado == 'V':
    print('Seu estado é civil viúvo: V')
elif estado == 'O':
    print('Estado civil outro: O ')
else:
    print('Escolha um estado civil válido ')    

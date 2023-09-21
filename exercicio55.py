#Façaum programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Digite a segunda nota? '))

media = (n1 + n2) / 2

if media > 7:
    print(f'Você foi aprovado! PARABÉNS! sua média foi {media:.1f}')
elif media < 5:
    print(f'Infelizmente, você foi reprovado! sua média foi {media:.1f}')
else:
    print(f'Você está de recuperação! Ainda existe uma chance! ESTUDE! sua média foi {media:.1f}')
       
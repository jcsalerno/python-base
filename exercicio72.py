# 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

#Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 


tamanho = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade da conexão em Mbps: '))

# aqui trasnformamos megabytes em megabits para que tamanho e velocidade estejam na mesma unidade
tamanho_megabits = tamanho * 8

tempo = tamanho_megabits / velocidade
# transformando em minutos
tempo_minutos = tempo / 60
print(f'O tempo de download é de {tempo_minutos} minutos')

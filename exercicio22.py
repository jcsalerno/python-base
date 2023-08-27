#faça um programa parar sortear os alunos em uma apresentação 4 alunos e mostrar a ordem sorteada.
import random
alunos = ["Aluno1", "Aluno2", "Aluno3", "Aluno4"]
ordem_sorteada = random.sample(alunos, len(alunos))
print("Ordem de apresentação dos alunos:")
for idx, aluno in enumerate(ordem_sorteada, start=1):
    print(f"{idx}. {aluno}")

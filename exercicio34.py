#!/usr/bin/env python3
"""Exibe relatório de crianças por atividades.
Imprimir a lista de crianças agrupadas por sala que frequentam cada umas das
atividades
"""
__version__ = '0.1.1'

sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['João', 'Antonio', 'Carlos', 'Maria', 'Isolada']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Carlos', 'Maria', 'Isolada']
aula_danca  = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
    ]

#Listar alunos em cada atividade por sala                            
for nome_atividade, atividade in atividades: 
    print(f'Alunos da atividade {nome_atividade}\n')

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)     
     
    print(f'sala1', atividade_sala1)
    print(f'sala2', atividade_sala2)
    print()
    print("#" * 35)

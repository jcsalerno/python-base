#!/usr/bin/env python3
"""Bloco de notas

$ exercicio38.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ exercicio38.py read tech
...
...
"""
__version__ = "0.1.0"

import os
import sys 


cmds = ('read', 'new')
path = os.curdir
filepath = os.path.join(path, 'notes.txt')


arguments = sys.argv[1:]
if not arguments:
    print('Invalid usage')
    print(f'You must specify subcommand {cmds}')
    sys.exit(1)

if arguments[0] not in cmds:
    print(f'Invalid command {arguments[0]}')

if arguments[0] == 'read':
    #leitura das notas 
    for line in open(filepath):
        title, tag, text = line.split('\t')
        if tag.lower() == arguments[1].lower():
            print(f'title: {title}')
            print(f'text: {text}')
            print('-' * 30)
            print()

if arguments[0] == 'new':
    title = arguments [1]
    text = [
        f'{title}\n',
        input('tag:').strip(),
        input('text: \n').strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write('\t'.join(text) + '\n')
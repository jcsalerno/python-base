"""Hello World. Multi languages.
Depending on the language configured in the environment, the program displays 
the corresponding message.
Usage: Have the variable LANG properly configured. ex:
    export LANG=pt_BR
Execution:
    python3 exercicio32.py
    or
     ./exercicio32.py    
"""
__version__ = "0.0.1"
__author__ = "Julio Cesar"
__license__ = "Unlicense"

import os

current_language = os.getenv('LANG', 'en_US')[:5]

if current_language == 'pt_Br':
    msg = 'Olá, Mundo!'
elif current_language =='it_IT':
    msg = 'Ciao, Mondo!'

msg = 'Hello, World!'
print(msg)



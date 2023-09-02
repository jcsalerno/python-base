#!/usr/bin/env python
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
__version__ = "0.1.2"
__author__ = "Julio Cesar"
__license__ = "Unlicense"

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = {
    'en_US': 'Hello, World!',
    'pt_BR': 'Olá, Mundo!',
    'it_IT': 'Ciao, Mondo!',
    'es_SP': 'Hola, Mundo!',
    'fr_FR': 'Bonjour, Monde!',
}

print(msg[current_language])



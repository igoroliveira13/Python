'''
1 - Usuario escolhe um tema e código sorteia uma palavra para o jogo

2 - Conforme usuario da palpites código verifica se há a letra na palavra


'''

import os
from random import randint
import time

os.system('cls')

chances = 6

animais = ['Cachorro', 'Gato', 'Peixe', 'Cavalo', 'Leão']

while True:
    
    nome_jogo = 'JOGO DA FORCA'
    print('=-' * 20)
    print(nome_jogo.center(40, ' '))
    print('=-' * 20)
        
    print('\n'
        '0 - Sair'
        '1 - Animais\n'
        '2 - Profissões\n')
    if chances == 0:
        print('+---+\n'
            '|   |\n'
            '|   O\n'
            '|  /|\ \n'
            '|  / \ \n'
            '-+-----')
    elif chances == 1:
        print('+---+\n'
            '|   |\n'
            '|   O\n'
            '|  /|\ \n'
            '|  /  \n'
            '-+-----')
    elif chances == 2:
        print('+---+\n'
            '|   |\n'
            '|   O\n'
            '|  /|\ \n'
            '|    \n'
            '-+-----')
    elif chances == 3:
        print('+---+\n'
            '|   |\n'
            '|   O\n'
            '|  /| \n'
            '|   \n'
            '-+-----')
    elif chances == 4:
        print('+---+\n'
            '|   |\n'
            '|   O\n'
            '|   | \n'
            '|   \n'
            '-+-----')
    elif chances == 5:
        print('+---+\n'
            '|   |\n'
            '|   O\n'
            '|    \n'
            '|   \n'
            '-+-----')
    elif chances == 6:
                print('+---+\n'
            '|   |\n'
            '|   \n'
            '|    \n'
            '|   \n'
            '-+-----')
    
    chances -= 1

    time.sleep(2)

    os.system('cls')

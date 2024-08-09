# Aula 12
# Desafio 045
# Crie um programa que faça o computador jojar Jokenpô com você.

from random import randint
from time import sleep
import emoji

estilo = {'clear':        '\033[m',
          'bold':      '\033[1m',
          'blue':         '\033[34m',
          'blueBold':     '\033[1;34m',
          'cyan':         '\033[36m',
          'cyanBold':     '\033[1;36m',
          'green':        '\033[32m',
          'greenBold':    '\033[1;32m',
          'grey':        '\033[37m',
          'greyBold':    '\033[1;37m',
          'purple':     '\033[35m',
          'purpleBold': '\033[1;35m',
          'red':     '\033[31m',
          'redBold': '\033[1;31m',
          'yellow':      '\033[33m',
          'yellowBold':  '\033[1;33m',
          'blackWhite': '\033[7;30m'}
asteriscos = 60

print(f'*' * asteriscos)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #Gera um range de 0 a 2

print(emoji.emojize('''
===== Opções ======
===================
= \033[7m   \033[1mJokenpô     \033[m =
=  [0] Pedra :raised_fist:    =
=  [1] Papel :hand_with_fingers_splayed:   =
=  [2] Tesoura :crossed_fingers:  =
===================
''', language = 'alias'))

print(f'*' * asteriscos)

jogador = int(input(f'{estilo["bold"]}Qual é a sua jogada?{estilo["clear"]} '))

print(f'*' * asteriscos)

if jogador > 2:
    print(f'\033[7;31mJogada inválida!{estilo["clear"]}')

else:
    print(f'{estilo["purpleBold"]}JO')
    sleep(0.8)
    print(f'KEN')
    sleep(0.8)
    print(f'PO!!{estilo["clear"]}')
    
    print(f'*' * asteriscos)

    if computador == jogador:
        print(emoji.emojize(f'{estilo["blueBold"]}EMPATE!{estilo["clear"]} :white_flag:', language = 'alias'))

    else:
        print(f'Computador jogou {itens[computador]}')
        print(f'Jogador jogou {itens[jogador]}')

        if computador == 0: # PEDRA
            if jogador == 1: # PAPEL
                print(emoji.emojize(f'{estilo["greenBold"]}Jogador VENCEU!{estilo["clear"]} :hand_with_fingers_splayed:', language = 'alias'))
            elif jogador == 2: # TESOURA
                print(emoji.emojize(f'{estilo["redBold"]}Computador VENCEU!{estilo["clear"]} :raised_fist:', language = 'alias'))

        elif computador == 1: # PAPEL
            if jogador == 0: # PEDRA
                print(emoji.emojize(f'{estilo["redBold"]}Computador VENCEU!{estilo["clear"]} :raised_fist:', language = 'alias'))
            elif jogador == 2: # TESOURA
                print(emoji.emojize(f'{estilo["greenBold"]}Jogador VENCEU!{estilo["clear"]} :hand_with_fingers_splayed:', language = 'alias'))

        elif computador == 2: # TESOURA
            if jogador == 0: # PEDRA
                print(emoji.emojize(f'{estilo["greenBold"]}Jogador VENCEU!{estilo["clear"]} :raised_fist:', language = 'alias'))
            elif jogador == 1:  # PAPEL
                print(emoji.emojize(f'{estilo["redBold"]}Computador VENCEU!{estilo["clear"]} :crossed_fingers:', language = 'alias'))

print(f'*' * asteriscos)
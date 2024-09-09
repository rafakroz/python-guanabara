# Aula 16
# Desafio 074
# Exercício 16.3
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
# que estão na tupla.

from random import randint

cor = {'clear':      '\033[m',
       'bold':       '\033[1m',
       'blue':       '\033[34m',
       'blueBold':   '\033[1;34m',
       'cyan':       '\033[36m',
       'cyanBold':   '\033[1;36m',
       'green':      '\033[32m',
       'greenBold':  '\033[1;32m',
       'grey':       '\033[37m',
       'greyBold':   '\033[1;37m',
       'purple':     '\033[35m',
       'purpleBold': '\033[1;35m',
       'red':        '\033[31m',
       'redBold':    '\033[1;31m',
       'yellow':     '\033[33m',
       'yellowBold': '\033[1;33m',
       'blackWhite': '\033[7;30m'}

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

lista = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print('Os valores sorteados foram: ', end='')

for n in lista:
       print(f'{n} ', end='')

print(f'\nForam sorteados {len(lista)} números.')
print(f'O menor número da lista é {min(lista)}, na {lista.index(min(lista))+1}° posição.')
print(f'O maior número da lista é {max(lista)}, na {lista.index(max(lista))+1}° posição.')
print(f'Lista ordenada: {sorted(lista)}')

print(f'*' * asteriscos) # --------------------------------------

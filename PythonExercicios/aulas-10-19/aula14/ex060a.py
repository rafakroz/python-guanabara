# Aula 14
# Desafio 060
# Exercício 14.4
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep

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

num = int(input('Fatorial de: '))

resultado = 1
count = 1

print(f'*' * asteriscos) # --------------------------------------

while count <= num:
    resultado = resultado * count
    print(f'{num} x {count} = {resultado}')
    count += 1 
    sleep(1)

print(resultado)

print(f'*' * asteriscos) # --------------------------------------
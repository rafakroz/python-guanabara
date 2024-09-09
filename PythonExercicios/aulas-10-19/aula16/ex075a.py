# Aula 16
# Desafio 075
# Exercício 16.4
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:
# A - Quantas vezes apareceu o valor 9.
# B - Em que posição foi digitado o primeiro valor 3.
# C - Quais foram os números pares.

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

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
num4 = int(input('Quarto número: '))
lista = (num1, num2, num3, num4)

print(f'*' * asteriscos) # --------------------------------------

print('Foram inseridos os números: ', end='')
for n in lista:
       print(f'{n} ', end='')

numBuscaA = 9
if lista.count(numBuscaA) > 0:
       print(f'\nO número {numBuscaA} apareceu {lista.count(numBuscaA)} vezes na lista.')
else:
       print(f'\nO número {numBuscaA} não foi inserido.')

numBuscaB = 3
if lista.count(numBuscaB) > 0:
       print(f'O número {numBuscaB} está na posição {lista.index(numBuscaB)}.')
else:
       print(f'O número {numBuscaB} não foi inserido.')

print(f'Os números pares inseridos foram: ', end='')
for n in lista:
       if n % 2 == 0:
              print(f'{n} ', end='')

print(f'\nOs números ímpares inseridos foram: ', end='')
for n in lista:
       if n % 2 == 1:
              print(f'{n} ', end='')

print('\n')

print(f'*' * asteriscos) # --------------------------------------

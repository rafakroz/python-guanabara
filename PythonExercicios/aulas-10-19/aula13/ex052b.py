# Aula 13
# Desafio 052
# Exercício 13.7
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    
    print(f'{i}', end=' ')

print('\033[m')

if total == 2:
    print(f'O número {num} foi divisível apenas {total} vezes.')
    print('E por isso ele \033[33mé PRIMO\033[3m!')
else:
    print(f'O número {num} foi divisível {total} vezes.')
    print('E por isso ele \033[31mnão é PRIMO\033[m!')
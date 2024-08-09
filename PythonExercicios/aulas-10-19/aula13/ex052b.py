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
print(f'O número {num} foi divisível {total} vezes.')

if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')

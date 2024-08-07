# Aula 10
# Desafio 030
# Crie um programa que leia um núemro inteiro e mostre na tela se é PAR ou ÍMPAR.

print('*' * 30)

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')
    
print('*' * 30)
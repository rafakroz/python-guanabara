# Aula 10
# Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice

print('Tente acertar em que número pensei entre 0 e 5!')

print('*' * 30)

meuNum = int(input('Digite seu número: '))

lista = [0, 1, 2, 3, 4, 5]

escolhido = choice(lista)

print('*' * 30)

if meuNum == escolhido:
    print(f'Você escolheu {meuNum} e acertou!')
else:
    print(f'Você escolheu {meuNum} e errou! O número correto é {escolhido}.')

print('Tente novamente!')
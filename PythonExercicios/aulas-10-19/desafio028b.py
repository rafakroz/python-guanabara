# Aula 10
# Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('Tente acertar em que número pensei entre 0 e 5!')

print('*' * 30)

numPc = randint(0, 5)

meuNum = int(input('Digite seu número: '))

print('*' * 30)

print('Processando.')
sleep(0.5)
print('Processando..')
sleep(0.5)
print('Processando...')
sleep(0.5)

print('Só mais um pouco.')
sleep(0.5)
print('Só mais um pouco..')
sleep(0.5)
print('Só mais um pouco...')
sleep(0.5)

if meuNum == numPc:
    print(f'Você acertou!')
else:
    print(f'Você escolheu {meuNum} e errou! O número correto é {numPc}.')

print('Tente novamente!')
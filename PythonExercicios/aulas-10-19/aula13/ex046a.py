# Aula 13
# Desafio 046
# Exercício 13.1
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

asteriscos = 60

print(f'*' * asteriscos)

for i in range(10, 0, -1):
    print(f'Contagem: {i}')
    sleep(1)
print(emoji.emojize(':fireworks: :fireworks: :fireworks:', language = 'alias'))
sleep(1)

print(f'*' * asteriscos)
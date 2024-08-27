# Aula 14
# Desafio 061
# Exercício 14.5
# Refaça o Desafio 051 - Aula 13, lendo o primeiro termo e a razão de uma Progressão Aritmétrica,
# mostrando os 10 primeiros termos da progressão usando a estrutura While.

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

inicio = int(input('Primeiro número: '))
razao = int(input('Razão: '))

termo = inicio
qtd = 10
cont = 1

print(f'*' * asteriscos)

while cont <= 10:
    print(f'{termo}', end = ' - ')
    termo += razao
    cont += 1

print('FIM')

print(f'*' * asteriscos) # --------------------------------------

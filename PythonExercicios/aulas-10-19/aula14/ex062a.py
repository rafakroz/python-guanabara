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
cont = 1
total = 0
mais = 10

print(f'*' * asteriscos)

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end = ' - ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input(f'Quantos termos você quer mostrar a mais? '))
    print('FIM')

 # Aula 13
# Desafio 051
# Exercício 13.6
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmétrica.
# No final, mostre os 10 primeiros termos dessa progressão.

asteriscos = 60

print(f'*' * asteriscos)

inicio = int(input('Primeiro número: '))
razao = int(input('Razão: '))

decimo = inicio + (10 - 1) * razao

print(f'*' * asteriscos)

for i in range(inicio, decimo + razao, razao):
    print(f'{inicio}', end = ' - ')
    inicio += razao

print('FIM')
print(f'*' * asteriscos)
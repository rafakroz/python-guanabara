# Aula 13
# Desafio 047
# Exercício 13.2
# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.

asteriscos = 60

print(f'*' * asteriscos)

# opção 1

for i in range(1, 51):
    if i % 2 == 0:
        print(f'{i}', end = ' ')
print('...')

# opção 2

for i in range(2, 51, 2):
    print(f'{i}', end = ' ')
print('...')
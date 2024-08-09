# Aula 13
# Desafio 050
# Exercício 13.5
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

asteriscos = 60

print(f'*' * asteriscos)

soma = 0
total = 0
pares = 0

for i in range(1, 7):
    num = int(input(f'{i}) Digite um valor: '))
    total += num
    if num % 2 == 0:
        soma += num
        pares += 1

print(f'*' * asteriscos)

if pares == i:
    print(f'Todos os núemros inseridos são pares!')
    print(f'O somatório total dos {i} números é {total}.')
else:
    print(f'O somatório total dos {i} números é {total}.')
    
    if pares == 0:
        print(f'E nenhum número par foi inserido!')
    elif pares == 1:
        print(f'O do único número par é {soma}.')
    else:
        print(f'O somatório apenas dos {pares} números pares é {soma}.')

print(f'*' * asteriscos)
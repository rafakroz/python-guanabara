# Aula 13
# Desafio 048
# Exercício 13.3
# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1

print(f'O somatório dos {contador} números é {soma}.')

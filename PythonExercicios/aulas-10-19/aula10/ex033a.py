# Aula 10
# Desafio 033
# Faça um programa que leia 3 (3, 7, 5) números e mostre qual é o maior e qual é o menor.

print('*' * 30)

n1 = int(input('Primero número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = 2
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print('*' * 30)

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')

print('*' * 30)
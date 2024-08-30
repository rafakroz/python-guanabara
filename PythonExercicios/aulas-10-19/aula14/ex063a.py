# Aula 14
# Desafio 063
# Exercício 14.7
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma Sequência de Fibonacci.
# Exemplo:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------
print(f'Sequência de Fibonacci')

qtdTermos = int(input(f'Quantos termos você quer exibir? '))

t1 = 0  #t1 iniciado com 0
t2 = 1  #t2 iniciado com 1

print(f'{t1} -> {t2}', end='')

cont = 3  #inicia em 3, pois os 2 primeiros termos foram atribuídos

while cont <= qtdTermos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(f' -> FIM')

'''
cont 1 / cont 2
t1 = 0
t2 = 1
t3 = 0 + 1 = 1

cont 3
t1 = 1
t2 = 1
t3 = 1 + 1 = 2

cont 4
t1 = 1
t2 = 2
t3 = 1 + 2 = 3

cont 5
t1 = 2
t2 = 3
t3 = 2 + 3 = 5

cont 6
t1 = 3
t2 = 5
t3 = 3 + 5 = 8

cont 7
t1 = 5
t2 = 8
t3 = 5 + 8 = 13

cont 8
t1 = 8
t2 = 13
t3 = 8 + 13 = 21

cont 9
t1 = 13
t2 = 21
t3 = 13 + 21 = 34

'''
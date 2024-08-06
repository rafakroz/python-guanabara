n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
divisao = n1 / n2
restoDiv = n1 % n2
divisaoInteira = n1 // n2
potencia = n1 ** n2 # n1 elevado ao n2

print(f'O resultado da soma de {n1} e {n2} é: {soma}')
print(f'O resultado da subtração de {n1} e {n2} é: {sub}')
print(f'O resultado da multiplicação de {n1} e {n2} é: {mult}')
print(f'O resultado da divisão de {n1} e {n2} é: {divisao}')
print(f'O resultado do resto da divisão de {n1} e {n2} é: {restoDiv}')
print(f'O resultado da divisão inteira de {n1} e {n2} é: {divisaoInteira}')
print(f'O resultado da potência de {n1} e {n2} é: {potencia}')

"""
Ordem de precedência:
1: ()
2: **
3: * / // %
4: + -
"""

# Exemplos do vídeo

print('----------------------------------')

op1 = 5 + 3 * 2
print(f'O resultado da operação 1 é: {op1}')

op2 = 3 * 5 + 4 ** 2
print(f'O resultado da operação 2 é: {op2}')

op3 = 3 * (5 + 4) ** 2
print(f'O resultado da operação 3 é: {op3}')

print('----------------------------------')

n3 = 10
n4 = 5

print('Teste: {}'.format(n3 + n4))

print('----------------------------------')

#Formatando a string
nome = input('Digite seu nome: ')
print(f'Prazer em te conhecer {nome:>20}')

print('----------------------------------')

print('Texto do print 1', end=' ')
print('Texto do print 2.')
print('Texto com \nalgumas quebras de \nlinha.')
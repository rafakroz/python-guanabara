# Programa para sortear a ordem de apresentação de trabalho dos alunos.
# Leia o nome dos quatro e mostre a ordem sorteada

import random

n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceito aluno: '))
n4 = str(input('Nome do quarto aluno: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(f'A ordem de apresentação é: \n{lista}.')
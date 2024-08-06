# Desenvolva  um programa que leia as duas notas de um aluno,
# calcule e mostre a su média

nome = input('Nome do aluno: ')
nota1 = int(input('Informe a nota 1: '))
nota2 = int(input('Informe a nota 2: '))

media = (nota1 + nota2) / 2

print(f'{nome} tirou {nota1} na primeira prova, \n{nota2} na segunda prova, \ne ficou com média {media}.')

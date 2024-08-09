# Desenvolva  um programa que leia as duas notas de um aluno,
# calcule e mostre a su média

nome = input('Nome do aluno: ')
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))

media = (nota1 + nota2) / 2

print(f'{nome} tirou {nota1:.1f} na primeira prova, \n{nota2:.1f} na segunda prova, \ne ficou com média {media:.1f}.')

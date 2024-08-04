# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário , com 15% de aumento.

nome = input('Informe o nome do funcionário: ')
salario = int(input(f'Informe o salário base de {nome}: R$'))

salarioReajustado = salario + (salario * 0.15)

print(f'O salário de {nome} é de R${salario}. \nSerá reajustado em 15%, passando para R${salarioReajustado}.')
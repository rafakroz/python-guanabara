# Aula 10
# Desafio 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

print('*' * 30)

nome = str(input('Informe o nome do funcionário: ')).strip()
salario = float(input('Informe o salário atual: R$'))

if salario > 1250:
    salarioReajustado = salario + (salario * 0.10)
    percentual = '10%'
else:
    salarioReajustado = salario + (salario * 0.15)
    percentual = '15%'

print('*' * 30)

print(f'{nome} terá direito ao aumento de {percentual}.')
print(f'O salário atual de R${salario:.2f} passará para R${salarioReajustado:.2f}.')

print('*' * 30)

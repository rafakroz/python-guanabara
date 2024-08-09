# Aula 10
# Desafio 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

estilo = {'limpa': '\033[m',
          'negrito': '\033[1m',
          'vermelho': '\033[31m',
          'vermelhoBold': '\033[1;31m',
          'verde': '\033[32m',
          'amarelo': '\033[33m',
          'azul': '\033[34m',
          'pretoebranco': '\033[7;30m'}

print(f'{estilo['azul']}*{estilo['limpa']}' * 30)

nome = str(input(f'{estilo['negrito']}Informe o nome do funcionário: ')).strip()
salario = float(input(f'{estilo['negrito']}Informe o salário atual: R$'))

if salario > 1250:
    salarioReajustado = salario + (salario * 0.10)
    percentual = '10%'
else:
    salarioReajustado = salario + (salario * 0.15)
    percentual = '15%'

print('*' * 30)

print(f'{estilo['negrito']}{nome}{estilo['limpa']} terá direito ao {estilo['verde']}aumento{estilo["limpa"]} de {percentual}.')
print(f'O salário atual de {estilo["amarelo"]}R${salario:.2f}{estilo["limpa"]} passará para {estilo["verde"]}R${salarioReajustado:.2f}{estilo["limpa"]}.')

print(f'{estilo['azul']}*{estilo['limpa']}' * 30)

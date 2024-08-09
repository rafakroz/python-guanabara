# Aula 12
# Desafio 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
# mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.6 e 25: Peso ideal
# Entre 25.1 e 30: Sobrepeso
# Entre 30.1 e 35: Obesidade Grau I
# Entre 35.1 e 40: Obesidade Grau II
# Acima de 40.1: Obesidade mórbida

estilo = {'clear':        '\033[m',
          'bold':      '\033[1m',
          'blue':         '\033[34m',
          'blueBold':     '\033[1;34m',
          'cyan':         '\033[36m',
          'cyanBold':     '\033[1;36m',
          'green':        '\033[32m',
          'greenBold':    '\033[1;32m',
          'grey':        '\033[37m',
          'greyBold':    '\033[1;37m',
          'purple':     '\033[35m',
          'purpleBold': '\033[1;35m',
          'red':     '\033[31m',
          'redBold': '\033[1;31m',
          'yellow':      '\033[33m',
          'yellowBold':  '\033[1;33m',
          'blackWhite': '\033[7;30m'}

asteriscos = 60

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)

nome = str(input('Nome: '))
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))

imc = peso / (altura ** 2)

print(f'''
========================================
= \033[7m        \033[1mIMC: FAIXAS e STATUS        \033[m =
=  {estilo["cyanBold"]}Abaixo de 18.5: Abaixo do Peso{estilo["clear"]}      =
=  {estilo["greenBold"]}Entre 18.6 e 25: Peso ideal{estilo["clear"]}         =
=  {estilo["blueBold"]}Entre 25.1 e 30: Sobrepeso{estilo["clear"]}          =
=  {estilo["purpleBold"]}Entre 30.1 e 35: Obesidade Grau I{estilo["clear"]}   =
=  {estilo["yellowBold"]}Entre 35.1 e 40: Obesidade Grau II{estilo["clear"]}  =
=  {estilo["redBold"]}Acima de 40.1: Obesidade Grau III{estilo["clear"]}   =
========================================
''')

if imc <= 18.5:
    print(f'Seu IMC é {estilo["bold"]}{imc:.1f}{estilo["clear"]}.')
    print(f'Status: {estilo["cyanBold"]}Abaixo do peso{estilo["clear"]}.')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é {estilo["bold"]}{imc:.1f}{estilo["clear"]}.')
    print(f'Status: {estilo["greenBold"]}Peso ideal{estilo["clear"]}.')
elif 25 < imc <= 30:
    print(f'Seu IMC é {estilo["bold"]}{imc:.1f}{estilo["clear"]}.')
    print(f'Status: {estilo["blueBold"]}Sobrepeso{estilo["clear"]}.')
elif 30 < imc <= 35:
    print(f'Seu IMC é {estilo["bold"]}{imc:.1f}{estilo["clear"]}.')
    print(f'Status: {estilo["purpleBold"]}Obesidade Grau I{estilo["clear"]}.')
elif 35 < imc <= 40:
    print(f'Seu IMC é {estilo["bold"]}{imc:.1f}{estilo["clear"]}.')
    print(f'Status: {estilo["yellowBold"]}Obesidade Grau II{estilo["clear"]}.')
elif imc > 40:
    print(f'Seu IMC é {estilo["bold"]}{imc:.1f}{estilo["clear"]}.')
    print(f'Status: {estilo["redBold"]}Obesidade Grau III{estilo["clear"]}.')

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)
# Aula 14
# Desafio 057
# Exercício 14.1
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

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

print(f'*' * asteriscos) # --------------------------------------

nome = str(input('Digite seu nome: ')).strip()
sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    print(f'{estilo["redBold"]}Dados inválidos!{estilo["clear"]}')
    sexo = str(input(f'Por favor {nome}, digite novamente seu sexo: ')).strip().upper()[0]

print(f'*' * asteriscos) # --------------------------------------

print(f'Dados registrados!')
print(f'Nome: {nome}')
print(f'Sexo: {sexo}')

print(f'*' * asteriscos) # --------------------------------------
# Aula 12
# Desafio 042
# Refaça o Desafio 035 dos Triângulos, acrescentando o recurso de mostrar que tipo de triÂngulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

estilo = {'clear':        '\033[m',
          'bold':      '\033[1m',
          'blue':         '\033[34m',
          'blueBold':     '\033[1;34m',
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

r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 and r1 == r3 and r2 == r3:
        print(f'{estilo["bold"]}Reta 1:{estilo["clear"]} {r1}')
        print(f'{estilo["bold"]}Reta 2:{estilo["clear"]} {r2}')
        print(f'{estilo["bold"]}Reta 3:{estilo["clear"]} {r3}')
        print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)
        print(f'Será formado um {estilo["greenBold"]}triângulo equilátero{estilo["clear"]}!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f'{estilo["bold"]}Reta 1:{estilo["clear"]} {r1}')
        print(f'{estilo["bold"]}Reta 2:{estilo["clear"]} {r2}')
        print(f'{estilo["bold"]}Reta 3:{estilo["clear"]} {r3}')
        print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)
        print(f'Será formado um {estilo["blueBold"]}triângulo isósceles{estilo["clear"]}!')
    elif r1 != r2 or r1 != r3 or r2 != r3:
        print(f'{estilo["bold"]}Reta 1:{estilo["clear"]} {r1}')
        print(f'{estilo["bold"]}Reta 2:{estilo["clear"]} {r2}')
        print(f'{estilo["bold"]}Reta 3:{estilo["clear"]} {r3}')
        print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)
        print(f'Será formado um {estilo["purpleBold"]}triângulo escaleno{estilo["clear"]}!')
else:
    print('Não é possível formar um triângulo!')

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)
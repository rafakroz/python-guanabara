# Aula 13
# Desafio 053
# Exercício 13.8
# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Desconsiderar acentos também.
# Palindromo: frases que podem ser lidas de trás para frente e formam a mesma frase.
# Exemplos:
# Após a sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anotaram a data da maratona

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

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split() # separando a frase me palavras

junto = ''.join(palavras) #juntando as palavras

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'A frase: {junto}')
print(f'Invertida: {inverso}')

if inverso == junto:
    print(f'É um palíndromo!')
else:
    print(f'Não é um palíndromo!')


'''
Opção sem for com técnica de fatiamento:
inverso = junto[::-1] 
: Inicia do começo
: Vai até o fim
-1 de trás para frente
'''
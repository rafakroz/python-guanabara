# Aula 16
# Desafio 073
# Exercício 16.2
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A - Apenas os 5 primeiros colocados.
# B - Os 4 últimos colocados na tabela.
# C - Uma lista com os times em ordem alfabética.
# D - Em que posição na tabela está o time da Chapecoense.

cor = {'clear':      '\033[m',
       'bold':       '\033[1m',
       'blue':       '\033[34m',
       'blueBold':   '\033[1;34m',
       'cyan':       '\033[36m',
       'cyanBold':   '\033[1;36m',
       'green':      '\033[32m',
       'greenBold':  '\033[1;32m',
       'grey':       '\033[37m',
       'greyBold':   '\033[1;37m',
       'purple':     '\033[35m',
       'purpleBold': '\033[1;35m',
       'red':        '\033[31m',
       'redBold':    '\033[1;31m',
       'yellow':     '\033[33m',
       'yellowBold': '\033[1;33m',
       'blackWhite': '\033[7;30m'}

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

lista = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro',
         'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Internacional',
         'Bragantino', 'Athletico-PR', 'Juventude', 'Criciúma', 'Grêmio',
         'Fluminense', 'Corinthians', 'EC Vitória', 'Cuiabá', 'Atlético-GO')

print('========== CAMPEONATO BRASILEIRO ==========')
print('Os 5 primeiros colocados:')
# for primeiros in range(0, 5):
#     print(f'{primeiros + 1}º - {lista[primeiros]}')
print(f'{lista[0:5]}')
print(f'-' * asteriscos) # --------------------------------------

print('Os 4 últimos colocados:')
print(f'{lista[-4:]}')
print(f'-' * asteriscos) # --------------------------------------

print('Lista ordenada:')
print(sorted(lista))
print(f'-' * asteriscos) # --------------------------------------

time = 'Flamengo'
# indice = lista.index(time)
print(f'Em que posição o {time} está? ')
print(f'Está na {lista.index(time) + 1}ª posição.')

print(f'*' * asteriscos) # --------------------------------------

# Desafio 022
# Crie um programa que leia o nome completo de uma e mostre:
# O nome com todas as letras em upper
# O nome com todas as letras em lower
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Nome completo: '))
nomeUpper = nome.upper()
nomeLower = nome.lower()
lenTotal = len(nome)
lenTotalSemEspacos = len(nome) - nome.count(' ')

nomeDividido = nome.split()

# ['Rafael', 'Queiroz', 'da', 'Silva']
#     0          1       3       4

'''
print(f'Upper: {nome.upper()}')
print(f'Lower: {nome.lower()}')
print(f'Total de caracteres: {len(nome)}')
print(f'Total sem espaços: {len(nome.replace(' ', ''))}')
print(f'Total caracteres primero nome: {len(nomeDividido[0])}')'''

print(f'Upper: {nomeUpper}')
print(f'Lower: {nomeLower}')
print(f'Total de caracteres: {lenTotal}')
print(f'Total sem espaços: {lenTotalSemEspacos}')
print(f'Total caracteres primero nome ({nomeDividido[0]}): {len(nomeDividido[0])}')
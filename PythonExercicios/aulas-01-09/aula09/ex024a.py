# Desafio 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = str(input('Digita a sua Cidade: ')).strip()

cidadeDividida = cidade.split()

print(f'Sua cidade começa com SANTO? {'SANTO' in cidadeDividida[0].upper()}')

# print(f'Sua cidade começa com SANTO? {cidade[:5].upper() == 'SANTO'}')
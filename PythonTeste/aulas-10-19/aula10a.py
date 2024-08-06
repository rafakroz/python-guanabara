# Aula 10 - Condições (Parte 1)

nome = str(input('Qual o seu nome? '))

if nome == 'Rafael':
    print(f'Olá {nome}, seja bem-vindo!')
else:
    print(f'Se retire! Você não é bem-vindo {nome}!')
    
print(f'Bom dia!')

n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

media = (n1 + n2) / 2

if media >= 6.0:
    print(f'Pelo visto você estudou! Sua média é {media}.')
else:
    print(f'Estude mais! Sua média é {media}')

# Estrutura simplificada
# print(f'Pelo visto você estudou! Sua média é {media}.' if media >= 6.0 else f'Estude mais! Sua média é {media}')
# Aula 10
# Desafio 031
# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
# e R$ 0,45 para viagens mais longas.

print('*' * 30)

distancia = float(input('Qual a distância (km) até o destino? '))

faixa1 = float(0.50) * distancia
faixa2 = float(0.45) * distancia

print('--')

if distancia <= 200:
    print(f'Distância total: {distancia}km')
    print(f'Valor da passagem: R${faixa1:.2f}')
else:
    print(f'Distância total: {distancia}km')
    print(f'Valor da passagem: R${faixa2:.2f}')

print('*' * 30)
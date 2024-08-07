# Aula 10
# Desafio 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80mh/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

carro = str(input('Modelo do carro: '))
print('*' * 40)

vel = int(input('Velocidade do carro: '))
print('*' * 40)

velMax = 80
multaKm = float(7.00)
valorMulta = float(multaKm * (vel - velMax))

if vel <= velMax:
    print(f'O {carro} passou a {vel}km/h e está dentro do limite de velocidade!')
else:
    print(f'O limite de velocidade é de {velMax}km/h.')
    print(f'O {carro} passou a {vel}km/h e foi multado!')
    print(f'Valor da multa: R${valorMulta:.2f}')

print('*' * 40)
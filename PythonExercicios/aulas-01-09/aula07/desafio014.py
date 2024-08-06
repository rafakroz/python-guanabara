# Escreva um programa que converta uma temperatura de
# C° para F°

fahrenheit = 32

temperatura = float(input('Informe a temperatura em C°: '))

conversao = ((9 * temperatura) / 5) + fahrenheit

print('-' * 10)

print(f'{temperatura}°C correspondem a {conversao}°F.')

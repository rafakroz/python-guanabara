# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros

metro = int(input('Informe o(s) metro(s): '))

cm = metro * 100
mm = metro * 1000

print(f'{metro}m em centímetros é: {cm}cm.')
print(f'{metro}m em milímetros é: {mm}mm.')
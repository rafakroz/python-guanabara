# Faça um programa que leia a LARGURA e a ALTURA de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta, pinta uma área de 2m²

largura = int(input('Largura da parede: '))
altura = int(input('Altura da parede: '))

area = largura * altura
areaTinta = 2

litros = area / areaTinta

print(f'Para pintar {area}m² (Largura {largura}m / Altura {altura}m), é preciso {litros} litros de tinta.')



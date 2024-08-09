# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()

busca = str('a')

print(f'A frase: {frase} \nContém {frase.upper().count(busca.upper())} letras "{busca}".')

print(f'A letra "{busca}" aparece pela primeira vez na posição {frase.upper().find(busca.upper()) + 1}.')

print(f'A letra "{busca}" aparece pela última vez na posição {frase.upper().rfind(busca.upper()) +1}.')

# find() indica a posição do caracter buscado
# +1, para exibir a posição de maneira mais legígel
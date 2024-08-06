# C u r s o   e m   V  í  d  e  o    P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

frase = 'Curso em Vídeo Python'

print(frase[3])

print(frase[3:13])

print(frase[:13])

print(frase[1:15:2])

print(frase[1::2])

print(frase[::2])

print("""Maecenas ipsum ante, pellentesque non dolor aliquet, sodales molestie magna.
Suspendisse tempus mauris id nulla faucibus, nec fermentum diam varius.
Ut pellentesque nibh quam. Nullam nec ex dignissim, convallis dui sit amet, aliquam magna.
Sed auctor lacus et porttitor luctus. Integer ullamcorper consequat lorem quis mollis. Quisque non ultricies est.
Proin faucibus tempor mauris at viverra. Maecenas quis mollis mauris.
Vivamus et libero mollis, tincidunt elit ac, elementum dolor.""")

print(frase.count('o'))

print(frase.count('O'))

print(len(frase)) # Quantidade de caracteres

frase2 = '   Curso em Vídeo Python   '

print(len(frase2)) # Quantidade de caracteres considerando os espaços no início e fim

print(len(frase2.strip())) # Removendo os espaço

print(frase.upper())

print(frase.lower())

print(frase.replace('Python', 'Android'))

frase3 = 'Curso em Vídeo Python (2)'
frase3 = frase3.replace('Python', 'Android')
print(frase3)

print('Curso' in frase)

print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo')) # Em caixa baixa, nenhum resultado
print(frase.lower().find('vídeo')) # Alterando a string para lower, há resultado

# C u r s o   e m   V  í  d  e  o    P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

print(frase.split())

# Resultado: ['Curso', 'em', 'Vídeo', 'Python']

dividido = frase.split()

# ['Curso', 'em', 'Vídeo', 'Python']
#     0      1       2         3

print(dividido[0])

# [2] : Vídeo
# [3] : Vídeo
#       01234

print(dividido[2][3])
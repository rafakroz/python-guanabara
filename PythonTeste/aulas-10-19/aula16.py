# Curso Python #16 - Tuplas
# https://www.youtube.com/watch?v=0LB3FSfjvao&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

#exemplo:

lanche = ('humburguer', 'suco', 'pizza', 'pudim', 'batata-frita')
#              0          1        2        3            4

# Tuplas são imutáveis! Nnao tem como alterar o valor.

# () : Tupla
# [] : Lista
# {} : Dicionário

print(lanche[2])
print(lanche[0:2]) # o últimom elemento é ignorado
print(lanche[1:]) # começa no 1 vai até o final
print(lanche[-1]) # de trás para frente

print(f'*' * asteriscos) # --------------------------------------

# se não precisar da posição do item

for c in lanche:
    print(c) 

print(f'*' * asteriscos) # --------------------------------------

# esta forma, não tem como exibir a posição

cont = 1

for item in lanche:
    print(f'Item {cont}: {item}')
    cont += 1

print(f'*' * asteriscos) # --------------------------------------

# Len para obter o tamanho da tupla
print(len(lanche))

print(f'*' * asteriscos) # --------------------------------------

# O range começa em 0 e vai até o tamanho da tupla
# O print vai exibir cada item da tupla
# obtem dado e posição

for cont2 in range(0, len(lanche)):
    print(lanche[cont2])

print(f'*' * asteriscos) # --------------------------------------

# Exibindo item e posição

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print(f'*' * asteriscos) # --------------------------------------

# sorted : exibe os itens organizados

print(sorted(lanche))

print(f'*' * asteriscos) # --------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # Forma uma tupla única

print(a)
print(b)
print(c)
print(sorted(c))

print(c.count(5)) # Conta quantas vezes houve ocorrência do valor
print(f'Resultado: {c.count(5)}') # Conta quantas vezes houve ocorrência do valor

print(f'*' * asteriscos) # --------------------------------------

print(c)
print(c.index(8)) # Exibe a posição do valor
print(c.index(2, 1))
# 2 : valor a ser buscado
# 1: a partir de qual posição (deslocamento)

print(f'*' * asteriscos) # --------------------------------------

gato = ('Fred', 2, 'M', 'Gato')

del(gato) # Apagando a tupla da memória

gato = ('Fred')

print(gato)

print(f'*' * asteriscos) # --------------------------------------

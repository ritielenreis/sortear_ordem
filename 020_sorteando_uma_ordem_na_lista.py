from random import shuffle
a = input('Digite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de Apresentação será:')
print(lista)
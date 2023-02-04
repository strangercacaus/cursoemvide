
def linha():
    print('-='*15)

print('Criando Listas:')
lista = ['Cauê', 'Marcela', 'Julia', 'Talita']
print(lista)
linha()
print('Adicionar ítem ao final da lista:')
lista.append('Isadora')
print(lista)
linha()
print('Adicionar ítem em um índice determinado:')
lista.insert(0,'Aline')
print(lista)
linha()
print('Removendo ítens de listas:')
del lista[0]
print(lista)
#Remove um ítem com base no índice
linha()
lista.pop()
print(lista)
#Se argumento for vazio, exclui o último ítem da lista, se não, é possível passar o argumento indicando o índice.
linha()
lista.remove('Talita')
print(lista)
linha()
#Remove o ítem que se equivale ao argumento passado.


print('Definindo uma lista a partir da função list()')
lista = list(range(4,11))
print(lista)
linha()
print('Ordenando uma lista com o método sort:')
lista.sort()
print(lista)
linha()
print('Ordenando uma lista com a ordem reversa no método sort:')
lista.sort(reverse=True)
print(lista)
linha()
print('Descobrindo o tamanho de uma lista utilizando len():')
print(len(lista))
linha()
print('Extraíndo o índice e o valor em pares:')
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}.')
linha()

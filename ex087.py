line = []
array = []
pares = 0
tercol = 0
maior = 0
for x in range(0, 3):
    for y in range(0, 3):
        n = int(input(f'Digite um valor para [{x}, {y}]:'))
        line.append(n)
    array.append(line[:])
    line.clear()

for x in range(0, len(array)):
    for y in range(0, len(array[x])):
        print(f'[ {array[x][y]} ]', end='')
    print('')

for x in range(0, len(array)):
    for y in range(0, len(array[x])):
        numero = array[x][y]
        if numero % 2 == 0:
            pares += numero
print(f'A soma dos valores pares é {pares}')

for x in range(0, len(array)):
    tercol =+ array[x][2]

print(f'A soma dos valores da terceira coluna é {tercol}')

for y in range(0, len(array[1])):
    if maior < array[1][y]:
        maior = array[1][y]

print(f'O maior da segunda linha é {maior}')



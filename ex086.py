line = []
array = []
for y in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para [{x}, {y}]:'))
        line.append(n)
    array.append(line[:])
    line.clear()

for y in range(0, len(array)):
    for x in range(0, len(array[x])):
        print(f'[ {array[x][y]} ]', end='')
    print('')
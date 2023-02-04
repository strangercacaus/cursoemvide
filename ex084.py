pessoas = []
maispesadas = []
maisleves = []
for c in range(1,6):
    nome = str(input('Digite um nome: '))
    peso = int(input('Digite o peso: '))
    pessoas.append(list([nome, peso])[:])
    if c == 1:
        maxpeso = minpeso = peso
    if peso < minpeso:
        minpeso = peso
    if peso > maxpeso:
        maxpeso = peso
print(f'Foram cadastradas {len(pessoas)} pessoas.')

for c in pessoas:
    if c[1] == minpeso:
        maisleves.append(c[0])
    elif c[1] == maxpeso:
        maispesadas.append(c[0])

if len(maispesadas) > 1:
    print(f'As pessoas mais pesadas, com {maxpeso}kg são:')
    for p in maispesadas:
        print(p)
elif len(maispesadas) == 1:
    print(f'A pessoa mais pesada, com {maxpeso}kg é:\n{maispesadas[0]}')

if len(maisleves) > 1:
    print(f'As pessoas mais leves, com {minpeso}kg são:')
    for p in maisleves:
        print(p)
elif len(maisleves) == 1:
    print(f'A pessoa mais leve, com {minpeso}kg é:\n{maisleves[0]}')
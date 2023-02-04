palabras = ('Vasco', 'Trono', 'John', 'Snow', 'White', 'Walker', 'Dracarys', 'Samba', 'Orlando', 'Buarque')
for p in palabras:
    temvogal = False
    print(f'\nNa palavra {p.upper()} ', end='')
    for letra in p:
        if letra in 'aeiouAEIOU':
            temvogal = True
    if temvogal:
        print('temos ', end='')
        for letra in p:
            if letra in 'aeiouAEIOU':
                print(f'{letra} ', end='')
    else:
        print('não temos vogais')
listagem = ('Pão', 1,
            'Leite', 3.50,
            'Nescau', 5.40,
            'Carne', 18.90,
            'Manteiga', 8.65,
            'Geléia', 4.35,
            'Mortadela', 3.80)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40s}')
print('_'*40)
for l in range (0, int(len(listagem)/2)):
    print(f'{listagem[l*2]:.<32s}R${listagem[l*2+1]: >6.2f}')
print('_' * 40)

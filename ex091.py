from random import randint

jogadores = ['Cacau', 'Marcela', 'Julia', 'Victor']
notas = {}
for item in jogadores:
    notas[item] = randint(1, 6)

notas_sorted = dict(sorted(notas.items(), key=lambda x: x[1], reverse=True))
print(notas_sorted)

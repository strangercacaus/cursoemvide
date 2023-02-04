from random import randint
jogos = int(input('Digite quantos jogos devem ser sorteados:'))
resultado = []
for jogo in range(1, jogos + 1):
    palpite = []
    while len(palpite) < 6:
        n = randint(1, 60)
        if n not in palpite:
            palpite.append(n)
    palpite.sort()
    resultado.append(palpite[:])

for n in range(0, len(resultado)):
    print(f'Jogo {n +1 }: {resultado[n]}')

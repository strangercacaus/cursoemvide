from random import randint
valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for v in valores:
    print(v)
print(f'O maior número sorteado foi{max(valores)}')
print(f'O menor número sorteado foi{min(valores)}')

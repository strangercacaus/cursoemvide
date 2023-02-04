n = int(input('Digite um número e descubra o seu fatorial:'))
c = n
f = 1
for c in range(n, 0, -1):
    print('{} '.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print(f)
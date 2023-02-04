o = 's'
r = 0
c = 0

while o != 'n':
    n = int(input('Digite um número: '))
    r += n
    c += 1
    if ma > n:
        ma = ma
    elif n > ma:
        ma = n
    if me
    o = str(input('Deseja Continuar? [S/N]').strip().lower())
print('Você digitou {} números, a soma foi {} e a média foi {}'.format(c, r, r/c))

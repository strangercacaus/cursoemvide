def fatorial(number, show=False):
    number
    f = 1
    if not show:
        for c in range(number, 0, -1):
            f *= c
            c -= 1
        print(f)
    else:
        for c in range(number, 0, -1):
            print('{} '.format(c), end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        print(f)


fatorial(2, show=True)

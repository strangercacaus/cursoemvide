def maior(*n):
    return sorted(n, reverse=True)[0]

print(maior(1, 2, 3, 4, 5, 6, 7, 88, 9, 10, 11))


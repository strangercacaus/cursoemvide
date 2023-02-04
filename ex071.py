resto = saque = int(input('Digite o valor a ser sacado: R$'))
cedulas = 200, 100, 50, 20, 10, 5, 1
for valor in cedulas:
    numcedulas = 0
    while resto > 0 and resto >= valor:
        resto = resto - valor
        numcedulas += 1
    if numcedulas > 0:
        print(f'Total de {numcedulas} cédulas de R${valor},00')

sexo = 'None'
while sexo not in 'MF':
    sexo = input('Digite o seu Sexo (M ou F):').strip().upper()[0]
    if sexo not in ['M', 'F']:
        print('Valor inválido.')
print('Fim')

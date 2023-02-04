def linha():
    (
        print('-' * 30)
    )


mais18 = 0
mulhermenos20 = 0
homem = 0
idade = 0
sexo = 'Undefined'
while True:
    linha()
    print('CADASTRE UMA PESSOA:')
    linha()
    idade = (int(input('Digite a Idade: ')))
    linha()
    sexo = str(input('Digite o Sexo (M ou F)')).upper().strip()[0]
    linha()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    continua = str(input('Deseja Continuar? (S ou N): ')).strip().upper()[0]
    linha()
    while continua not in 'SN':
        continua = str(input('Deseja Continuar? (S ou N): ')).strip().upper()[0]
        linha()
    if continua == 'N':
        break
print(
    f'{mais18} pessoas têm mais de 18 anos.\n{homem} Homens foram cadastrados e \n{mulhermenos20} Mulheres com menos de 20 anos foram cadastradas.')

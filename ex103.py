def ficha():
    nome = str(input('Digite o nome do jogador: '))
    if nome == '':
        nome = '<desconhecido>'
    try:
        gols = int(input('Digite a quantidade de gols: '))
    except ValueError:
        gols = 0
    print(f'O Jogador {nome} fez {gols} gols.')

ficha()

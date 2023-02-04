from random import randint

wins = 0


def linha():
    (
        print('-=' * 30)
    )


while True:
    choice = str(input('Par ou Ímpar?(P ou I): ')).strip().lower()[0]
    linha()
    while choice not in 'pi':
        choice = str(input('Escolha inválida, digite: Par ou Ímpar? (P ou I): ')).strip().lower()[0]
        linha()
    if choice == 'i':
        choicepretty = 'Ímpar'
    else:
        choicepretty = 'Par'
    comp = randint(1, 6)
    num = int(input('Escolha um Número: '))
    linha()
    if (num + comp) % 2 == 0:
        parimp = 'p'
        parimppretty = 'Par'
    else:
        parimp = 'i'
        parimppretty = 'Ímpar'
    if choice == parimp:
        wins += 1
        print(
            f'Você escolheu {num}, o computador escolheu {comp}.\nO resultado foi {num + comp} que é {parimppretty}.\nVocê escolheu {choicepretty}, você ganhou.')
        linha()
    else:
        print(
            f'Você escolheu {num}, o computador escolheu {comp}.\nO resultado foi {num + comp} que é {parimppretty}.\nVocê escolheu {choicepretty}, você perdeu.')
        linha()
        break
print(f'Total de Vitórias: {wins}')

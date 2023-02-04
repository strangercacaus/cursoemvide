def escreva(text):
    frase = f'{text:^30}'
    length = (len(frase))
    print('-' * length)
    print(frase)
    print('-' * length)


escreva('Deixa os garoto brincá')

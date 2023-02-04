from random import randint
num = randint(1,10)
palpite = int(input('Digite o seu palpite:'))
tentativas = 1
while palpite != num:
    if palpite > num:
        palpite = (int(input('Menos... digite um novo palpite:')))
    elif palpite < num:
        palpite = (int(input('Mais... digite um novo palpite:')))
    tentativas += 1
print('O Número  era {}, você acertou com {} tentativas!'.format(num,tentativas))
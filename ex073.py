times = ('Chapecoense', 'Figueirense', 'Avaí', 'Vasco', 'Internacional', 'Fluminense', 'Boca Juniors')
print('Seja bem vindo a tabela do Brasileitrab')
print('-=' * 18)
opcao = 'Z'
while opcao not in 'ABCD':
    print('Selecione a opção Desejada:')
    print('-=' * 18)
    print('A: 3 Primeiros colocados')
    print('B: Últimos 2 colocados')
    print('C: Times em ordem alfabética')
    print('D: Chapecoense')
    print('-=' * 18)
    opcao = str(input('Sua Escolha: ')).strip().upper()[0]
if opcao == 'A':
    for t in times[0:3]:
            print(t)
elif opcao == 'B':
        for t in times[-2:]:
            print(t)
elif opcao == 'C':
        for t in (sorted(times)):
            print(t)
else:
        print((times.index('Chapecoense')+1))


from random import randint
funcao = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('Numeros escolhidos: {} e {}'.format(num1, num2))
while funcao != 5:
    funcao = int(input('Digite a função desejada:\n1: Somar\n2: Multiplicar\n3: Maior\n4: Novos Números\n5: Sair do Programa\nEscolha: '))
    if funcao == 1:
        print('--------------------------------------------------')
        print('A soma entre {} e {} é {}'.format(num1, num2, num1 + num2))
        print('--------------------------------------------------')
    elif funcao == 2:
        print('--------------------------------------------------')
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, num1 * num2))
        print('--------------------------------------------------')
    elif funcao == 3:
        print('--------------------------------------------------')
        print('O maior número entre {} e {} é {}'.format(num1, num2,max(num1,num2)))
        print('--------------------------------------------------')
    elif funcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um outro número: '))
        print('--------------------------------------------------')
        print('Os Novos númeroes escolhidos foram {} e {}'.format(num1, num2))
        print('--------------------------------------------------')
    elif funcao == 5:
        True
    else:
        print('--------------------------------------------------')
        print('Função Inválida!')
        print('--------------------------------------------------')
        funcao = int(input('Digite a função desejada:\n 1: Somar\n2:Multiplicar\n3:Maior\n4:Novos Números\n5: Sair do Programa\nEscolha'))
        print('--------------------------------------------------')
print('Programa Encerrado')


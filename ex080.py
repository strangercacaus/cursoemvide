# Desafio 080
list = []
while True:
    num = int(input('Digite um número (999 para parar):'))
    if num == 999:
        break
    else:
        if num not in list:
            if list == [] or num > list[-1]:
                list.append(num)
                print(f'Número adicionado ao final da lista.')
            else:
                pos = 0
                while pos < len(list):
                    if num <= list[pos]:
                        list.insert(pos, num)
                        break
                    pos += 1
                print(f'Número adicionado na posição {pos} da lista.')
        else:
            print('Este número já foi digitado, digite novamente')

print(f'Você digitou os números {list}')

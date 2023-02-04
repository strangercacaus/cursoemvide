def linha():
    print('-'*30)

linha()
print('Sequência de Fibonice')
linha()

n = int(input('Digite um número: '))
list = [0,1]
c = 1
while c < n-1:
    list.append (list[-1] + list[-2])
    c += 1
for o in list[0: n]:
    print('{} > '.format(o), end= '')
print('Fim')

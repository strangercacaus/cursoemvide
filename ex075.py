valores = (int(input('Digite um número: ')),
         int(input('Agora mais um: ')),
         int(input('E outro: ')),
         int(input('E o último: ')))
print(f'O Valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O Valor 3 foi digitado na {valores.index(3)+1} posição.')
else:
    print('O Número 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for v in valores:
    if v % 2 == 0:
          print(v, end=' ')


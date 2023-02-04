#Desafio 082
list = []
while True:
  num = int(input('Digite um número (999 para parar):'))
  if num == 999:
    break
  else:
    if num not in list:
     list.append(num)

print(f'Você digitou os números {list}')
listpares = []
listimpares = []
for n in list:
  if n % 2 == 0:
    listpares.append(n)
  else:
    listimpares.append(n)
print(f'Os Números pares são {listpares}')
print(f'Os Números ímpares são {listimpares}')

#Desafio 079
list = []
while True:
  num = int(input('Digite um número (999 para parar):'))
  if num == 999:
    break
  else:
    if num not in list:
      list.append(num)
list.sort()
print(f'Você digitou os números {list}')
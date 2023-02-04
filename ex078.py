#Desafio 078
list = []
for const in range(1,6):
  list.append(int(input('Digite um número:')))
print(f'Você digitou os números {list}')
print('-='*30)

print(f'O maior valor é {max(list)},nas posições ',end='')
for ind, num in enumerate(list):
  if num == max(list):
    print(f'{ind}...', end='')
print('')
print('-='*30)


print(f'O menor valor é {min(list)},nas posições ',end='')
for ind, num in enumerate(list):
  if num == min(list):
    print(f'{ind}...', end='')
print('')
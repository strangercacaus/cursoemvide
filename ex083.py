#Desafio 083
expr = str(input('Digite uma Expressão com parênteses:'))
pabertos = 0
for c in expr:
  if c == '(':
    pabertos += 1
  if c == ')':
    pabertos -= 1
  if pabertos < 0:
    break
if pabertos == 0:
  print('A expressão está correta.')
else:
  print('Erro de sinxtaxe: Número incorreto de parênteses.')

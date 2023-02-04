result = numlist = []
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    numlist.append(num)
print(sum(numlist, 0))
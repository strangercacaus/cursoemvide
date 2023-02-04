num = int(input('Digite um número: '))
result = []
while num != 999:
    numlist.append(num)
    print(numlist)
    num = int(input('Digite um número: '))
print(sum(numlist, 0))
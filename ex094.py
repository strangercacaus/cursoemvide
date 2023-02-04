people = {}
while True:
    name = str(input('Digite um nome: '))
    sex = str(input('Digite o Sexo (M/F): ')).strip().upper()
    age = int(input('Digite a Idade: '))
    people[name] = {'sexo': sex, 'idade': age}
    option = str(input('Deseja continuar? (S/N')).strip().lower()
    if option in ('Nn'):
        break
print(people)

print(f'No total, {len(people)} pessoas foram cadastradas.')
temp = []
for l in people.values():
    temp.append(l['idade'])
avgage = sum(temp)/len(temp)
print(f'A média de idade do grupo é de {avgage:5.2f} anos.')
for l in people.keys():
    if people[l]['sexo'] == 'F':
        print(f'{l} é do sexo feminino.')
for l in people.keys():
    if people[l]['idade'] > avgage:
        print(f'{l} está acima da média de idade.')
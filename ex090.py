aluno = {'nome': 'Cacau', 'media': 0}
aluno['nome'] = anome = str(input('Digite o nome do aluno: '))
aluno['media'] = amedia = float(input('Digite a média do aluno: '))

if aluno['media'] >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
print(f'Situação do Aluno: {situacao}')
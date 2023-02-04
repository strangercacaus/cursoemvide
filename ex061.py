primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contagem = 1
limite = 10
resultado = primeirotermo
numad = 1
while numad != 0:
    while contagem <= limite:
        print('Termo {} = {}'.format(contagem,resultado))
        contagem += 1
        resultado += razao
    numad = int(input('Digite quantos números adicionais você deseja ver: '))
    limite += numad
print('Fim')
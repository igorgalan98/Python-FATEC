n1 = int(input('Digite a primeira nota: '))
kg1 = int(input('Digite o primeiro peso: '))
n2 = int(input('Digite a segunda nota: '))
kg2 = int(input('Digite o segundo peso: '))
n3 = int(input('Digite a terceira nota: '))
kg3 = int(input('Digite o terceiro peso: '))

nota = n1 * kg1 + n2 * kg2 + n3 * kg3
div = kg1 + kg2 + kg3
media = nota / div

print('A nota média envolvendo o resultado {}, {}, e {}, para o peso de {}, {} e {} é {:.2f}'.format(n1, n2, n3, kg1, kg2, kg3, media))
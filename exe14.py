def positivo():
# Função para solicitar um número positivo
    while True:
# lopp que se repete até receber o resultado desejado
        try:
            numero = float(input('digite um número positivo maior que zero: '))
            if numero > 0:
                return numero
            else:
                print('O número deve ser maior que zero. Tente novamente.')
        except ValueError:
            print('Isso não é um número válido. Tente novamente.')

def operacoes(numero): 
    quadrado = numero ** 2
    cubo = numero ** 3
    raizQuadrada = numero ** (1/2)
    raizCubica = numero ** (1/3)

    print(f'Número: {numero:.2f}')
    print(f'Quadrado: {quadrado:.2f}')
    print(f'cubo: {cubo:.2f}')
    print(f'Raiz quadrada: {raizQuadrada:.2f}')
    print(f'raiz cúbica: {raizCubica:.2f}')

numero = positivo()
# Primeiro, o programa chama 'positivo()' para obter um número positivo do usuário.
operacoes(numero)
# Em seguida, ele passa esse número para 'operacoes(numero)' para exibir os cálculos.
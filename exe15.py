def acharNumero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            if numero > 0:
                return numero
            else:
                print('O número deve ser maior que zero. Tente novamente.')
        except ValueError:
            print('Isso não é um número válido. Tente novamente.')

def contas(base, expoente):
    total = base ** expoente
    print(f'{base} elavado a {expoente} é igual a {total:.2f}')

base = acharNumero('Digite o número base: ')
expoente = acharNumero('Digite o número expoente: ')

contas(base, expoente)
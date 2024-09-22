def valorAno(mensagem):
    while True:
        try:
            ano = int(input(mensagem))
            if ano > 0:
                return ano
            else: print('Favor, informar um ano válido')
        except ValueError:
            print('Favor, inserir apenas números')

def calcAno(ano):
    idade = 2024 - ano
    idadeFutura = 2005 - ano
    print(f'A idade referente ao ano atual é "{idade}". E em 2005 a idade referente era "{idadeFutura}"')

ano = valorAno('Digite o ano de nascimento: ')
calcAno(ano)
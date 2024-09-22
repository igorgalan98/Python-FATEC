salario = int(input('Digite seu salário: '))
desconto = 25 / 100
calc = salario * desconto
total = salario + calc
print('Seu salário prévio de {} recebeu um aumento de {:.2f}. Resultando um total de {:.2f}'.format(salario, calc, total))

salario = float(input('Digite seu salário: '))
# salário é uma variante que recebe int de inteiro
aumento = float(input('Digite o valor do aumento: '))
# aumento é uma variante que recebe float de futuável
desconto = aumento / 100
# cria outra variante para dividir
calc = salario * desconto
# cria outra variante para multiplicar
total = salario + calc
# variante para somar o salário e o cálculo do desconto
print('Seu salário prévio de {} recebeu um aumento de {:.2f}. Resultando um total de {:.2f}'.format(salario, calc, total))
# print para imprimir, {} para preencher, 2f para aparecer dois números após a vírgula e .format para puxar as info das variates

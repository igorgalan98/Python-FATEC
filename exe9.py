base = float(input('Digite seu salário base: '))
gratidao = 5 / 100
imposto = 7 / 100
gratSal = base * gratidao
impSal = base * imposto
total = base + gratSal - impSal
print('O salário base de "{:.2f}", sobre um imposto de 7% "{:.2f}" e uma gratificação de "{:.2f}" referentes ao salário base, teve um resultado de "{:.2f}"'.format(base, impSal, gratSal, total))
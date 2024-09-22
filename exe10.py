base = float(input('Digite seu salário base: '))
grat = 50
imp = 10 / 100
impBase = base * imp
total = base + grat - impBase
print('Com um salário base de "{:.2f}", gratificação de "{:.2f}", e um imposto de 10 por cento do salário de base "{:.2f}" equivale a um salário de: {:.2f}'.format(base, grat, impBase, total))
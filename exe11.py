deposito = float(input('Digite o valor do seu depósito: '))
juros = int(input('Digite o valor do juros: '))
jcal = juros / 100
djcal = deposito * jcal
total = deposito + djcal
print('O seu depósito de "{:.2f}", com um juros de "{:.2f}", equivale a um rendimento de "{:.2f}" e um total de "{:.2f}" sobre o salário'.format(deposito, jcal, djcal, total))
nome = str(input('Informe o nome do vendedor: '))
salario = float(input('Informe o salário mínimo: '))
vendas = float(input('Informe o total de vendas efetuadas no mês: '))

media = 15 / 100
comissao = vendas * media
total = comissao + salario

print(f'O(A) vendedor(a) {nome} recebeu no final do mês o salário de = {total:.2f}')
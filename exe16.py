def valorPe(mensagem):
    while True:
        try:
            pe = float(input(mensagem))
            if pe > 0:
                return pe
            else: print('O número inserido deve ser maior que 0')
        except ValueError:
            print('Este não é um valor válido, favor inserir apenas números')

def calc(pe):
    polegadas = pe * 12
    jardas = pe / 3
    milhas = pe / (3 * 1760)
    print(f'As polegadas valem: "{polegadas:.2f}" As jardas: "{jardas:.2f}" as milhas valem: "{milhas:.2f}"')

pe = valorPe('Digite o valor de pés a ser calculado: ')

calc(pe)
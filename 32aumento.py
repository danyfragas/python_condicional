# exercício 31: escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250.00 calcule um aumento de 10%. Para os inferiores ou iguais, aumento é de 15%.

sal = float(input('Informe o seu salário atual: R$ '))

if sal > 1250.00:
    novo = sal * 0.10
    print(f'O seu novo salário com 10% de aumento será: R$ {novo}')
else:
    novo = sal * 0.15
    print(f'O seu novo salário com 15% de aumento será: R$ {novo}')

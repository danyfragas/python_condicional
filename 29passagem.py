# exercício 29: escreva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km p/ viagens de até 200Km e R$0.45 p/ viagens mais longas.

d = float(input('Informe a distância da viagem em Km: '))
if d >= 200:
    passagem = 0.45 * d
else:
    passagem = 0.50 * d

print('O valor da passagem custará: R$ {:.2f}'. format(passagem))

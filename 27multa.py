# exercício 27: escreva um programa que leia a velocidade de um carro se ele ultrapassar 80km/h, mostre uma mensagem dinzendo que ele foi multado. A multa vai custar R$7.00 A CADA Km acima do limite.

vel = float(input('Velocidade do veículo em km/h: '))

if vel > 80.0:
    print('Caro usuário, a velocidade informada ultrapassa a média de 80km/h. Portanto, você foi multado.')
    multa = (vel - 80) * 7
    print('O valor da multa é de: R$ {:.2f}'. format(multa))
else:
    print('Você está dentro do limite de velocidade.')

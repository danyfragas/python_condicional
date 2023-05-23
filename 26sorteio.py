# exercício 26: escreva um programa que faça o computador "pensar" em um nº int entre 0 e 5 e peça para o usuário tentar descobrir qual foi o nº escolhido pelo computador. O programa deverá escrever na tela se ganhou ou perdeu.

import random
# from random improt randit

# sorteio = randit [0, 5]
num = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(num)

n = int(input('Insira o número: '))
print('O número sorteado foi: {}'. format(sorteio))

if n == sorteio:
    print('Você ganhou! C:')
else:
    print('Você perdeu! :C')

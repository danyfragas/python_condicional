# exercício 28: escreva um programa que leia um nº int e mostre na tela se ele é PAR ou ÍMPAR

n = int(input('Informa o número: '))
resto = n % 2

if resto == 0:
    print('O número {} é PAR!'. format(n))
else:
    print('O número {} é ÍMPAR'. format(n))

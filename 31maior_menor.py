# exercício 31: escreva um programa que leia três números e mostre qual é o maior e menor.

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n2
if n1 > n2 and n1 > n2:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3

'''
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3
'''

print(f'O maior número é o {maior}, e o menor é {menor}.')


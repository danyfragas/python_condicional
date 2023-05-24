# exercício 33: escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

a = float(input('Informe o comprimento da linha "a": '))
b = float(input('Informe o comprimento da linha "b": '))
c = float(input('Informe o comprimento da linha "c": '))

if a + b > c and a + c > b and b + c > a:
    print('É possível fazer um triângulo com essas medidas.')
else:
    print('Não é possível fazer um triângulo com essas medidas.')

import math

def calcular_raizes(a,b,c):
    if a == 0:
        print('A equação não é de segundo graau')
        return
    delta == b**2 - 4*a*c

    if delta < 0:
        print('A equação naõ tem valores reais')
    elif delta == 0:
        raiz = -b /(2*a)
        print('A equação possui uma raiz real: ', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        print('A equação possui duas raízes reais:')
        print('Raiz 1: ', raiz1)
        print('Raiz 2: ', raiz2)

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
calcular_raizes(a,b,c)
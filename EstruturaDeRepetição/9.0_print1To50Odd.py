#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print('Este programa exibirá os números ímpares entre 1 e 50')

def escalador():
    resto = 1
    while resto >= 1 and resto < 50:
        if resto % 2:
            print(resto)
            resto += 1
        else:
            resto += 1
    return

escalador()
        
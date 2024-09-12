#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print('Este programa exibirá os números ímpares entre 1 e 50')

def escalador():
    marcador = 1
    while marcador >= 1 and marcador < 50:
        if marcador % 2:
            print(marcador)
            marcador += 1
            pass
        else:
            marcador += 1
    return

escalador()
        
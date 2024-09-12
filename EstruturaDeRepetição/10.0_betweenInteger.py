# Faça um programa que receba dois números inteiros e gere os números 
# inteiros que estão no intervalo compreendido por eles. 

pri = int(input('Digite o primeiro numero \n'))
sec = int(input('Digite o segundo numero \n'))

def intervalo(a,b):
    print('-'*30)
    if a < b:
        while a < b-1:
            a += 1
            print(a)
            
    elif b < a:
        while b < a-1:
            b += 1
            print(b)
    return 
        
    

intervalo(pri, sec)
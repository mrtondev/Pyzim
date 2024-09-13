#Altere o programa anterior para mostrar no final a soma dos números. 

pri = int(input('Digite o primeiro numero \n'))
sec = int(input('Digite o segundo numero \n'))

def intervalo(a,b):
    print('-'*30)
    c = 0
    if a < b:
        while a < b-1:
            c += a
            a += 1
            print(a)
            
    elif b < a:
        while b < a-1:
            c += b
            b += 1
            print(b)
    print('Soma do total: ', c)
    return 
        
    

intervalo(pri, sec)
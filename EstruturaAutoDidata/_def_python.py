def calculadora(numa,numb):

        res=float
        conta = str

        conta = input('Operador ( + - * /) \n') 

    
        match conta:
            case '+':
                res = numa + numb
                print('Resultado:{:.2f}' .format(res))   
            case '-':
                res = numa - numb
                print('Resultado: {:.2f}' .format(res))
            case '*':
                res= numa * numb
                print('Resultado: {:.2f}' .format(res))   
            case '/':
                res = numa / numb
                print('Resultado: {:.2f}' .format(res))
            case _:
                print('Erro')

a=float(input('Digite o valor do primeiro num \n'))
b=float(input('Digite o valor do segundo \n'))
calculadora(a,b)    
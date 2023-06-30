print('Calculadora')
print('Início.... \n')
mat1=float(input(' \n'))
mat2=float(input(' \n'))
res=str
op=input('( + - * /)\n')
while True:
    def cal(prim,seg):
        
        result=float
        match op:
            case '+':
                result=prim + seg
                print('{:.2f}' .format(result))
            case '-':
                result=prim - seg
                print('{:.2f}' .format(result))
            case '*':
                result=prim * seg
                print('{:.2f}' .format(result))
            case '/':
                result=prim / seg
                print('{:.2f}' .format(result))
            case _:
                print('Erro')
        
    cal(mat1,mat2)
    res=input('Deseja realizar outra conta: (S para sim || N para não)\n')
    if res.upper() == 'N':
        break
    elif res.upper() == 'S':
        mat1=float(input('\n'))
        mat2=float(input('\n'))
        op=input('( + - * /)\n')
        cal(mat1,mat2)
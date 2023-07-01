print('Calculadora')
print('Início.... \n')

while True:
    mat1 = float(input(' \n'))
    mat2 = float(input(' \n'))
    op = input('( + - * /)\n')
    
    def cal(prim, seg):
        result = float
        match op:
            case '+':
                result = prim + seg
                print('{:.2f}'.format(result))
            case '-':
                result = prim - seg
                print('{:.2f}'.format(result))
            case '*':
                result = prim * seg
                print('{:.2f}'.format(result))
            case '/':
                result = prim / seg
                print('{:.2f}'.format(result))
            case _:
                print('Erro')

    cal(mat1, mat2)
    
    res = input('Deseja realizar outra conta: (S para sim || N para não)\n')
    if res.upper() == 'N':
        break
    elif res.upper() == 'S':
        continue
    

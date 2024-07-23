#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


import time



#pA = 80000

#pB = 200000

#cresA =  3

#cresB = 1.5





def povoCresc():

    anos = 0

    pA=float(input('Digite a população do país A \n '))
    pB=float(input('Digite a população do país B \n '))

    cresA=float(input('Agora digite a Taxa Anual de Crescimento do País A\n'))
    cresB=float(input('Agora digite a Taxa Anual de Crescimento do País B\n'))

    print('População inicial do País A: 80000 \n')
    print('População inicial do País B: 200000 \n')

    while pA <= pB:
        pA += pA * (cresA/100)
        pB += pB * (cresB/100)
        anos += 1
        print('Ano:', anos)
        print('População A:', pA)
        print('População B:', pB)
        time.sleep(1.5)

    print('Em', anos , 'anos , a População do País A superou a do País B \n')

    return 

povoCresc()

resp = str(input('Deseja executar o programa novamente?\n'))

while resp.upper() == "S":
    povoCresc()
else:
    print('Fim do programa\n')

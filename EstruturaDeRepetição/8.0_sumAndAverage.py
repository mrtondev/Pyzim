#Faça um programa que leia 5 números e informe a soma e a média dos números. 

print('Programa irá ler 5 números, informar a soma deles e em seguida sua média')

primeiro = float(input('Digite o primeiro número \n '))
segundo = float(input('Digite o segundo número \n '))
terceiro = float(input('Digite o terceiro número \n '))
quarto = float(input('Digite o quarto número \n '))
quinto = float(input('Digite o quinto número \n '))

def somaMaisMedia(a,b,c,d,e):
    total = 0
    media = 0
    total =a+b+c+d+e
    media = total / 5

    print('soma dos 5 números: ', total ,'\n')
    print('media da soma dos 5 números:',media , '\n' )

    return

somaMaisMedia(primeiro, segundo, terceiro, quarto, quinto)
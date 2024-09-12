#Faça um programa que leia 5 números e informe o maior número.

print('Insira 5 números (um de cada vez) e o programa lhe informará o maior número')

primeiro = float(input('Digite o primeiro número \n '))
segundo = float(input('Digite o segundo número \n '))
terceiro = float(input('Digite o terceiro número \n '))
quarto = float(input('Digite o quarto número \n '))
quinto = float(input('Digite o quinto número \n '))

def maiorN(a,b,c,d,e):
    if a > b and a > c and a > d and a > e:
        print(a,' Primeiro é o maior')
    elif b > a and b > c and b > d and b > e:
        print(b,' Segundo é o maior')
    elif c > a and c > b and c > d and c > e :
        print(c,' Terceiro é o maior')
    elif d > a and d > b and d > c and d > e :
        print(d,' Quarto é o maior')
    else:
        print(e,' Quinto é o maior')


maiorN(primeiro, segundo, terceiro, quarto, quinto)


def execucao(nome, ocorrido):

    nomes = ['Neymar', 'Cristiano Ronaldo', 'Messi', 'Xavi' , 'Zidane', 'Vini Júnior' ]

    ocorridos = [ 'Joga na seleção' , 'É um excelente jogador', 'Ganhou muitos campeonatos', 'É um jogador renomado', 
                'Seria um ótimo técnico', 'Poderia ser goleiro?']
   
    print(nomes[nome], ocorridos[ocorrido])
    

    return

a = int(input('Digite um número de 0 a 5 para o nome do jogador \n'))
b = int(input('Agora digite um número de 0 a 5 para a frase de complemento \n'))

execucao(a, b)
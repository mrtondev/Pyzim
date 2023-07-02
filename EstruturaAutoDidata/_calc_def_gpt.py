def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

while True:
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = soma(num1, num2)
        print("Resultado da soma:", resultado)
    elif opcao == "2":
        resultado = subtracao(num1, num2)
        print("Resultado da subtração:", resultado)
    elif opcao == "3":
        resultado = multiplicacao(num1, num2)
        print("Resultado da multiplicação:", resultado)
    elif opcao == "4":
        resultado = divisao(num1, num2)
        print("Resultado da divisão:", resultado)
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

    print()  # Linha em branco para separar as operações

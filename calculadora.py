import sys
# Essa calculadora foi feita para treinar o que aprendi sobre importação e definir funções


def input_calc():
    escolha = int(input("selecione: soma (1) multiplicação (2) divisão (3) sair(4) "))

    if escolha == 1:
        soma_calc()
    elif escolha == 2:
        multiplicar_calc()
    elif escolha == 3:
        dividir_calc()
    elif escolha == 4:
        sair()
    else:
        print("\nOpção inválida\n")
        input_calc()


def soma_calc():
    print("\n** Calculadora de soma **\n")
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))

    calc_numbers = soma(num1, num2)

    print(f"O resultado é: {calc_numbers}\n")

    input_calc()


def multiplicar_calc():
    print("\n** Calculadora de multiplicação **\n")
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))

    calc_numbers = multiplica(num1, num2)

    print(f"O resultado é: {calc_numbers}\n")

    input_calc()


def dividir_calc():
    print("\n** Calculadora de divisão **\n")
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))

    calc_numbers = divide(num1, num2)

    print(f"O resultado é: {calc_numbers}\n")

    input_calc()


def sair():
    sys.exit(0)


def soma(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiplica(a, b):
    return a * b


if __name__ == "__main__":
    input_calc()

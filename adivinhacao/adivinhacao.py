from turtle import clear

print("******************\n\tAdvinhação\t\n******************\n")

rodada = 1
chances = 3
num_secreto = 42

while rodada < chances:
    print("Rodada ", rodada, " de 3\n")
    rodada += 1
    num_digitado_str = input("Digite o número: ")

    print("\nVocê digitou: ", num_digitado_str)

    tentativa = int(num_digitado_str)

    # Variável para condições
    tentativa_correta = tentativa == num_secreto
    tentativa_maior = tentativa > num_secreto
    tentativa_menor = tentativa < num_secreto

    if tentativa_correta:
        print("Você acertou!")
    else:
        if tentativa_maior:
            print("Você errou! Seu valor foi MAIOR que o número secreto.\n")
        elif tentativa_menor:
            print("Você errou! Seu valor foi MENOR que o número secreto.\n")

    rodada += 1
    chances -= 1

print("\tFim de Jogo")
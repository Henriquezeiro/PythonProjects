import random

print("\n\x1B[3m************* Jogo da Adivinhação *************\x1B[3m\n")

rodada = 1
chances = 5
num_secreto = random.randint(1, 100)

for rodada in range(1, chances + 1):

    print("\033[3;35m" "rodada {} de 5" "\033[0m".format(rodada))
    num_digitado_str = input("Digite o número entre 1 e 100: ")
    print("\nVocê digitou: ", num_digitado_str)
    tentativa = int(num_digitado_str)

    if tentativa < 1 or tentativa > 100:
        print("\033[1;3;31m" "Número inválido! Tente algo entre 1 e 100" "\033[0m\n")
        continue

    # Variável para condições
    tentativa_correta = tentativa == num_secreto
    tentativa_maior = tentativa > num_secreto
    tentativa_menor = tentativa < num_secreto

    if tentativa_correta:
        print("\033[32m" "\x1B[3m" "Você acertou! O número secreto era" "\x1B[0m" "\033[0m", num_secreto)
        break
    else:
        if tentativa_maior:
            print("\033[31m" "\x1B[3m" "Você errou! Seu valor foi MAIOR que o número secreto." "\x1B[0m" "\033[0m\n")
        elif tentativa_menor:
            print("\033[31m" "\x1B[3m" "Você errou! Seu valor foi MENOR que o número secreto." "\x1B[3m" "\033[0m\n")
    if chances == 1:
        print("\033[33m" "\x1B[3m" "O número secreto era" "\x1B[3m" "\033[0m", num_secreto)

    chances -= 1

print("\n" "\x1B[3m" "************* Fim de Jogo *************" "\x1B[3m")
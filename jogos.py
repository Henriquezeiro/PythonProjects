import adivinhacao
import forca


def escolher_jogo():
    print("\n** Escolha o Jogo **\n")

    escolha = int(input("Adivinhação (1) Forca (2) | "))

    if escolha == 1:
        adivinhacao.jogar()
    elif escolha == 2:
        forca.jogar()
    elif escolha == 3:
        exit(0)
    else:
        print("Opção inválida!")
        escolher_jogo()


if __name__ == "__main__":
    escolher_jogo()

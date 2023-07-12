import adivinhacao
import forca
import calculadora


def escolher_jogo():
    print("\n** Escolha o Jogo **\n")

    escolha = int(input("Adivinhação (1) Forca (2) Calculadora (3): "))

    if escolha == 1:
        adivinhacao.jogar()
    elif escolha == 2:
        forca.jogar()
    elif escolha == 3:
        calculadora.input_calc()
    else:
        print("Opção inválida!")
        escolher_jogo()


if __name__ == "__main__":
    escolher_jogo()

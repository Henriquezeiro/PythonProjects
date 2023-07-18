def jogar():
    global letra
    print("\n************* Jogo da Forca *************\n")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("\nqual a letra: ")
        index = 1
        for letra in palavra_secreta:
            if chute == letra:
                print("letra {} encontrada na posição {} ".format(letra, index))
            index += 1

        print("jogando...")


if __name__ == "__main__":
    jogar()

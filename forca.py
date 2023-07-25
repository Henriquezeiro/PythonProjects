import random


def jogar():
    imprimir_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()  # arruma isso depois organizando em funções
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    # Enquanto não enforcou e nem acertou o loop continua. É usado not para inverter os valores para TRUE para que o
    # loop possa funcionar
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:  # se o chute estiver em palavra secreta irá ser substitution os underscore
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)

        else:  # se a letra chutada não estiver na palavra secreta o erro será incrementado em 1
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7  # enforcou será True se os erros forem iguais a 5
        acertou = "_" not in letras_acertadas  # acertou será True se os underscores não estiverem em letras_acertadas
        print(letras_acertadas)  # mostra no terminal quais letras estão corretas substituindo os underscores

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprimir_mensagem_inicial():
    print("\n*****************************************")
    print("************* Jogo da Forca ***************")
    print("*******************************************\n")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="utf-8")  # abrir arquivo txt
    palavras = []  # Lista vazia para receber o conteúdo

    for linha in arquivo:  # loop para adicionar cada linha do arquivo na lista
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()  # fechar arquivo
    numero_aleatorio = random.randrange(0, len(palavras))  # gera número aleatório para definir como índice da lista
    palavra_secreta = palavras[numero_aleatorio].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("\nqual a letra: ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Você ganhou!")
    print("   _____ ")
    print(" ( \\   / )")
    print("    \\ /")
    print("    /_\\")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu!")
    print("Palavra Secreta:", palavra_secreta)
    print("    _________")
    print("  /           \\")
    print(" |   x     x   |")
    print("  \\    ^      /")
    print("     |_|_|_|  ")
    print("     |-|-|-|")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()

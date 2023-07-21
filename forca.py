import random


def jogar():
    imprimir_mensagem_inicial()
    carrega_palavra_secreta() # arruma isso depois organizando em funções

    numero_aleatorio = random.randrange(0, len(palavras))  # gera número aleatório para definir como índice da lista

    palavra_secreta = palavras[numero_aleatorio].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    # Enquanto não enforcou e nem acertou o loop continua. É usado not para inverter os valores para TRUE para que o
    # loop possa funcionar
    while not enforcou and not acertou:
        chute = input("\nqual a letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:  # se o chute estiver em palavra secreta irá ser substitution os underscore
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:  # se a letra chutada não estiver na palavra secreta o erro será incrementado em 1
            erros += 1

        enforcou = erros == 5  # enforcou será True se os erros forem iguais a 5
        acertou = "_" not in letras_acertadas  # acertou será True se os underscores não estiverem em letras_acertadas
        print(letras_acertadas)  # mostra no terminal quais letras estão corretas substituindo os underscores

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")


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


if __name__ == "__main__":
    jogar()

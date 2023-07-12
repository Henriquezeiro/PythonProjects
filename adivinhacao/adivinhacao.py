import random

print("\n************* Jogo da Adivinhação *************\n")

chances = 0
num_secreto = random.randrange(1, 101) # Gera um número aleatório
pontos = 1000

# funcionalidade para seleção de níveis
print("Qual o nível de dificuldade?\nfácil (1) médio (2) difícil (3)")
nivel = int(input("Defina o nível: "))

if nivel == 1:
    chances = 20
elif nivel == 2:
    chances = 10
else:
    chances = 5

# loop de rodadas
for rodada in range(1, chances + 1):

    print(f"\nrodada {rodada} de {chances}")
    tentativa = int(input("Digite o número entre 1 e 100: "))
    print(f"Você digitou: {tentativa}")

    if tentativa < 1 or tentativa > 100:
        print("Número inválido! Tente algo entre 1 e 100\n")
        continue

    # Variável para condições
    tentativa_correta = tentativa == num_secreto
    tentativa_maior = tentativa > num_secreto
    tentativa_menor = tentativa < num_secreto

    if tentativa_correta:
        print(f"Você acertou e fez {pontos} pontos!! O número secreto era", num_secreto)
        break
    else:
        pontos_perdidos = abs(num_secreto - tentativa)
        pontos = pontos_perdidos
        if tentativa_maior:
            print("Você errou! Seu valor foi MAIOR que o número secreto.\n---------------------------------------------")
            if rodada == chances:
                print(f"O número secreto era {num_secreto} e você fez {pontos} pontos.")

        elif tentativa_menor:
            print("Você errou! Seu valor foi MENOR que o número secreto.\n---------------------------------------------")
            if rodada == chances:
                print(f"O número secreto era {num_secreto} e você fez {pontos} pontos.")

print("************* Fim de Jogo *************")

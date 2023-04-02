import random

print("--------------------------------------------")
print("Seja bem-vindo! Esse é o jogo de advinhação!")
print("--------------------------------------------")

# variável do tipo int que armazena o número secreto
num_secreto = random.randrange(1, 101)
# variável do tipo int que armazena o número máximo de tentativas
total_de_tentativas = 0
pontos = 100

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Rodada {} de {}!".format(rodada, total_de_tentativas))
    # variável do tipo int que armazena o número escolhido pelo usuário
    num_escolhido = int(input("Digite o seu número inteiro entre 1 e 100: "))
    print("Você digitou: {}".format(num_escolhido))
    
    if num_escolhido < 1 or num_escolhido > 100:
        print("Você deve digitar um número inteiro entre 1 e 100!\n")
        continue
    
    # variáveis que armazenam as condições de comparação
    acertou = num_secreto   == num_escolhido
    maior   = num_escolhido >  num_secreto
    menor   = num_escolhido <  num_secreto


    # condição que verifica se o usuário acertou o número secreto
    if (acertou):
        print("Você ACERTOU! Você fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você ERROU! O seu número é maior que o número secreto!\n")
        elif (menor):
            print("Você ERROU! O seu número é menor que o número secreto!\n")
        pontos_perdidos = abs(num_secreto - num_escolhido)
        pontos = pontos - pontos_perdidos
        
print("Fim do jogo! Você fez {} pontos!".format(pontos))
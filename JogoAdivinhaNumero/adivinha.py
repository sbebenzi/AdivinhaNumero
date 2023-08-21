import random
def adivinhaNumero() :
    numeroSecreto = random.randint(1,100)
    tentativas = 0
    palpite = 0

    print("Bem vindo ao jogo Adivinhe o número!!")
    print("Tente adivinhar o numero de 1 - 100.")

    while palpite != numeroSecreto :
        try:
            palpite = int(input("Digite seu palpite:"))
        except:
            print("Digite um número válido")
            continue

        tentativas += 1

        if palpite < numeroSecreto :
            print("Seu palpite foi menor do que o numero que eu estou pensando... Tente novamente:")

        elif palpite > numeroSecreto :
            print("Seu palpite foi maior do que o numero que eu estou pensando... Tente novamente:")

    print("Parabéns Voce acertou!!!")    

adivinhaNumero();
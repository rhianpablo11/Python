#coding utf-8
import random
random.seed()
x = random.randrange(1,2)
confirmar = "sim"
chances = 3
print(f"bem vindo ao meu jogo de adivinhação ")
while chances >0:
    print(f"voce tem {chances} ainda disponiveis")
    num = int(input("digita um num"))
    if num == x:
        print("voce acertou")
        break
    else:
        print("voce errou")
        if x>num:
            print("o num q tu botou era menor")
        else:
            print("o num era maior")
        chances -=1

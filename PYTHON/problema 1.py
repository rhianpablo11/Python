#conding utf-8
print("bem vindo ao nosso ambiente, aqui diremos a sua faixa etária em que você se enquadra")
nome = input("Qual o nome da vossa senhoria?")
idade = int(input("Qual a sua idade?"))
if idade <0:
    print("idade nao pode ser negativa")
elif idade<=12:
    print(f"tu, {nome}, ainda é criança")
elif idade<=19:
    print(f"tu, {nome}, é adolescente")
elif idade<=49:
    print(f"tu, {nome}, é adulto")
elif idade<=64:
    print(f"tu, {nome}, é coroa")
elif idade<=65:
    print(f"o sr, {nome}, já é idoso")
else:
    print("vai comprar o corolla se n tiver")
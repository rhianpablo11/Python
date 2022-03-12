# coding utf-8
print("A gasolina na minha cidade custa R$4,00.")
preco = float(input("quanto custa na sua cidade?"))
if preco <0:
    print("O valor não pode ser negativo")
elif preco > 4.0:
    print("Está acima da média")
elif preco < 4.0:
    print("Está abaixo da média.")
else:
    print("Está igual")
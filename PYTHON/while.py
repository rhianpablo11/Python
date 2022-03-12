#coding utf-8
i=1
while i>100:
    print(f"R${i},00 é seu saldo atual, Rhian Pablo")
    i+=50
print("fim da lista")
continuar = "sim"
while continuar.lower() =="sim":
    idade = int(input("Qual a sua idade?"))
    print(f"então você nasceu em:{2022-idade}")
    continuar = input("Deseja consultar novamente?")
print("foi bom ter vc por aq")
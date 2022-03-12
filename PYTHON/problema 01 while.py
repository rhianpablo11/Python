# coding: utf-8
i = int(input("Qual número vc deseja fazer a contagem inicial?"))
o = int(input("qual o número que vc deseja finalizar a contagem?"))
if i<o:
    while i <= o:
        print(i)
        i += 1
else:
    while i>=o:
        print(i)
        i -= 1
print("Fim da listagem")
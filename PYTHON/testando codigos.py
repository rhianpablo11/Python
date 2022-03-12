#coding utf-8
numeros = []
print("Para parar o programa basta digitar 0 e ele vai emitir os resultados finais")
get_numb = float(input("Digite numeros para alimentar o programa"))
if get_numb != 0:
    numeros.append(get_numb)
while get_numb != 0:
    get_numb = float(input("Digite numeros para alimentar o programa"))
    if get_numb != 0:
        numeros.append(get_numb)
tam_lista = len(numeros)
lista_neg = []
lista_pos = []
for itens in numeros:
    if itens < 0:
        lista_neg.append(itens)
    if itens > 0:
        lista_pos.append(itens)
tam_lista_pos = len(lista_pos)
tam_lista_neg = len(lista_neg)

porcentagem_pos = (tam_lista_pos / tam_lista) * 100
porcentagem_neg = (tam_lista_neg / tam_lista) * 100
print("o porcentual de numeros posivos que voce digitou foi de %2.2f " %porcentagem_pos)
print("o porcentual de numeros negativos que voce digitou foi de %2.2f " %porcentagem_neg)
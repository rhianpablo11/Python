#coding utf-8
print("Para parar o programa, digite -1")
f_exercicios = int(input("Qual a frequencia de pratica de exercicios praticadas?\n"
                         "0 -nunca \n 1 -poucas vezes \n 2 -muitas vezes"))
lista_pessoas = []
nunca = []
poucas_vezes = []
muitas_vezes = []
lista_pessoas.append(f_exercicios)
while f_exercicios != -1 and f_exercicios == 0 or f_exercicios == 1 or f_exercicios == 2:
    f_exercicios = int(input("Qual a frequencia de pratica de exercicios praticadas?\n"
                             "0 -nunca \n 1 -poucas vezes \n 2 -muitas vezes"))
    if f_exercicios != -1:
        lista_pessoas.append(f_exercicios)

for respostas in lista_pessoas:
    if respostas == 0:
        nunca.append(respostas)
    if respostas == 1:
        poucas_vezes.append(respostas)
    if respostas == 2:
        muitas_vezes.append(respostas)
print(len(lista_pessoas))
print((len(nunca) / len(lista_pessoas)) * 100)
print((len(poucas_vezes) / len(lista_pessoas)) * 100)
print(((len(muitas_vezes)) / len(lista_pessoas)) * 100)
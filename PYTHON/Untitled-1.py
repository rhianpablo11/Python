# coding: utf-8
print("ola!")
nome = input("fala ai teu nome maluco")
idade = int(input("diz ai tua idade para eu saber um a parada aq"))
print(f"seja bem vindo pivete(a){nome} , com idade de:{idade}anos")
print("seja bem vindo pivete(a){} , com idade de:{}anos" .format(nome, idade))
a = 4
c = 555
b = 4.55
print(f"numeros: {a}")
print("numeros: %6d" %(a))
print(f"num: {c:9}")
print(f"num:{b: .6f}")
print("num: %5.10f" %(b))
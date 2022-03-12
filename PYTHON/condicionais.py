# conding utf-8
nome=input("qual o seu nome?")
idade = int(input("qual a tua idade?"))
print(f"Olá amigo,{nome}")
lingprogramado = input("quer saber em qual linguagem eu fui programado?")
if lingprogramado.lower() == "sim":
    print("Eu fui programado em python")
if lingprogramado.lower() == "nao":
    print(f"entao vá se lascar {nome} e")
print("o preço medio da gasosa no br é 5 reais")
preco = float(input("qual o preço da gasosa na sua city?"))
if preco >5.0:
    print("preço está mais caro hein, muda de cidade")
if preco <5.0:
    print("preço ta barato vou me mudar p ai")
if preco == 5:
    print("entao ta normal")
if nome> "Rhian":
    print("se armava na chmada do colegio")
if nome<"Rhian":
    print("tinha q chegar cedo no colegio ne nego")
if idade >=18 and idade <=70:
    print("vocÊ é obrigado a votar ja seu corno")
if idade <18 or idade >70:
    print("nem pode votar ai ainda mijao")
print("tenha um ótimo dia")
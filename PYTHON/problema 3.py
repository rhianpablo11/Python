# coding utf-8
print("Seja bem-vindo a calculadora do Rhian")
valor_1 = float(input("Qual o primeiro valor da operação"))
valor_2 = float(input("QUal o segundo valor da operação?"))
print("Escolha uma das operações abaixo:")
print("1) soma\n2)subtração\n3)multiplicação\n4)divisão")
operacao = int(input("Insira o NÚMERO correspondente a operação desejada"))
if operacao == 1:
    print(f"O resultado é: {valor_1+valor_2}")
elif operacao == 2:
    print(f"O resultado é: {valor_1-valor_2}")
elif operacao == 3:
    print(f"O resultado é: {valor_1*valor_2}")
elif operacao == 4:
    if valor_2 == 0:
        print(f"O segundo valor digitado impossibilitará a divisão, logo ela não ocorrerá")
    if valor_2 != 0:
        print(f"O resultado é: {valor_1/valor_2}")
else:
    print("Operação inválida")
n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um número inteiro: "))

print("Qual operação você deseja realizar;")
print("Informe soma(+), subtração (-), multiplicação (*) e divisão(/)")
operacao = input()
resultado = 0

if operacao == "+":
    resultado = n1 + n2

elif operacao == "-":
    resultado = n1 - n2

elif operacao == "*":
    resultado = n1 * n2

elif operacao == "/":
    resultado = n1 / n2

else:
    print("Valor invalido!")

print(f"O valor da operação é: {resultado}")

consumo = int(input("Informe o consumo(kWh) de energia: "))
print("Informe o tipo de instalação:")
instalacao = (input("Residencial(R), Indrustrial(I) e Comercial(C)"))

if instalacao == "R":
    if consumo <= 500:
        valor = consumo * 0.756221
    elif consumo > 500:
        valor = consumo * 0.65

elif instalacao == "I":
    if consumo <= 1000:
        valor = consumo * 0.55
    elif consumo > 1000:
        valor = consumo * 0.60

elif instalacao == "C":
    if consumo <= 5000:
        valor = consumo * 0.756221
    elif consumo > 5000:
        valor = consumo * 0.60

else:
    print("Valor invalido!")

print(f"O valor a pagar R$ {valor:6.2f}")

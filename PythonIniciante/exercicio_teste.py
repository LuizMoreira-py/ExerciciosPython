salario = float(input("Digite um valor para calculo de aumento de salário: "))

percentual = 0

if salario > 1250:
    percentual = 10
    aumento = (salario * percentual / 100)
    novoSalario = salario + aumento

if salario <= 1250:
    percentual = 15
    aumento = (salario * percentual / 100)
    novoSalario = salario + aumento

print(f"O aumento de salário é de R${aumento:6.2f}")
print(f"O novo salário é de R${novoSalario:6.2f}")

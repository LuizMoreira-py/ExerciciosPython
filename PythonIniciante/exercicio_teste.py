# Escreva um programa que calcule o resto da divisão inteira entre dois
# números.
# # Utilize apenas as operações de soma e subtração para calcular o resultado.

cont = 1
dividendo = int(input("Informe um número inteiro para o dividendo: "))
divisor = int(input("Infome um número inteiro para o divisor: "))

while True:
    print(f"{cont}° divisão: {dividendo} - {divisor}")
    dividendo = dividendo - divisor
    resto = dividendo
    cont += 1
    if resto <= divisor:
        print(f"Resto = {resto}")
        break

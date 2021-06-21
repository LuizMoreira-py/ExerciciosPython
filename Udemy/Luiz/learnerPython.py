numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número digitado é par!")
    elif numero % 2 == 1:
        print("O número digitado é impar!")
else:
    print("O valor digitado não é inteiro!")

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número digitado é par!")
    elif numero % 2 == 1:
        print("O número digitado é impar!")
else:
    print("O valor digitado não é inteiro!")

horas = input("Digite somente a hora do seu relógio: ")

if horas.isdigit():
    horas = int(horas)
    if horas <= 11:
        print("Bom dia!")
    elif horas >= 12 and horas <= 17:
        print("Boa tarde!")
    elif horas >= 18 and horas <= 23:
        print("Boa noite!")
    else:
        print("Valor invalido")

nome = input("Digite o seu nome: ")
caracteres = len(nome)

if caracteres <= 4:
    print("Seu nome é muito curto!")
elif caracteres > 4 and caracteres <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")

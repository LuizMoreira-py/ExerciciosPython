num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num1.isdigit() and num2.isdigit():
    print("Os números digitados são inteiros, pode somar")
    num1 = int(num1)
    num2 = int(num2)

    def soma(num1, num2):
        return num1 + num2
    print(soma(num1, num2))
else:
    print("Não pode converter os números")

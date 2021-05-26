# Escreva um programa que leia um número e verifique se é ou não um
# número primo. Para fazer essa verificação, calcule o resto da
# divisão do número por 2 e depois por todos os números ímpares
# até o número lido. Se o resto de uma dessas divisões for igual zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único
# número primo que é par.

x = 0
numero = int(input())
resto = numero % 2

if numero == 2:
    print(f"O número {numero} é primo")

else:
    while x < numero:
        if x % 2 == 1:
            divisao = numero % x
        x += 1

    if divisao % x != 0:
        print(f"O número {numero} é primo")

    else:
        print(f"O número {numero} não é primo")

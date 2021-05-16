# Escreva um programa que leia números inteiros do teclado. O programa deve
# ler os números até que o usuário digite 0 (zero). No final da execução,
# exiba a quantidade de números digitados como a soma e a média aritmética.

soma = 0
contador = 0
media = 0

while True:
    numeros = int(input("Digite um número inteiro: "))
    if numeros == 0:
        break
    soma += numeros
    contador += 1
media = soma // contador

print(f"Total de números digitados: {contador}")
print(f"Soma dos números digitados: {soma}")
print(f"Média dos números digitados: {media}")

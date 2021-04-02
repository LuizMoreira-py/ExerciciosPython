# Escreva um programa que pergunte a distância
# que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para
# viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distracia = float(input("Informe a distância(KM) que deseja percorrer: "))
preco = 0

if distracia <= 200:
    preco = 0.50

else:
    preco = 0.45

custo = distracia * preco
print(f"Valor total: R$ {custo:6.2f}")

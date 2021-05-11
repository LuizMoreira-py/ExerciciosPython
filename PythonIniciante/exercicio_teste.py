mes = 0
total = 0.0

taxa = float(input("Valor da taxa(%): "))

while mes <= 23:
    depositoMensal = float(input("Deposito mensal: R$ "))

    rendimentoPeriodo = (depositoMensal * taxa) * mes

    total = total + depositoMensal
    rendimentoTotal = total + rendimentoPeriodo

    mes += 1
    print(f"Mês {mes} ---- Rendimento periodo: R$ {rendimentoPeriodo:6.2f} ---- Rendimento total: {rendimentoTotal:6.2f}")

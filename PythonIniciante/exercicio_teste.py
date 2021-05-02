mes = 0

deposito = float(input("Valor do depósito: R$ "))
taxa = float(input("Valor da taxa(%): "))

rendimento = deposito * taxa

while mes <= 23:
    rendimentoPeriodo = (deposito * taxa) * mes
    rendimentoTotal = deposito + rendimentoPeriodo
    mes += 1
    print(f"Mês {mes} ---- Depósito: R$ {deposito:6.2f} ---- Rendimento: R$ {rendimento:6.2f} ---- Rendimento periodo: R$ {rendimentoPeriodo:6.2f} ---- Rendimento total: {rendimentoTotal:6.2f}")

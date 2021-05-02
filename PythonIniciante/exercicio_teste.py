mes = 0

deposito = float(input())
taxa = float(input())

rendimento = deposito * taxa

while mes <= 23:
    rendimentoPeriodo = (deposito * taxa) * mes
    mes += 1
    print(f"Mês {mes} Depósito: R$ {deposito} Rendimento: R$ {rendimento} Rendimento periodo: R$ {rendimentoPeriodo}")

total = deposito + rendimentoPeriodo
print(f"Total: R$ {total}")

deposito = float(input("Digito o valor do depósito: R$ "))
taxa = float(input("Digite o valor da taxa: R$ "))



mes = 0
total = deposito * taxa

while mes <= 24:
    juros = total * mes    
    mes += 1
    print(f"Mês {mes} Deposito {deposito} Rendimento {juros}")

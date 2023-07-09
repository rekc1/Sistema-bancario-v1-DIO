menu = 0
Limite_Saque = 3
valor_maximo_saque = 500
saldo = 700
extrato = ""
saques_realizados = 1

while menu != 4:
    menu = int(input(" [1] Depósitar\n [2] Sacar\n [3] Consultar Extrato\n [4] Sair\n R:"))

    if menu == 1:
        valor = float(input("Quanto você deseja depósitar?: "))
        saldo += valor
        extrato = extrato + f" Depósito: R$ {valor} /"
        print("Depósito realizado com sucesso!")
    elif menu == 2:
        if saques_realizados <= Limite_Saque:
            valor = float(input("Quanto você deseja sacar?: "))
            if valor <= valor_maximo_saque:
                if valor <= saldo:
                    saldo -= valor
                    extrato = extrato + f" Saque: R$ {valor} /"
                    print("Saque realizado com sucesso!")
                    saques_realizados += 1
                else:
                    print("Não foi possível realizar o saque por falta de saldo!")
            else:
                print(f"Não é possível fazer saques superiores á {valor_maximo_saque}!")
        else:
            print("Número limite de saques excedido!")
    elif menu == 3:
        print(f"Extrato: {extrato}")
        print(f"Saldo: {saldo}")

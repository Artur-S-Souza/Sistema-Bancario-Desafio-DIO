menu = """
## Sistema Bancário - Desafio DIO##
#             1- Sacar            #
#           2- Depositar          #
#            3- Extrato           #
#             0- Sair             #
###################################
"""

extrato = ""
saques = 0
SAQUES_DIARIOS = 3
limite_saque = 500
saldo = 0

while True:
    print(menu)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if saques >= SAQUES_DIARIOS:
            print("Número máximo de saques diários atingido.")
        elif saques < SAQUES_DIARIOS:
            saque = float(input("Digite o valor do saque: "))
            if saque > saldo:
                print("Saldo insuficiente.")
            elif saque > limite_saque:
                print(f"Límite de saque não permitido, seu límite é de R$ {limite_saque:.2f}.")
            elif saque <= limite_saque:
                saldo -= saque
                saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            continue
    elif opcao == "2":
        deposito = float(input("Digite o valor do depósito: "))
        while deposito == 0:
            print("Valor de deposito inválido, tente novamente.")
            deposito = float(input("Digite o valor do deposito: "))
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")

    elif opcao == "3":
        if not extrato:
            print("Nenhuma transação realizada.")
        else:
            print("Extrato:")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break

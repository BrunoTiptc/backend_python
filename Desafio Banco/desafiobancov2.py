menu = """

[c] Criar usuário
[t] Criar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Funções
def saque(saldo=0, extrato="", limite=500, numero_saques=0, limite_saques=3):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def deposito(saldo=0, extrato=""):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo=0, extrato=""):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF (apenas números): ")
    endereco = input("Informe o endereço: ")
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    print(f"Usuário {nome} criado com sucesso!")
    return usuario

def criar_conta_corrente(usuario):
    numero_conta = input("Informe o número da conta: ")
    agencia = input("Informe a agência: ")
    conta_corrente = {
        "numero_conta": numero_conta,
        "agencia": agencia,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "limite": 500,
        "numero_saques": 0,
        "limite_saques": 3
    }
    print(f"Conta corrente {numero_conta} criada com sucesso!")
    return conta_corrente

# Variáveis iniciais
saldo = 0
extrato = ""
limite = 500
numero_saques = 0
limite_saques = 3

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(saldo, extrato, limite, numero_saques, limite_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "c":
        usuario = criar_usuario()
        
    elif opcao == "t":
        if 'usuario' in locals():
            conta_corrente = criar_conta_corrente(usuario)
        else:
            print("Você precisa criar um usuário primeiro.")

    elif opcao == "q":
        print("Saindo... Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

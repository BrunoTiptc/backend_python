menu = """

[1] Depositar
[2] Sacar
[3] Extrato 
[4] Sair 

=> """

saldo = 0
limite = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0
while True:
    
    opçao = input(menu)
    
    if opçao == "1":
        valor = float(input("Informe o valor do deposito:  "))
        
        if valor > 0: 
            saldo += valor 
            extrato += f"\nDepósito: R${valor:.2f}"
            print ("Deposito bem sucessido! seu saldo agora é R${:.2f}, e esse é o seu extrato:{}".format(saldo, extrato))
        elif valor <= 0:
            print ("Voce digitou um valor negativo") 
                  
    elif opçao == "2":
        saque = float(input("Digite o quanto voce vai sacar: "))
        saldo -= saque
        extrato += f"\nSaque: R${saque:.2f}"
        print ("Saque bem sucessido! seu saldo agora é R${:.2f}, e esse é o seu extrato: {}".format(saldo, extrato))
        
    elif opçao == "3":
        print("extrato: {}".format(extrato))
             
    elif opçao == "4":
        break
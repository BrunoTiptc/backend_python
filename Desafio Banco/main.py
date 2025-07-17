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
valor = 0
deposito = 0

while True:
    
    opçao = input(menu)
    
    if opçao == "1":
        print("\n Deposito \n")
        deposito = float(input("Digite o quanto voce vai depositar:"))
        if deposito > 0: 
            saldo += deposito 
            extrato += f"\nDeposito: R${deposito:.2f}\n"
            print ("Deposito bem sucessido! seu saldo agora é R${:.2f}, e esse é o seu extrato:{}".format(saldo, extrato))
        elif deposito <= 0:
            print ("Voce digitou um valor negativo")
           
    elif opçao == "2":
        print("\n sacar \n")
      
    elif opçao == "3":
        print("Extrato")
        
    elif opçao == "4":
        break
# Conjunto de domínios válidos
regras = {"gmail.com", "outlook.com", "yahoo.com"}

# Entrada do usuário
email = input().strip()

# Verifica se há exatamente um @ no e-mail
if email.count("@") == 1:
    usuario, dominio = email.split("@", 1)
    if usuario and dominio in regras:
        print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")

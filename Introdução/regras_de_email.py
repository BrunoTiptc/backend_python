# Entrada do usuário
email = input().strip()

# Conjunto com os domínios permitidos
regras = {
    "gmail.com",
    "outlook.com",
    "yahoo.com"
}


# TODO: Verifique as regras do e-mail:
if "@" in email:
    usuario, dominio = email.split("@", 1)
    if dominio in regras:
        print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")

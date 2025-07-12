# Conhecendo metodos uteis da classe string 

curso = "pYtHon"
curso1 = "    Python  "

print(curso.upper())     # converte para maiusculo

print(curso.lower())     # converte para minusculo

print(curso.title())     # so a primeira maiusculo

print(curso1.strip())     # remove espaco vazio da esquerda e direita

print(curso1.lstrip())     # remove espaco vazio da esquerda 

print(curso1.rstrip())     # remove espaco vazio da direita

# juncoes e centralizacao 

print (curso.center(10,"#"))   # vai manter centralizado a string e vai adicioanr mais os caracteres que falta ate 10

print(".".join(curso))  # join e parecido com for , ele vai passar item por item, e cada incrementacao vai ser um "."
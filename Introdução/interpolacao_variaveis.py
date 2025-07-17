# 3 tipos de formatacao
'''
Old style % 
por porcentagem
'''
nome = "Bruno"
idade = 29
profissao = "Engenheiro de Software"
linguagem = "Python"

print(" \n Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s. \n" %(nome, idade, profissao, linguagem))

# metodo format 
print(" \n Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}. \n ".format(nome, idade, profissao, linguagem))

# metodo format pelo indice
print(" \n Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}. \n ".format(linguagem, profissao, idade, nome))

# direto
print(" \n Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. \n ")


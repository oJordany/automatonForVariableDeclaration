# import string
# lista = {"a","b","c","d","e"}

# conjunto = {"c","l","f", "d", "g", "h", "1", "4"}

# LUC = lista.union(conjunto)

# dif = LUC.difference(lista)

# print(set(sorted(conjunto)))
import re
string = "teste, um, dois,   tres    ;"
lista = [nome.strip() for nome in string.split(",")]
lista[-1] = re.sub(r"\s+;", ";", lista[-1])
print(lista)

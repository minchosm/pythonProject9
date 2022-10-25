entradaPaises = input("Introduce los paises separados por comas: ")
conjunto = set(entradaPaises.split(', '))
lista = sorted(list(conjunto))
x = 1
for items in lista:

    print(f"{x}º país: {items} ")
    x += 1

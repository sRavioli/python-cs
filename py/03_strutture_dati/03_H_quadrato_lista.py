# Ottenere una lista che abbia al suo interno tutti i quadrati dei numeri che
# vanno da 1 a 10


def square_list():
    lst = list(range(1, 11))
    squared_list = [i**2 for i in lst]
    return print(squared_list)


square_list()


# soluzione del professore
# usando un ciclo
# def quadrato(numero):
#     return numero**2


# output = []
# for i in range(1, 11):
#     output.append(quadrato(i))

# print(output)

# usando una list comprehension
# output = [quadrato(i) for i in range(1, 11)]
# print(output)

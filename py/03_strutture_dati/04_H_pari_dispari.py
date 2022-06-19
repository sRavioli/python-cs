# Ottenere una lista che abbia la stringa pari in corrispondenza dei numeri
# pari, mentre quella dispari in corrispondenza dei numeri dispari, per tutti i
# numeri che vanno da 1 a 10.

# modificando la lista di base
def even_odd_overwrite():
    lst = list(range(1, 11))
    for i in lst:
        if i % 2 == 0:
            lst[i - 1] = f"{i} - even"
        else:
            lst[i - 1] = f"{i} - odd"
    return print(lst)


even_odd_overwrite()


# creando una nuova lista
def even_odd_new():
    lst = list(range(1, 11))
    even_odd_lst = []
    for i in lst:
        if i % 2 == 0:
            even_odd_lst.append(f"{i} - even")
        else:
            even_odd_lst.append(f"{i} - odd")

    return print(even_odd_lst)


even_odd_new()


# soluzione del professore
# con un ciclo
# output = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         output.append("pari")
#     else:
#         output.append("dispari")

# print(output)

# usando una list comprehension
# output = ["pari" if i % 2 == 0 else "dispari" for i in range(1, 10)]
# print(output)

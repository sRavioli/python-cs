# Scriviamo una funzione che iteri fino a che il valore associato ad un
# contatore intero è minore di 10. Usiamo un ciclo `while``.


def count_ten():
    # crea contatore
    i = 0
    while i < 10:
        # incrementa contatore
        i += 1
        # stampa contatore
        print(i)


# chiama funzione
count_ten()


# soluzione del professore
# def itera_while():
#     i = 0
#     while i < 10:
#         i = i + 1
#         print("{}-ma iterazione".format(i))


# itera_while()


# È possibile parametrizzare la funzione
# def count_ten_param(j):
#     while j < 10:
#         j += 1
#         print(j)


# count_ten_param(5)

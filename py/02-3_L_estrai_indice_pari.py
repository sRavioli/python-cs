# Estraiamo tutti gli indici pari di una lista arbitraria di dieci elementi in
# ordine inverso. Per farlo, usiamo sia la funzione `range` sia lo slicing.


def extract_even_slice(lst):
    if len(lst) != 10:
        error = "List must contain 10 elements"
        return print(error)
    else:
        even_lst = lst[-2::-2]
        return print(even_lst)


extract_even_slice(list(range(10)))


# soluzione del professore
# def estrai_con_slice(lista):
#     if len(lista) != 10:
#             print('Errore!')
#             return []
#     else:
#             return lista[-2::-2]

# def estrai_con_range(lista):
#     if len(lista) != 10:
#         print('Errore!')
#         return []
#     else:
#         l_out = []
#         for i in range(8, -1, -2):
#             l_out.append(lista[i])
#         return l_out

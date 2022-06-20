# Scriviamo una funzione che restituisca il prodotto riga per colonna di due
# vettori `v1` e `v2`. Usiamo una list comprehension, e verifichiamo che la
# lunghezza dei due vettori sia coerente. Valutiamo inoltre il tempo necessario
# all'esecuzione. Il metodo dovrà funzionare indipendentemente dall'ordine in
# cui sono passati i parametri.
#
# Provare ad effettuare la stessa operazione in NumPy.

import numpy as np
from time import time


# https://math.stackexchange.com/questions/2567679/product-between-a-column-vector-and-a-row-vector
def row_col_product(a: np.ndarray, b: np.ndarray) -> np.ndarray:

    # verifica che entrambi gli array siano bidimensionali (`barry`) e che
    # una delle due dimensioni sia pari a $1$ (per confermare che siano dei
    # `barry` riga/colonna)
    if (min(a.shape) or min(b.shape)) != 1:
        raise ValueError(
            f"One (or both) vector has too many rows/columns (a: {min(a.shape)}, b: {min(b.shape)})"
        )

    result = []  # lista nulla da convertire in array
    # le `barry.shape` sono `(1, n)` o viceversa. L'indice `m` è la
    # `barry.ndim` minore dei due array, utile per selezionare correttamente
    # gli elementi dell'array
    for m in range(1):
        for i in range(max(a.shape)):
            partial = []  # lista nulla che funge da riga (da riempire)

            for j in range(max(b.shape)):
                # verifica quale array sia riga/colonna poiché gli elementi da
                # utilizzare per il prodotto cambiano a seconda dell'ordine
                # degli array di input.
                if a.shape[0] == 1:
                    res = a[m][j] * b[i][m]
                else:
                    res = a[i][m] * b[m][j]

                partial.append(res)  # aggiunge il prodotto alla lista riga
            result.append(partial)  # aggiunge la riga alla lista principale
    return np.array(result)  # converte la lista di liste in array


a = np.array([[1, 2, 3]])
b = np.array([[4], [5], [6]])

start = time()
print(row_col_product(a, b))
print(row_col_product(b, a))  # otterremo lo stesso risultato
stop = time()
print(stop - start)

# tutta questa operazione la si può effettuare tramite numpy:
# print(a * b)
# print(b * a)


# soluzione del professore
# Ecco una possibile soluzione:

# from time import time
# import numpy as np
#
# def riga_per_colonna(v1, v2):
#     tic = time()
#     if v1.shape[0] == 1:
#         if v2.shape[1] == 1 and v1.shape[1] == v2.shape[0]:
#             prod = sum([v1[0][i] * v2[i] for i in range(v2.shape[0])])
#     elif v2.shape[0] == 1:
#         if v1.shape[1] == 1 and v2.shape[1] == v1.shape[0]:
#             prod = sum([v1[i] * v2[0][i] for i in range(v1.shape[0])])
#     else:
#         return 'Le dimensioni non sono coerenti!'
#     toc = time()
#     return prod, toc - tic
#
# v1 = np.array([[1,2,3,4]])
# v2 = np.array([[1],[2],[3],[4]])
#
# res = riga_per_colonna(v1, v2)
# res = riga_per_colonna(v2, v1)
# res = riga_per_colonna(np.array([[1]]), v2)
#
# L'equivalente operazione in NumPy è data da:
# res = v1 * v2 # in realtà è data da np.dot(v1, v2)

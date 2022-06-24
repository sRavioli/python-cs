# Scriviamo la funzione `rettifica(array)`, che restituisce un array delle
# stesse dimensioni di quello in ingresso ma che porta tutti i valori negativi
# a `0`.

import numpy as np


def rectification(arry: np.ndarray) -> np.ndarray:
    arry[arry < 0] = 0
    return arry


a = np.array([[1, 2, 3], [-4, 5, -6], [7, -8, 9]])
print(rectification(a))


# soluzione del professore
# def rettifica(array):
#     array[array < 0] = 0
#     return array

# rettifica(np.array([-1, 2, -3, 4]))

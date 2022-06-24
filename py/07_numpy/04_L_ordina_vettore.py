# Scriviamo la funzione `asort(vect)` che restituisce un vettore riga ordinato
# in modo discendente.

import numpy as np


def asort(vector: np.ndarray) -> np.ndarray:
    sorted_vector = np.sort(vector)
    return sorted_vector[::-1]


v = np.array([1, 6, 7, 3, 4, 2, 9, 8, 5])
print(asort(v))


# soluzione del professore
# def asort(array):
#     s = np.sort(array)
#     return s[-1::-1]

# asort(np.array([3, 2, 5, -1]))

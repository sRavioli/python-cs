# Scriviamo la funzione `inverti_se_invertibile(mat)` che, data una matrice
# bidimensionale, restituisca l'inversa soltanto se `mat` è bidimensionale,
# quadrata, e il determinante sia diverso da zero. Usare esclusivamente le
# istruzioni `if`.

import numpy as np


def inv_if_invertible(mtrx: np.ndarray) -> np.ndarray:
    if mtrx.ndim != 2:
        raise ValueError("Matrix is not 2-dimensional")

    if mtrx.shape[0] != mtrx.shape[1]:
        raise ValueError("Matrix is not square")

    if np.linalg.det(mtrx) == 0:
        raise ValueError("Matrix determinant is 0, thus not invertible")

    return np.linalg.inv(mtrx)


mtrx = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
print(inv_if_invertible(mtrx))


# soluzione del professore
# def inverti_se_invertibile(mat):
#     if len(mat.shape) == 2 \
#         and mat.shape[0] == mat.shape[1] \
#         and linalg.det(mat) != 0:
#         return linalg.inv(mat)
#     raise ValueError('La matrice passata non è invertibile.')

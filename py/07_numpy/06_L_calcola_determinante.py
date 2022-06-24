# Scriviamo la funzione `calcola_determinante(mat)` che permetta di calcolare
# il determinante di una matrice 2×2 **senza** usare l'apposita funzione NumPy.

import numpy as np


def calc_determinant(mtrx: list) -> float:
    # controlla che matrice sia quadrata 2x2
    if (len(mtrx), len(mtrx[0]), len(mtrx[0])) != (2, 2, 2):
        raise ValueError("Matrix must be of 2×2 type!")

    det = (mtrx[0][0] * mtrx[1][1]) - (mtrx[0][1] * mtrx[1][0])
    return det


mtrx = [[1, 2], [3, 4]]
print("det:", calc_determinant(mtrx))
print("np.linalg.det:", np.linalg.det(mtrx))


# soluzione del professore
# def calcola_determinante(mat):
#     if len(mat.shape) == 2 and (mat.shape[0] == mat.shape[1]) and mat.shape[0] == 2:
#         return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
#     raise ValueError("La matrice non ha le dimensioni attese.")

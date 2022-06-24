# Verificare che il prodotto tra una matrice invertibile e la sua inversa sia
# la matrice identità.

import numpy as np


def check_prod(mtrx: np.ndarray) -> bool:
    inv_mtrx = np.linalg.inv(mtrx)
    prod = mtrx * inv_mtrx
    if np.array_equal(np.eye(3), prod):
        return True


mtrx = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
print(check_prod(mtrx))


# soluzione del professore
# import numpy as np
#
# mat = np.array([[5, 0, 1], [0, 2, 2], [0, 0, 3]])
# mat_inv = np.linalg.inv(mat)
# np.eye(3) == mat.dot(mat_inv)

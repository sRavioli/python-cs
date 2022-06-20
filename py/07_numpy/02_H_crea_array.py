# Scriviamo una funzione `crea_array(dim_1, dim_2, val_min, val_max)` che crei
# array di dimensioni arbitrarie `dim_1×dim_2` fatti di numeri interi
# casuali compresi tra `val_min` e `val_max`. Di default, la funzione dovrà
# creare dei vettori riga.
#
# Provare ad effettuare la stessa operazione in NumPy.

import numpy as np
from random import randint


def make_array(shape: tuple, vmin: int, vmax: int) -> np.ndarray:
    arry = [
        [randint(vmin, vmax) for i in range(shape[0])]
        for j in range(shape[1])
    ]
    return np.array(arry)


print(make_array((5, 2), 2, 10))


# Scriviamo la funzione `descrivi(array)` che permette di descrivere un array
# in termini non parametrici, individuando mediana, deviazione standard e range
# interquartile (ovvero tra il 25-percentile ed il 75-percentile).

import numpy as np


def describe_arr(array: np.ndarray) -> None:
    median = f"median:\t\t{np.median(a)}\n"
    std = f"standard dev:\t{np.std(a)}\n"
    iqr = f"iqr:\t\t{np.percentile(a, 75) - np.percentile(a, 25)}\n"

    return f"{median}{std}{iqr}"


a = np.array([3, 5, 3, 2, 1, 8])
print(describe_arr(a))

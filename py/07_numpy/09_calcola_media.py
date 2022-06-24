# Scriviamo la funzione `calcola_media(array, pesi)` che restituisce il valor
# medio di un array; usiamo una lista. Il parametro `pesi` è opzionale; nel
# caso sia lasciato il valore opzionale (lista vuota), la media sarà
# aritmetica; in caso contrario, verifichiamo la coerenza delle dimensioni dei
# vettori e restituiamo la media pesata.


def calc_mean(array: list, weights: list = None) -> float:
    if weights is None:
        return sum(array) / len(array)

    if len(weights) != len(array):
        raise ValueError("Array and weights must have the same length")

    return sum([weights[i] * array[i] for i in range(len(array))]) / sum(weights)


a = [5, 4, 5]
b = [0, 1, 0]
c = [0, 1]

print(calc_mean(a))
print(calc_mean(a, b))
# print(calc_mean(a, c))


# soluzione del professore
# def calcola_media(array, pesi=[]):
#     if pesi == []:
#         return sum(array) / len(array)
#     else:
#         if len(pesi) == len(array):
#             return sum([(pesi[i] * array[i]) for i in range(len(array))])
#     raise ValueError("La lunghezza dei pesi non corrisponde a quella degli array.")


# print(calcola_media([5, 4, 5]))
# print(calcola_media([5, 4, 5], [0, 1, 0]))
# calcola_media([5, 4, 5], [0, 1])

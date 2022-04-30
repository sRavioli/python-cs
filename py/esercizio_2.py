# funzione che iteri finché cond bool falsa. usiamo ciclo for. maz 100 iterazioni. si può usare random

import random as rnd

# while rnd.randint(0, 1) != 1:
#     for i in range(100):
#         print(i)


def itera():
    for elemento in range(100):
        if rnd.randint(0, 10) > 5:
            print("continuo")
        else:
            print("esco")
            break


itera()

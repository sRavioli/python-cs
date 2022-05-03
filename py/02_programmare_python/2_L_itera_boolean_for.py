# Scriviamo una funzione che iteri fino a che una condizione booleana non è
# `False`. Usiamo un ciclo `for`, ponendo come numero massimo di iterazioni 100
# e se necessario, usando il metodo `random.randint(a, b)`.

# importa random, genera numeri casuali
import random as rnd


def iterate_bool_for():
    for i in range(100):  # for loop, massimo 100 iterazioni
        condition = rnd.randint(0, 20) < 15  # condizione booleana
        if condition:  # se vera
            print(f"{i + 1} - Continuing")
        else:
            print(f"{i + 1} - Exiting")
            break  # esci dal ciclo
    return condition


iterate_bool_for()


# compact version
def iterate_compact():
    for i in range(100):
        if rnd.randint(0, 20) < 10:  # condizione booleana
            print(f"{i + 1} - Continuing")
        else:
            print(f"{i + 1} - Exiting")
            break


# iterate_compact()


# soluzione del professore. È stato sostituto il nome della variable `eval` con
# `evaluate` dato che la prima è una parola riservata.
# def itera_for():
#     cond = True
#     for i in range(100):
#         evaluate = rnd.randint(-10, 10)
#         print("Valuto numero {}".format(evaluate))
#         if evaluate < 0:
#             print("Esco")
#             cond = False
#             return cond
#         else:
#             print("Continuo")
#     return cond


# itera_for()

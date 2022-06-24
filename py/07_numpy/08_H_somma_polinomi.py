# Scriviamo la funzione `somma_polinomi(pol_1, pol_2)` che permetta di sommare
# due polinomi di grandezza arbitraria.

from numpy.polynomial import Polynomial


def add_polys(p: list, q: list) -> Polynomial:
    if len(p) > len(q):
        for coef in range(len(p) - len(q)):
            q.append(0)
    elif len(q) > len(p):
        for coef in range(len(q) - len(p)):
            p.append(0)

    return Polynomial([p[i] + q[i] for i in range(len(p))])


p = [3, 2, 1]  # = x**2 + 2x + 3
q = [3, 2]  # 2x + 3
r = [3, 5, 6, 2]  # 2x**3 + 6x**2 + 5x + 3

print(add_polys(p, q))  # 6.0 + 4.0 x**1 + 1.0 x**2
print(add_polys(p, r))  # 6.0 + 7.0 x**1 + 7.0 x**2 + 2.0 x**3


# soluzione del professore
# def somma_polinomi(pol_1, pol_2):
#     if len(pol_1) < len(pol_2):
#         while len(pol_1) < len(pol_2):
#             pol_1.insert(0, 0)
#     elif len(pol_2) < len(pol_1):
#         while len(pol_2) < len(pol_1):
#             pol_2.insert(0, 0)
#     return [(pol_1[i] + pol_2[i]) for i in range(len(pol_1))]

# somma_polinomi([0, 1, 2], [2, 2, 1])
# somma_polinomi([1, 2], [2, 2, 1])
# somma_polinomi([1, 2], [2, 2, 2, 1])

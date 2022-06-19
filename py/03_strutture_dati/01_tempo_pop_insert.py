# Proviamo a valutare il tempo necessario alle operazioni di `insert` e `pop`
# su una coda in Python usando la libreria `time`. Confrontiamo il risultato
# ottenuto con quello ottenibile implementando una coda come una struttura di
# tipo `deque` e usando gli opportuni metodi `appendleft()` e `popleft()`.

import time as t
from collections import deque


def time_list(lst: list, num: int) -> None:
    t1_insert = t.time()
    lst.insert(0, num)
    t2_insert = t.time()
    t_insert = t2_insert - t1_insert

    t1_pop = t.time()
    lst.pop()
    t2_pop = t.time()
    t_pop = t2_pop - t1_pop

    return f"insert: {t_insert}\npop: {t_pop}"


def time_deque(lst: list, num: int) -> None:
    dqq = deque(lst)

    t1_appendleft = t.time()
    dqq.appendleft(num)
    t2_appendleft = t.time()
    t_appendleft = t2_appendleft - t1_appendleft

    t1_popleft = t.time()
    dqq.popleft()
    t2_popleft = t.time()
    t_popleft = t2_popleft - t1_popleft

    return f"appendleft: {t_appendleft}\npopleft: {t_popleft}"


lst = list(range(100_000_000))

print(time_list(lst, 1))
print(time_deque(lst, 1))


# soluzione del professore
#
# from time import time
# from collections import deque
#
# def queue(queue, pushed=1):
#     tic = time()
#     queue.insert(0, 4)
#     queue.pop()
#     toc = time()
#     return tic, toc
#
# def queue_con_deque(queue, pushed=1):
#     tic = time()
#     queue.appendleft(pushed)
#     queue.popleft()
#     toc = time()
#     return tic, toc
# Proviamo a chiamare le due funzioni:
#
#
# queue = list(range(10000000))
# queue_d = deque(queue)
#
# queue_classica(queue)
# queue_con_deque(queue_d)

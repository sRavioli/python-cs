# Creare un metodo che raddoppi una lista passata come argomento in ingresso.
# Provare ad utilizzare un ciclo `for` e ricordare la differenza tra `shallow`
# e `deep copy`.


def double_list(lst):
    for i, element in enumerate(lst):
        lst[i] = element * 2
    return lst


print(double_list(["a", "b", "c"]))
print(double_list([1, 2, 3, 4]))


# soluzione del professore

# Potremmo essere tentati di scrivere una funzione come la seguente:
#
# def raddoppia_lista(lista):
#     for elemento in lista:
#         lista.append(elemento)
#         print(f"Lista all'iterazione attuale: {lista}")
#
#
# Proviamo a chiamare questa funzione; avremo subito un output ingestibile.
# Ciò è legato al fatto che Python è fermo in un loop infinito: il metodo
# agisce sulla lista originaria, che ad ogni iterazione del ciclo "ingloba" un
# altro elemento, provocando di conseguenza un aumento delle dimensioni della
# lista e, quindi, un'ulteriore iterazione, e così via all'infinito.
#
# Possiamo però ottenere il risultato che ci serve usando il metodo deepcopy:
#
# from copy import deepcopy
#
# def raddoppia_lista_deep(lista):
#     lista_appoggio = deepcopy(lista)
#     for elemento in lista_appoggio:
#         lista.append(elemento)
#         print(f"Lista di appoggio: {lista_appoggio}")
#         print(f"Lista attuale: {lista}")
#
#
# In questo caso, stiamo creando un'altra variabile, chiamata lista_appoggio,
# che sarà utilizzata come "buffer" per aggiungere alla lista originaria gli
# elementi relativi a sé stessa. Provando a chiamare questo codice otterremo
# il risultato desiderato:
#
# >>> raddoppia_lista_deep([1, 2])
# Lista di appoggio: [1, 2]
# Lista attuale: [1, 2, 1]
# Lista di appoggio: [1, 2]
# Lista attuale: [1, 2, 1, 2]

# estraiamo tutti gli indici pari in una lista abritraria di 10 elementi in ordine inverso.
# per farlo, usiamo la funzione range e lo slicing

def get_index():
    ll = list(range(10))
    print(ll)
    print(ll[-2::-2])

get_index()

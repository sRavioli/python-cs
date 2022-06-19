# Scrivere una dict comprehension che permetta di ottenere il dizionario
# `vecchio_o_giovane` dato il seguente dizionario:
#
# dizionario = {
#     'Jax Teller': 27,
#     'Walter White': 52,
#     'Billy Butcher': 41,
#     'Luke Skywalker': 79,
#     'Bobby Singer': 68,
#     'Johnny Lawrence': 49
# }
#
# In particolare, il dizionario `vecchio_o_giovane` avrà le stesse chiavi del
# dizionario di partenza, a cui sarà associato il valore `'giovane'` soltanto
# se il valore della chiave del dizionario di partenza è inferiore a `65`.


dct = {
    "Jax Teller": 27,  # giovane
    "Walter White": 52,  # giovane
    "Billy Butcher": 41,  # giovane
    "Luke Skywalker": 79,  # vecchio
    "Bobby Singer": 68,  # vecchio
    "Johnny Lawrence": 49,  # giovane
}

old_or_young = {
    key: "giovane" if value < 65 else "vecchio" for key, value in dct.items()
}

print(old_or_young)


# soluzione del professore
#
# vecchio_o_giovane = {
#     k: 'vecchio' if v > 65 else 'giovane' for (k, v) in dizionario.items()
# }
#
# Nota
# Per iterare sul dizionario originale, usiamo il metodo `items()` che, come
# visto in precedenza, ci restituisce un oggetto di tipo `dict_items` il quale
# è, per l'appunto, iterabile.

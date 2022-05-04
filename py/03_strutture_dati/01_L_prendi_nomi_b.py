# Selezioniamo tutti i nomi che iniziano con la lettera B dalla seguente lista:
# "Jax Teller", "Walter White", "Billy Butcher", "Luke Skywalker",
# "Bobby Singer", "Johnny Lawrence".

names = [
    "Jax Teller",
    "Walter White",
    "Billy Butcher",
    "Luke Skywalker",
    "Bobby Singer",
    "Johnny Lawrence",
]


def get_b_names(lst):
    b_names = [name for name in lst if name[0] == "B"]
    return print(b_names)


get_b_names(names)


# soluzione del professore
# Usando un ciclo:
# output_for = []
# for nome in names:  # `lista_nomi` sostituito con `names`
#     if nome[0] == "B":  # `nomi` sostituito con `nome`
#         output_for.append(nome)

# print(output_for)

# usando una list comprehension:
# `lista_nomi` sostituito con `names`
# output = [nome for nome in names if nome[0] == "B"]
# print(output)

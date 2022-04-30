name_list = [
    "Jax Teller",
    "Walter White",
    "Billy Butcher",
    "Luke Skywalker",
    "Bobby Singer",
    "Johnny Lawrence"
]

# def starts_w_B(name):
#     condition = (name[0] == "B")
#     return condition


def get_B_name(name_list):
    b_name_list = [name for name in name_list if name[0] == "B"]
    return b_name_list

print(get_B_name(name_list))

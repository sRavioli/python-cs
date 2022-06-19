# Utilizzare il pattern matching per stampare a schermo la parola "Vero" se il
# valore di una variabile è True, e "Falso" altrimenti.

def match_case(boolean):
    match boolean:
        case True:
            result = "Vero"
        case False:
            result = "Falso"

    return result

print(match_case(True))
print(match_case(False))


# soluzione del professore
# def match_case(true_or_false):
#     match true_or_false:
#         case True:
#             return "Vero"
#         case False:
#             return "Falso"



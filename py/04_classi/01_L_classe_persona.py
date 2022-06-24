# Scrivere una classe `Persona` applicando i concetti visti durante la lezione.

import argparse


class Persona:
    # il type hinting (`variabile: tipo`) suggerisce all'utente che tipo di
    # variabile inserire nella funzione. Con `...) -> None:` si suggerisce che
    # la funzione non abbia alcun valore di `return`.
    #
    # Attraverso il metodo `__init__()`, le variabile inserire nella funzione
    # vengono inizializzate, diventando i parametri della classe
    def __init__(self, nome: str, cognome: str, età: int = 18) -> None:
        #              ^^^^^^^^^
        #
        # se cambiassimo il nome della variabile evidenziata, dovremmo cambiare
        # anche il nome nell'istruzione `self.nome = ...` sostituendo a `...`
        # il nuovo nome della variabile.

        self.nome = nome  # <- dovremmo cambiare qui
        self.cognome = cognome
        self.età = età

    # per modificare il valore di una variabile, è necessario accedervi. Altri
    # linguaggi utilizzerebbero una sintassi di questo tipo:
    #
    # def get_età(self):
    #    return self.età
    #
    # def set_età(self, età):
    #     self.età = value
    #
    # per modificare i valori delle variabili devo accedervi. Vogliamo, ad
    # esempio "ringiovanire" di default tutte le persone. Usiamo un
    # modificatore. Altri linguaggi utilizzerebbero una sintassi del genere:
    #
    # def get_età(self):
    #    return self.età
    #
    # def set_età(self, età):
    #   self.età = value
    #
    # Python invece utilizza le `@property`. Per recuperare il valore
    # dell'istanza:
    @property
    def età(self):
        return self.__età

    # Per inserire un setter scriviamo:
    @età.setter
    def età(self, value):
        if value < 0:
            # "solleva" un errore nel caso l'età sia negativa
            raise ValueError("L'età non può essere negativa")
        self.__età = value  # per "ringiovanire" `value - 1`

    # creiamo il metodo `ringiovanisci()`
    def ringiovanisci(self):
        self.età = self.età - 1

    # creiamo un (finto) codice fiscale (CF). Il procedimento per creare un CF
    # è sempre lo stesso, ma il risultato è differente. Possiamo usare uno
    # `@staticmethod`:
    @staticmethod
    def calcola_codice_fiscale(nome, cognome, età):
        return nome + cognome + str(età)

    # il metodo `__str__()` viene chiamato quando stampiamo la singola istanza
    def __str__(self):
        return f"{self.nome} – {self.cognome}"


# possiamo usare il pacchetto `argparse` per inserire i dati quando eseguiamo
# lo script da riga di comando:
def crea_persona(args):
    p = Persona(args.nome, args.cognome)
    print(p)  # stampiamo l'istanza


# creiamo una funzione da richiamare in main per creare il parser di argomenti:
def my_parser():
    parser = argparse.ArgumentParser()  # creiamo il parser

    # aggiungiamo argomenti
    parser.add_argument("-n", "--nome", help="Nome", default="Ciccio")
    parser.add_argument("-c", "--cognome", help="Cognome", default="Cappuccio")

    # facciamo il parse degli argomenti
    args = parser.parse_args()

    # li consegniamo alla funzione creata in precedenza
    crea_persona(args)


# creiamo la funzione principale, `main()`, che è quella che eseguiremo
def main():
    my_parser()

    p = Persona("Ciccio", "Cappuccio")
    cf = Persona.calcola_codice_fiscale("Ciccio", "Cappuccio", 18)
    print(f"codice fiscale: {cf}")

    print(f"pre-ringiovanimento: {p.età}")
    p.ringiovanisci()
    print(f"post-ringiovanimento: {p.età}")

    print(p)

    # p.età = -5  # otterremo un errore dato che l'età è negativa


# Python fa uso di script, moduli e packages:
# - SCRIPT: sono i file .py che eseguiamo;
# - MODULI: sono i file .py che importiamo in altri file .py;
# - PACKAGES: sono delle cartelle di moduli.

# controlliamo che il nome del file sia "__main__". In questo modo la funzione
# `main()` verrà eseguita solo se il file viene eseguito direttamente (script)
# e non quando verrà importato come modulo in un altro file .py
if __name__ == "__main__":
    main()


# soluzione del professore
# Scriviamo la classe Persona come segue:
#
# class Persona():
#
#     def __init__(self, nome, cognome, eta):
#         self.nome = nome
#         self.cognome = cognome
#         self.eta = eta
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @nome.setter
#     def nome(self, value):
#         if len(value) < 2:
#             raise ValueError(
#             'La lunghezza del nome non può essere inferiore a due caratteri.'
#             )
#         else:
#             self.__nome = value
#
#     @property
#     def cognome(self):
#         return self.__cognome
#
#     @cognome.setter
#     def cognome(self, value):
#         if len(value) < 2:
#             raise ValueError(
#          'La lunghezza del cognome non può essere inferiore a due caratteri.'
#             )
#         else:
#             self.__cognome = value
#
#     @property
#     def eta(self):
#         return self.__eta
#
#     @eta.setter
#     def eta(self, value):
#         if value < 0:
#             raise ValueError("L'età non può essere negativa.")
#         else:
#             self.__eta = value
#
# Alcune note:
# - abbiamo riscritto la classe Persona in modo da trasformare tutti gli
#   attributi in proprietà;
# - per ogni proprietà, abbiamo specificato un getter, che restituisce il
#   valore della stessa;
# - oltre al getter, è stato specificato un setter, nel quale vi è anche una
#   forma di validazione del valore passato in input.
#
# Vediamo come usare la nostra nuova classe:
#
# ```
# >>> draco = Persona("Draco", "Malfoy", 12)
# >>> print(draco.nome)
# Draco
# >>> print(draco.eta)
# 12
# >>> hermione = Persona("", "Granger", 18)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in __init__
#   File "<stdin>", line 12, in nome
# ValueError: La lunghezza del nome non può essere inferiore ai 2 caratteri
# ```
#
# Notiamo che, dal punto di vista dello script che richiama la classe, non ci
# sono differenze di sorta; tuttavia, la logica di validazione ci permette di
# evitare errori e situazioni incoerenti, ed è inoltre possibile sfruttare le
# proprietà per accedere agli attributi privati della classe.

# Scrivere una classe `Persona` applicando i concetti visti durante la lezione.

import argparse


class Persona:
    # utilizziamo il type hinting: `var: type`
    # con `-> None` suggeriamo che la funzione non abbia un valore di return
    def __init__(self, nome: str, cognome: str, età: int = 18) -> None:
        # il metodo `__init__()` è usato per inizializzare i vari parametri
        # della classe
        #
        # nel caso in cui scrivessimo `cog: str` nell'argomento di `__init__()`
        # anziché `cognome: str` e non modificassimo `self.cognome = cognome`
        # in `self.cognome = cog`, l'interprete ci restituirà un errore.

        self.nome = nome
        self.cognome = cognome
        self.età = età

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
    # per "ringiovanire" di default scriveremo `self.età = value - 1`. Python
    # permette di non utilizzare questa sintassi facendo uso delle `@property`:
    @property
    def età(self):
        return self.__età

    # con la sintassi precedente recuperiamo il valore dell'istanza. Per
    # inserire un setter scriviamo:
    @età.setter
    def età(self, value):
        if value < 0:
            raise ValueError("L'età non può essere negativa")

        self.__età = value  # per ringiovanire `value - 1`

    # creiamo il metodo `ringiovanisci()`
    def ringiovanisci(self):
        self.età = self.età - 1

    # vogliamo, ad esempio, creare un codice fiscale (CF). Il procedimento per
    # creare il CF è sempre lo stesso, ma il risultato è differente. Possiamo
    # usare uno `@staticmethod`:
    @staticmethod
    def calcola_codice_fiscale(nome, cognome, età):
        return nome + cognome + str(età)  # non creiamo un vero CF, ovviamente

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

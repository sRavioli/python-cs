# scrivere una classe "Persona" applicando i concetti visti durante la lezione

import argparse


class Persona:

    # il valore che mi aspetto è "None"
    def __init__(self, nome: str, cognome: str, eta: int = 18) -> None:
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        # questi sono i parametri del metodo __init__. se chiamassimo cognome
        # `cog`, e lasciassimo invariato `self.cognome = cognome`, python
        # restituirà un errore

    # per modificare nome, cognome e età devo per forza accedervi
    # mettiamo che voglio ringiovanire tutte le persone di default
    # usiamo un modificatore. altri linguaggi avrebbero

    # def get_eta(self):
    #     return self.eta

    # def set_eta(self, value):
    #     self.eta = value

    # per ringiovanire di default basta fare `self.eta = value - 1`. python ci
    # permette di evitare questa notazione con le proprietà

    @property
    def eta(self):
        return self.__eta

    # così recupero il valore dell'istanza. per inserire un setter faccio:

    @eta.setter
    def eta(self, value):
        if value < 0:
            raise ValueError("Vedi che l'eta è negativa")
        self.__eta = value - 1

    def ringiovanisci(self):
        self.eta = self.eta - 1

    # usiamo `@staticmethod` per creare il CF, procedimento uguale ma CF diverso
    @staticmethod
    def calcola_codice_fiscale(nome, cognome, eta):
        return nome + cognome + str(eta)

    def __str__(self) -> str:
        return f"{self.nome} - {self.cognome}"


# per usare `argparse`
def crea_persona(args):
    p = Persona(args.nome, args.cognome)
    print(p)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nome", help="Nome della persona", default="Ciccio")
    parser.add_argument(
        "-c", "--cognome", help="Cognome della persona", default="Cappuccio"
    )
    args = parser.parse_args()
    crea_persona(args)

    p = Persona("Ciccio", "Cappuccio")
    cf = Persona.calcola_codice_fiscale("Ciccio", "Cappuccio", 18)
    print(cf)

    # p.ringiovanisci()
    print(p.eta)
    print(p)

    # p.eta = -5 # throws an error, eta negativa

# gli argomenti opzionali vanno sempre in coda


# python ha script, moduli e package
# - script si eseguono
# - moduli si importano
# - package sono cartelle di moduli

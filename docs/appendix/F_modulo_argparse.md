# Appendice F – Il modulo `argparse`

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<a name="top"></a>

<!-- TOC -->

1. [Appendice F – Il modulo `argparse`](#appendice-f--il-modulo-argparse)

<!-- /TOC -->

</details>

Il modulo `argparse` permette di inserire degli argomenti da passare al nostro
script Python mediante riga di comando.

Per farlo, dobbiamo seguire un processo articolato in quattro step:

1. creiamo un oggetto di classe `ArgumentParser`;
2. aggiungiamo gli argomenti di cui intendiamo fare il parsing;
3. effettuiamo il parsing di questi argomenti;
4. usiamo gli argomenti per chiamare il metodo opportuno

Vediamo un esempio.

Supponiamo di avere una classe `Persona`, e di voler scrivere uno script per
creare un oggetto di questa classe mediante riga di comando. Potremo scrivere:

```py
from argparse import ArgumentParser

class Persona():
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f'{self.nome} {self.cognome}'


def run(args):
    # Definiamo il metodo `run()` che sarà invocato ad ogni esecuzione dello
    # script. Il metodo accetta un parametro `args` che rappresenta gli
    # argomenti di cui è stato effettuato il parsing.

    p = Persona(args.nome, args.cognome)
    print(p)


def main():
    # Step 1: creiamo un oggetto di classe `ArgumentParser`
    parser = ArgumentParser()

    # Step 2: aggiungiamo due argomenti al parser
    parser.add_argument(
        '-n',                        # abbreviazione per invocare l'argomento
        '--nome',                    # nome completo dell'argomento
        help='Nome della persona',   # messaggio di aiuto per l'argomento
        default='Pippo',             # valore di default dell'argomento
    )
    parser.add_argument(
        '-c',
        '--cognome',
        help='Cognome della persona',
        required=True               # l'argomento non può essere omesso
    )

    # Step 3: facciamo il parsing degli argomenti
    args = parser.parse_args()   # gli argomenti saranno salvati in args

    # Step 4: passiamo gli argomenti al metodo run
    run(args)


if __name__ == '__main__':
    main()
```

Proviamo a salvare questo script in un file `run.py`, ed eseguiamolo usando la
notazione abbreviata:

```sh
$ python run.py -n Nome -c Cognome
Nome Cognome
```

Possiamo anche omettere il nome, ma non il cognome, in quanto è un parametro
richiesto:

```sh
$ python run.py -c Cognome
Pippo Cognome
```

Possiamo poi invocare l'help scrivendo:

```sh
$ python run.py -h
usage: run.py [-h] [-n NOME] -c COGNOME

optional arguments:
  -h, --help            show this help message and exit
  -n NOME, --nome NOME  Nome della persona
  -c COGNOME, --cognome COGNOME
                        Cognome della persona
```

Proviamo infine ad utilizzare la notazione completa:

```sh
$ python run.py --nome Nome --cognome Cognome
Nome Cognome
```

Proviamo adesso a modificare la classe `Persona` inserendovi l'età. In tal
senso, specifichiamo che l'età deve essere un valore intero; qualora questo non
avvenga, sarà lanciata un'eccezione.

```py
class Persona():
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, value):
        if not isinstance(value, int):
            raise ValueError("Fornire un intero per l'età.")
        self._eta = value

    def __str__(self):
        return f'{self.nome} {self.cognome}, {self.eta}'
```

Modifichiamo il resto dello script per adattarci alle nuove esigenze. Partiamo
dal metodo `run()`:

```python
def run(args):
    # Definiamo il metodo `run()` che sarà invocato ad ogni esecuzione dello
    # script. Il metodo accetta un parametro `args` che rappresenta gli
    # argomenti di cui è stato effettuato il parsing.

    p = Persona(args.nome, args.cognome, args.eta)
    print(p)
```

Aggiungiamo poi un altro argomento al `parser`:

```python
def main():
    # Step 1: creiamo un oggetto di classe `ArgumentParser`
    parser = ArgumentParser()

    # Step 2: aggiungiamo due argomenti al parser
    parser.add_argument(
        '-n',                        # abbreviazione per invocare l'argomento
        '--nome',                    # nome completo dell'argomento
        help='Nome della persona',   # messaggio di aiuto per l'argomento
        default='Pippo',             # valore di default dell'argomento
    )
    parser.add_argument(
        '-c',
        '--cognome',
        help='Cognome della persona',
        required=True               # l'argomento non può essere omesso
    )
    parser.add_argument(
        '-e',
        '--eta',
        help='Età della persona'
    )

    # Step 3: facciamo il parsing degli argomenti
    args = parser.parse_args()      # gli argomenti saranno salvati in args

    # Step 4: passiamo gli argomenti al metodo run
    run(args)


if __name__ == '__main__':
    main()
```

Proviamo ad eseguire di nuovo lo script:

```sh
$ python run.py -n Nome -c Cognome -e 18
Traceback (most recent call last):
  File "~\run.py", line 61, in <module>
    main()
  File "~\run.py", line 57, in main
    run(args)
  File "~\run.py", line 30, in run
    p = Persona(args.nome, args.cognome, args.eta)
  File "~\run.py", line 9, in __init__
    self.età = età
  File "~\run.py", line 18, in età
    raise ValueError("Age is not an integer")
ValueError: Age is not an integer
```

Vedremo che viene lanciato un errore, in quanto gli argomenti passati mediante
`argparse` sono normalmente interpretati come delle stringhe.

Per risolvere questo problema dovremo specificare il parametro `type`,
ponendolo ad `int`:

```python
parser.add_argument(
    '-e',
    '--eta',
    help='Età della persona',
    type=int
)
```

Se proviamo ad eseguire nuovamente lo script non riscontreremo alcun errore:

```sh
$ python run.py -n Nome -c Cognome -e 18
Nome Cognome, 18
```

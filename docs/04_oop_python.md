# 04 – Programmazione orientata agli oggetti in Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [04 – Programmazione orientata agli oggetti in Python](#04--programmazione-orientata-agli-oggetti-in-python)
   1. [La programmazione orientata agli oggetti](#la-programmazione-orientata-agli-oggetti)
   2. [Classi](#classi)
      1. [Metodi e attributi](#metodi-e-attributi)
2. [Classi in Python](#classi-in-python)
   1. [Il metodo `__init__()`](#il-metodo-__init__)
   2. [Modificatori di accesso](#modificatori-di-accesso)
   3. [Metodi](#metodi)

<!-- /TOC -->

</details>

Python offre un supporto esteso alla programmazione orientata agli oggetti
(_Object-Oriented Programming_ in inglese). Prima di proseguire sarebbe
opportuno introdurre brevemente questo concetto

## La programmazione orientata agli oggetti

Quello della _programmazione orientata agli oggetti_ (OOP per brevità) è un
paradigma di programmazione che permette di creare dei nuovi tipi definiti
dall'utente, questi sono complementari ai tipi definiti dal linguaggio di
programmazione. In tal senso, la OOP sposta il _focus_ dalle **funzioni**,
che sono centrali in linguaggi come il C o nel paradigma procedurale, ai
**dati**.

È per questo motivo che si arriva a dire che nella OOP tutto è un oggetto.

## Classi

Una classe è un _prototipo_ per un determinato tipo di dati, definito
dall'utente. Ad esempio:

- la Classe `Studente` rappresenta tutte le proprietà e le azioni associate ad
  uno studente;
- la Classe `Auto` rappresenta tutte le proprietà e le azioni associate ad
  un'auto;
- la Classe `Motore` definisce tutti i comportamenti dei motori;

e via discorrendo.

In generale può esistere una classe per ogni tipologia di oggetti presenti nel
mondo, sia esso reale o informatico.

È **_molto importante_** non confondere la classe con il singolo oggetto
chiamato **istanza**. Ad esempio:

- lo studente "Angelo Cardellicchio" è un'istanza della classe `Studente`;
- l'auto "Opel Corsa", targata "AB 123 CD" è un'istanza della classe `Auto`;
- l'auto "Hyundai Tucson", targata "CD 321 AB" è un'istanza della classe `Auto`;
- l'auto "Opel Corsa", targata "AA 123 CC" è un'altra istanza della classe
  `Auto`;

### Metodi e attributi

Ogni classe ha dei _metodi_, che caratterizzano le azioni le quali possono
essere usate su ogni istanza della classe stessa, e degli _attributi_, ovvero le
caratteristiche dell'istanza.

In particolare, ogni nuovo tipo, chiamato Classe, avrà opportuni attributi e
metodi, ognuno dei quali sarà accessibile dall'esterno mediante opportuni
modificatori.

Ad esempio, l'auto "Opel Corsa", targata "AA 123 CD" ha una casa costruttrice
(Opel), un modello (Corsa), una targa (AB 123 CD), una cilindrata, etc.

# Classi in Python

Per definire una classe in Python, usiamo la parola chiave `class`:

```python
class NomeClasse:
  # Metodi e Attributi della classe
  pass
```

Possiamo creare una classe a partire da un'altra classe utilizzando il concetto
di ereditarietà:

```python
class ClasseFiglia(ClasseMadre):
  pass
```

La classe `ClasseFiglia`, discende dalla classe `ClasseMadre` e ne eredita tutti
i metodi e gli attributi.

## Il metodo `__init__()`

La maggior parte dei linguaggi di programmazione prevede un costruttore per
creare un'istanza di una classe. Python, tuttavia, non lo prevede; fa uso invece
di un metodo di inizializzazione dei singoli attributi dell'istanza. Da questo
deriva il nome del metodo, `__init__()`:

```python
class NomeClasse(ClasseMadre):
    def __init__(self, *args, **kwargs):
        self.arg_1 = arg_1
        # ...
```

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Con la sintassi `*args` e `**kwargs` vogliamo rappresentare l'azione di
> unpacking di (rispettivamente) una lista ed un dizionario, mediante la quale
> stiamo passando tutti i valori contenuti all'interno della sequenza.
>
> </details>

Prestiamo particolare attenzione alla _keyword_ `self`, che permette di
riferirsi alla specifica istanza di una classe (concettualmente simile al
`this` del C++). Ad esempio:

```python
class Persona(object):
    def __init__(self, nome, cognome, età=18):
        self.nome = nome
        self._cognome = cognome
        self.__età = età
```

Evidenziamo quattro punti dal codice precedente:

1. la classe generica `object`, da cui derivano **tutte** le classi di Python.
   Non è necessario dichiararlo;
2. il funzionamento della parola chiave `self`, che permette di associare agli
   attributi della singola istanza un determinato valore;
3. la possibilità di inserire tra i parametri dei valori opzionali di default,
   come ad esempio `18` per `età`;
4. la presenza di uno o due underscore `_` davanti ad alcuni attributi.

Approfondiamo brevemente il quarto punto.

## Modificatori di accesso

Python prevede l'utilizzo di modificatori di accesso ai dati. Nell specifico
abbiamo i classici `public`, `protected` e `private`. Tuttavia, a differenza di
altri linguaggi, per distinguere tra i tre modificatori di accesso si utilizzano
rispettivamente zero, uno o due underscore come suffisso al nome dell'attributo.
Nel nostro caso:

```python
class Persona(object):
    def __init__(self, nome, cognome, età=18):
        self.nome = nome          # Membro `public`
        self._cognome = cognome   # Membro `protected`
        self.__età = età          # Membro `private`
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Nonostante il modificatore di accesso è comunque possibile accedere ai membri
> protetti dall'esterno della classe. Infatti:
>
> ```pycon
> >>> p = Persona("Jax", "Teller")
> >>> p.nome
> 'Jax'
> >>> p._cognome
> 'Teller'
> >>> p.__età
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> AttributeError: 'Persona' object has no attribute '__età'
> ```
>
> E come è possibile constatare, questo non è valido per gli attributi privati
>
> </details>

Questa sintassi può ovviamente essere usata per definire dei metodi protetti
oppure privati.

## Metodi

La sintassi per definire un metodo di classe è analoga a quella usata per
definire una funzione:

```python
def metodo(self, *args, **kwargs):
    pass
```

Tuttavia è presente una fondamentale differenza: il primo attributo di un metodo
di classe è **_sempre_** un riferimento all'istanza tramite la parola chiave
`self`. Tale riferimento non va specificato quando il metodo viene chiamato
all'esterno della classe:

```python
p = Persona("Nome", "Cognome")   # `p` è un'istanza di `Persona`
p.metodo(parametro)              # richiamo il metodo dall'istanza
```

Usiamo l'operatore `.` per accedere ai metodi definiti all'interno delle classi,
in questo caso accediamo a `metodo` della classe `Persona`.

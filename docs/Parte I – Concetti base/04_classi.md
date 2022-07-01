# 04 – Programmazione orientata agli oggetti in Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<a name="top"></a>

<!-- TOC -->

1. [04 – Programmazione orientata agli oggetti in Python](#04--programmazione-orientata-agli-oggetti-in-python)
   1. [La programmazione orientata agli oggetti (⮨)](#la-programmazione-orientata-agli-oggetti-)
   2. [Classi (⮨)](#classi-)
      1. [Metodi e attributi (⮨)](#metodi-e-attributi-)
   3. [Classi in Python](#classi-in-python)
      1. [Il metodo `__init__()` (⮨)](#il-metodo-__init__-)
      2. [Modificatori di accesso (⮨)](#modificatori-di-accesso-)
   4. [Metodi](#metodi)
      1. [Metodi di classe (⮨)](#metodi-di-classe-)
      2. [Metodi statici (⮨)](#metodi-statici-)
      3. [Metodi astratti (⮨)](#metodi-astratti-)
   5. [Le proprietà (⮨)](#le-proprietà-)

<!-- /TOC -->

</details>

Python offre un supporto esteso alla programmazione orientata agli oggetti
(_Object-Oriented Programming_ in inglese). Prima di proseguire sarebbe
opportuno introdurre brevemente questo concetto

## La programmazione orientata agli oggetti ([⮨](#top))

Quello della _programmazione orientata agli oggetti_ (OOP per brevità) è un
paradigma di programmazione che permette di creare dei nuovi tipi definiti
dall'utente, questi sono complementari ai tipi definiti dal linguaggio di
programmazione. In tal senso, la OOP sposta il _focus_ dalle **funzioni**,
che sono centrali in linguaggi come il C o nel paradigma procedurale, ai
**dati**.

È per questo motivo che si arriva a dire che nella OOP tutto è un oggetto.

## Classi ([⮨](#top))

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

Sostanzialmente creiamo una struttura dati che raggruppi le caratteristiche
generali di una classe. Quest'ultima è un'astrazione.

### Metodi e attributi ([⮨](#top))

Ogni classe ha dei _metodi_, che caratterizzano le azioni le quali possono
essere usate su ogni istanza della classe stessa, e degli _attributi_, ovvero le
caratteristiche dell'istanza.

In particolare, ogni nuovo tipo, chiamato Classe, avrà opportuni attributi e
metodi, ognuno dei quali sarà accessibile dall'esterno mediante opportuni
modificatori.

Ad esempio, l'auto "Opel Corsa", targata "AA 123 CD" ha una casa costruttrice
(Opel), un modello (Corsa), una targa (AB 123 CD), una cilindrata, etc.

## Classi in Python

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

### Il metodo `__init__()` ([⮨](#top))

La maggior parte dei linguaggi di programmazione prevede un costruttore per
creare un'istanza di una classe. Python, tuttavia, non lo prevede; fa uso invece
di un metodo di inizializzazione dei singoli attributi dell'istanza. Da questo
deriva il nome del metodo, `__init__()`:

```python
class NomeClasse(ClasseMadre):
    def __init__(self, *args, **kwargs):
        self.arg_1 = arg_1
        # ...
        pass
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

### Modificatori di accesso ([⮨](#top))

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

### Metodi di classe ([⮨](#top))

Il _decorator_ `@classmethod` ci permette di definire i _metodi di classe_:

```python
@classmethod
def builder_stringa(cls, strg: str):
    nome, cognome, eta = strg.split(" ")
    return Persona(nome, cognome, eta)
```

A differenza dei metodi standard, i metodi di classe hanno un riferimento alla
classe (`cls`) e non all'istanza (`self`). Questo significa che sono dei metodi
che si applicano all'intera classe e non alle singole istanze. Un tipico esempio
di utilizzato di metodo di classe è mostrato nel codice precedente, dove creiamo
un oggetto di classe `Persona` a partire da una stringa.

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Il metodo precedente è, di fatto, un'implementazioni del design pattern
> Builder.
>
> </details>

Per richiamare un metodo di classe occorre riferirsi al nome della classe
stessa e non alla singola istanza:

```pycon
>>> persona = Persona.builder_stringa("Bobby Munson 58")
>>> print(f"{persona.nome}, {persona._cognome}")
Bobby, Munson
```

### Metodi statici ([⮨](#top))

Mediante il decoratore `@staticmethod` possiamo definire un metodo _statico_. In
Python il funzionamento di un metodo di questo tipo è assimilabile al
comportamento di una funzione "semplice", definita però all'interno di una
classe e richiamabile su istanze della stessa. Ad esempio:

```python
@staticmethod
def nome_valido(nome):
    if len(nome) < 2:
        return False
    else:
        return True
```

È dunque possibile richiamare liberamente questo metodo con l'operatore `.` da
una singola istanza:

```pycon
>>> print(persona.nome_valido("Li"))
True
```

È possibile richiamarlo sulla classe stessa:

```pycon
>>> print(Persona.nome_valido("X"))
False
```

### Metodi astratti ([⮨](#top))

Possiamo definire dei metodi astratti mediante il decorator `@abstractmethod`.
Per farlo, la nostra classe deve ereditare metodi e attributi dalla classe `ABC`
(Abstract Base Class), contenuta nel package `abc`:

```python
from abc import ABC

class ClasseMadre(ABC):
    # ...

    @abstractmethod
    def metodo_da_sovrascrivere(self):
        pass
```

I metodi contrassegnati dal decorator `@staticmethod` dovranno essere
implementati nelle classi derivate (ovvero ne dovranno fare l'_override_):

```python
class ClasseFiglia(ClasseMadre):
    # ...

    def metodo_da_sovrascrivere(self):
        pass
```

## Le proprietà ([⮨](#top))

In molti linguaggi di programmazione si utilizzano dei metodi accessori
(_getter_) e modificatori (_setter_) rispettivamente per accedere e modificare
gli attributi delle istanze di una classe. Python non vieta di farlo: potremmo,
ad esempio scrivere un metodo `get_nome(self)` per accedere al nome di una
persona e un metodo `set_nome(self, nome)` per impostare la proprietà.

Tuttavia è presente una sintassi più compatta (e più _pythonic_) che fa uso del
decorator `@property`. Questo rappresenta una funzione a quattro parametri:

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

In particolare:

- `fget` è la funzione usata per **recuperare** il valore dell'attributo;
- `fset` è la funzione usata per **impostare** il valore dell'attributo;
- `fdel` è la funzione per **rimuovere** l'attributo;
- `doc` è la funzione per **documentare** e **descrivere** l'attributo.

Utilizzando `@property`, possiamo seguire le "best practices" della OOP,
rendendo privati gli attributi della classe e accedendovi mediante gli opportuni
metodi:

```python
class Persona():

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        if len(value) < 2:
            raise ValueError(
                    "La lunghezza del nome non può essere inferiore ai 2 caratteri"
                )
        else:
            self.__nome = value

    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, value):
        if len(value) < 2:
            raise ValueError(
                    "La lunghezza del cognome non può essere inferiore ai 2 caratteri"
                )
        else:
            self.__cognome = value

    @property
    def eta(self):
        return self.__eta

    @eta.setter
    def eta(self, value):
        if value < 0:
            raise ValueError("L'età non può essere negativa")
        else:
            self.__eta = value
```

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Vedi l'esercizio sulle classi per ulteriori spiegazioni.
>
> </details>

Alcune note:

- abbiamo riscritto la classe `Persona` in modo da trasformare tutti gli
  attributi in proprietà;
- per ogni proprietà, abbiamo specificato un _getter_ che restituisce il valore
  della stessa;
- per ogni proprietà, abbiamo specificato un _setter_, nel quale vi è anche una
  forma di validazione del valore di input.

Vediamo come usare la nostra nuova classe:

```pycon
>>> draco = Persona("Draco", "Malfoy", 12)
>>> print(draco.nome)
Draco
>>> print(draco.eta)
12
>>> hermione = Persona("", "Granger", 18)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __init__
  File "<stdin>", line 12, in nome
ValueError: La lunghezza del nome non può essere inferiore ai 2 caratteri
```

Notiamo che dal punto di vista dello script che richiama la classe, non sono
presenti grandi differenze. Tuttavia la validazione ci permette di evitare
errori e situazioni incoerenti, sfruttando inoltre le proprietà per accedere
agli attributi privati della classe.

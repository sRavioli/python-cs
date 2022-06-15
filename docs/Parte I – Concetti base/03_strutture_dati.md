# 03 – Strutture dati in Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [03 – Strutture dati in Python](#03--strutture-dati-in-python)
2. [Liste, pile e code](#liste-pile-e-code)
   1. [Pila](#pila)
   2. [Coda](#coda)
3. [List comprehension](#list-comprehension)
   1. [Forma estesa con `if` e `else`](#forma-estesa-con-if-e-else)
      1. [Perché usare le _list comprehension_?](#perché-usare-le-list-comprehension)
4. [Le _assignment expressions_](#le-assignment-expressions)
5. [Tuple](#tuple)
6. [Insiemi](#insiemi)
7. [Dizionari](#dizionari)
   1. [Chiavi e valori](#chiavi-e-valori)
   2. [Creazione di un dizionario non vuoto](#creazione-di-un-dizionario-non-vuoto)
      1. [Uso dell'operatore `{}`](#uso-delloperatore-)
      2. [Uso del costruttore `dict()`](#uso-del-costruttore-dict)
      3. [Uso della funzione `zip()`](#uso-della-funzione-zip)
      4. [Dict comprehension](#dict-comprehension)

<!-- /TOC -->

</details>

# Liste, pile e code

Python ci offre una grande varietà di metodi per gestire le liste; troviamo un
elenco esaustivo nella [documentazione ufficiale](https://docs.python.org/3.9/tutorial/datastructures.html#more-on-lists).

Grazie a questi metodi, è possibile costruire una pila o una coda in modo molto
più semplice rispetto ad altri linguaggi.

## Pila

Una pila (_stack_ in inglese) adotta una strategia di accesso ai dati del tipo
_Last-In_, _First-Out_ (LIFO). Questo significa che l'**_ultimo_** elemento che
viene aggiunto alla pila è il **_primo_** ad uscire dalla pila.

> <details open>
> <summary>ℹ️ <em>Esempio di pila</em></summary>
>
> Un tipico esempio di pila è quella dei piatti da lavare. Quasi sicuramente,
> il piatto in cima alla pila sarà l'ultimo che avremo preso dal tavolo;
> tuttavia, sarà anche il primo ad essere lavato.
>
> </details>

Per implementare una pila a partire da una lista possiamo usare due metodi:

- il metodo `.append()` che ci permette di inserire un nuovo elemento in cima
  alla pila (ovvero la posizione con indice `n - 1`, dove `n` è il numero di
  componenti);
- il metodo `.pop(pos)` che ci permette di estrarre un elemento in posizione
  `pos`. Se il valore di posizione `pos` non viene specificato, verrà estratto
  l'elemento in posizione `n - 1`.

Ad esempio:

```python
pl = [1, 2, 3]
pl.append(4)  # `pl` sarà pari a [1, 2, 3, 4]
rmvd = pl.pop(1)  # `rmvd` sarà pari a 4, `pl` sarà [1, 2, 3]
```

## Coda

Una coda (_queue_ in inglese) adotta una strategia di accesso ai dati del tipo
_First-In_, _First-Out_ (FIFO). In questo caso il primo elemento a uscire è
presente da più tempo in coda.

> <details open>
> <summary>ℹ️ <em>Esempio di coda</em></summary>
>
> Un tipico esempio di coda è quella che tutti quanti, prima o poi, abbiamo
> fatto alle Poste: il primo ad arrivare è il primo ad essere servito, poi il
> secondo, il terzo, e via così.
>
> </details>

Per implementare una coda a partire da una lista possiamo comunque usare i
metodi visti in precedenza con valore `pos` pari a `0`. Ad esempio:

```python
q = [1, 2, 3]
q.insert(0, 4)  # `q` sarà pari a [4, 1, 2, 3]
rmvd = q.pop(0)  # `rmvd` sarà pari a `4`, `q` sarà [1, 2, 3l]
```

Nonostante questo approccio si estremamente semplice, ha uno svantaggio: i
metodi `.insert()` e `.pop()` sono computazionalmente onerosi perché fanno in
modo di riallocare lo spazio occupato dagli elementi della lista.

In alternativa possiamo usare una struttura dati della libreria `collections`,
chiamata `deque`. La `deque` è progettata nello specifico per eseguire
efficientemente i metodi `.append()` e `.pop()` da entrambi i capi
struttura dati:

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(4)  # `d` sarà pari a [4, 1, 2, 3]
rmvd = d.popleft()   # `rmvd` sarà pari a 4, `d` sarà pari a [1, 2, 3]
```

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> La struttura dati `d` **_non_** è una lista ma una `deque`.
>
> </details>

# List comprehension

Una delle tecniche più usare per effettuare delle operazioni sugli elementi di
una lista è la **_list comprehension_**. Questa permette di sostituire quasi
completamente i classici cicli.

Le _list comprehension_ hanno una sintassi del tipo:

```python
lst_out = [func(elemento) for elemento in lst_in]
```

In altre parole otterremo in output una lista, `lst_out`, applicando ad ogni
elemento della lista lista originaria, `lst_in`, la funzione `func()`.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Sarebbe più opportuno parlare di iterabile di input e non di lista.
>
> </details>

## Forma estesa con `if` e `else`

Le _list comprehension_ possono anche includere delle istruzioni condizionali.
Un primo esempio è il seguente:

```python
lst_out_it = [func(elemento) for elemento in lst_in if condizione]
```

In questo caso la funzione `func()` verrà chiamata esclusivamente sugli elementi
che soddisfano la `condizione` indicata. Invece, se usassimo questa forma:

```python
lst_out_if_else = [f(elemento) if condizione else g(elemento) for elemento lst_in]
```

la funzione `f()` sarebbe invocata su tutti gli elementi che soddisfano la
`condizione`, mentre la funzione `g()` su tutti quelli che non la soddisfano.

### Perché usare le _list comprehension_?

Le _list comprehension_ sono utili e versatili. In molti casi, permettono di
sostituire i classici cicli con una sintassi più snella. Tuttavia, bisogna fare
attenzione a non abusare di questo strumento: si rischia di complicare
inutilmente il programma, rendendolo poco leggibile e mantenibile. In generale,
ricordiamo il **rasoio di Occam**: scegliere, tra più soluzioni possibili di un
problema, quella più semplice. Anche se è facile innamorarsi delle list
comprehension, è bene ricordarsi che anche i cicli sono leciti e funzionali.

# Le _assignment expressions_

Le list comprehension sono state pensate per approcci puramente iterativi. Di
conseguenza, risulta complesso implementare forme di ricorsione. Per ovviare a
questo inconveniente, Python ha introdotto dalla versione 3.8 le _assignment_
_expressions_.

Formalmente, una _assignment expression_ permette di **assegnare** e
**restituire** un valore all'interno di un'unica istruzione mediante il
**assignment expression operator**, chiamato anche _due punti uguale_. È stato
soprannominato il _walrus operator_ perché la sintassi `:=` ricorda gli occhi e
le zanne di un tricheco.

Vediamo un esempio:

```pycon
>>> walrus = False
>>> walrus
False
>>> (walrus := True)
True
>>> walrus
True
```

oppure:

```pycon
>>> print(tricheco := True)
True
```

Usiamo ora questo concetto per combinare ricorsione e list comprehension.
Definiamo i valori iniziali della [successione di Fibonacci](https://it.wikipedia.org/wiki/Successione_di_Fibonacci):

```pycon
>>> fib = [0, 1]
```

Usiamo una _assignment expression_ per ottenere una lista che come primo
elemento abbia il secondo elemento della lista precedente (quindi `1`) e come
secondo elemento la somma di tutti gli elementi della lista (quindi `0 + 1`):

```pycon
>>> (fib := [fib[1], fib[0] + fib[1]])
[1, 1]
```

L'operazione ha modificato il valore della lista `fib`. Ciò che però ci
interessa è soltanto la somma degli elementi precedenti della lista, quindi il
secondo valore ottenuto. Per isolarlo, possiamo usare l'operatore booleano
`and`:

```pycon
>>> (fib := [fib[1], fib[0] + fib[1]]) and fib[1]
2
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Otteniamo `2` perché ogni volta che viene usata la _assignment expression_,
> i valori di `fib` vengono aggiornati.
>
> </details>

Combiniamo i due passaggi precedenti e usiamo una list comprehension per
concatenare i risultati:

```pycon
>>> fib = [0, 1]
>>> fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1] for i in range(10)]
>>> fib
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

# Tuple

Le tuple permettono di rappresentare un insieme di valori di eterogenei,
separati da una virgola. Ad esempio:

```python
tpl = ("hello", "world", 12)
```

Come avviene per le liste, uno dei valori della tupla può essere un'altra tupla.
Ad esempio:

```python
tpl = ("hello", "world", (1, 2))
```

A differenza delle liste, le tuple sono immutabili. Questo però non implica che
non possano contenere al loro interno degli oggetti mutabili. Ad esempio:

```python
tpl = ("hello", "world", [1, 2, 3])
```

La tupla ha al suo interno due stringhe (immutabili) ed una lista (mutabile).
Modifichiamo la lista:

```python
tpl[2] = [2, 2, 3]
```

Otterremo un errore del genere:

```pycon
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Prevedibilmente, otteniamo un errore di assegnazione legato all'immutabilità
della tupla. Modifichiamo ora la lista:

```python
tpl[2][0] = 2   # `tpl` sarà `("hello", "world", [2, 2, 3])`
```

L'operazione è accettata e il risultato è quello atteso.

> <details>
> <summary>ℹ️ <em>Tuple e Liste</em></summary>
>
> All'osservatore attento non sfuggirà il fatto che le tuple e le liste siano
> simili dal punto di vista sintattico e differiscano sostanzialmente per la
> mutabilità. Da questo discende che le tuple sono estremamente efficaci nel
> caso in cui sia necessario **_solo_** accedere agli elementi contenuti, mentre
> le liste le usiamo se è necessario anche modificare gli elementi.
>
> </details>

# Insiemi

Anche gli insiemi (in inglese _set_) sono sintatticamente molto simili alle
liste, ma offrono una significativa differenza: _non ci possono essere elementi_
_ripetuti_.

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> L'analogia col concetto matematico di insieme è evidente.
>
> </details>

La sintassi per creare un insieme è la seguente:

```python
insm = {1, "stringa", 2}
```

L'insieme ammette al suo interno dati eterogenei, tuttavia non può contenere
liste o dizionari. Questo è legato al fatto che gli insiemi (ma anche i
dizionari) sono delle [hash table](https://it.wikipedia.org/wiki/Hash_table),
dunque sfruttano il concetto di _hash_ per rappresentare i dati contenuti in
maniera compatta ed efficiente. Poiché sia le liste che i dizionari non possono
essere rappresentati in questo modo, non possono essere racchiusi in un insieme.

Un'altra considerazione riguardante gli insiemi è che questi non sono ordinati:
questo rende impossibile accedere (e modificare) un elemento del set mediante il
suo indice, al contrario di liste e tuple.

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Gli insiemi possono essere usati per isolare gli elementi univoci presenti in
> una lista. Per farlo, basta convertire la lista in insieme:
>
> ```python
> lst = [1, 2, 2, 3]
> insm = set(lst)    # l'insieme sarà `{1, 2, 3}`
> ```
>
> </details>

# Dizionari

Il quarto ed ultimo tipo di struttura dati per sequenze degli stessi è il
_dizionario_, presente in altri linguaggi di programmazione sotto il nome di
_array associativo_ oppure _hash map_.

La base di un dizionario è la coppia _chiave_-_valore_ (spesso _key_-_val_),
nella quale un certo valore (di qualsiasi tipo) viene associato ad una
determinata chiave (immutabile).

I dizionari hanno diverse caratteristiche comuni ai set, dall'inutilizzabilità
delle liste come chiavi, al non permettere la ripetizione delle chiavi. Per
accedere alle coppie _key_-_val_ è necessario utilizzare l'opportuna chiave, e
non l'ordine delle coppie.

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Una differenza tra insiemi e dizionari sta nel fatto che quest'ultimi sono
> _ordinati_ a partire da Python 3.7.
>
> </details>

Per creare un dizionario, possiamo usare una sintassi simile a quella degli
insiemi. Ad esempio, per creare un dizionario vuoto:

```python
dct = {}
```

Possiamo ora inserire delle coppie _key-val_ in questo modo:

```python
dct["key"] = "val"
dct[1] = "n"   # `dct` sarà `{"key": "val", 1, "n"}`
```

Per accedere al valore associato ad una determinata chiave:

```python
dct[1]   # otterremo "n"
```

## Chiavi e valori

È possibile recuperare la lista di tutte la chiavi presenti in un dizionario
usando il metodo `keys()`, che restituisce un oggetto di tipo `dict_keys()`, che
può essere convertito in lista:

```python
keys = dct.keys()     # restituisce `dict_keys(['key', 1])`. Non è una lista!
print(list(chiavi))   # restituisce `['key', 1]`. È una lista
```

Analogamente, si può accedere a tutti i valori presenti nel dizionario mediante
il metodo `values()`, che restituisce un oggetto di tipo `dict_values()`
anch'esso da convertire in lista:

```python
vals = dct.values()   # restituisce `dict_values(['val', 'n'])`. Non è una lista!
print(list(vals)) # restituisce `['val', 'n']`. È una lista
```

Possiamo accedere anche a tutte le coppie _key-val_ mediante il metodo
`items()`, che restituisce un oggetto di tipo `dict_items()` che può essere
convertito in una lista di tuple:

```python
pairs = dct.items() # restituisce `dict_items([('key', 'val'), (1, 'n')])`
print(list(pairs))   # restituisce `['key', 'val']`. È una lista di tuple
```

## Creazione di un dizionario non vuoto

Sono presenti diversi modi per creare un dizionario non vuoto.

### Uso dell'operatore `{}`

Il metodo più semplice, che è anche quello che useremo più spesso, consiste nel
dichiarare nell'operatore `{}` le coppie _key-val_ iniziali:

```pycon
>>> dct = {"key1": 1, "key2": 2}
>>> dct
{'key1': 1, 'key2': 2}
```

### Uso del costruttore `dict()`

Un altro metodo consiste nell'usare il costruttore `dict()`:

```pycon
>>> dct = dict(key1=1, key2=2)
>>> dct
{'key1': 1, 'key2': 2}
```

### Uso della funzione `zip()`

Possiamo usare la funzione `zip()` per creare un dizionario a partire da due
liste:

```pycon
>>> keys = ["key1", "key2"]
>>> vals = [1, 2]
>>> dct = dict(zip(keys, vals))
>>> dct
{'key1': 1, 'key2': 2}
```

### Dict comprehension

Un modo per ottenere un dizionario a partire da un altro oggetto iterabile è la
_dict comprehension_, che è una forma del tipo:

```python
dct_out = {key: val for val in iterabile}
```

Ad esempio, possiamo creare un dizionario contenente come chiave i numeri da `1`
a `9` e come valori corrispondenti i quadrati degli stessi:

```pycon
>>> sqrs = {str(i): i**2 for i in range(1, 10)}
>>> print(sqrs)
{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
```

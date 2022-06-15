# 07 – Introduzione a NumPy

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [07 – Introduzione a NumPy](#07--introduzione-a-numpy)
   1. [Installare NumPy](#installare-numpy)
2. [Uso di NumPy](#uso-di-numpy)
   1. [Gli `ndarray`](#gli-ndarray)
   2. [Array vs liste](#array-vs-liste)
3. [Operazioni Algebriche con NumPy](#operazioni-algebriche-con-numpy)
   1. [Approccio con liste](#approccio-con-liste)

<!-- /TOC -->

</details>

La libreria **NumPy**, il cui nome deriva dalla sincrasi tra <em>Num</em>erical
e <em>Py</em>thon, è una tra le più utilizzate nelle applicazioni
di calcolo scientifico in Python.

Nella pratica, possiamo pensare a NumPy come ad uno standard _de facto_: le
classi e i metodi messi a disposizione dalla libreria sono utilizzati nella quasi
totalità degli altri strumenti Python per le scienze matematiche, chimiche, fisiche
e anche ingegneristiche.

Partiamo nella nostra disamina dalla procedura di installazione della libreria.

## Installare NumPy

> <details>
> <summary>ℹ️ <em>Installazione di una libreria</em></summary>
>
> Si ricorda che le opzioni utilizzabili per installare una libreria sono
> descritte in dettaglio nell'[appendice B]
>
> </details>

Per installare NumPy, ricorriamo all'utilizzo di `pip`, preferibilmente
all'interno di un ambiente virtuale:

```sh
$ conda activate <my-env>
(<my-env>) ~$ pip install numpy
```

# Uso di NumPy

## Gli `ndarray`

Abbiamo visto in precedenza che per usare un package o un modulo Python
all'interno dei nostri programmi dovremo per prima cosa importarlo:

```python
import numpy as np
```

Una volta importato, utilizziamo la struttura dati principe della libreria: l'array,
analogo a quelli descritti dalla classica formulazione matematica.

Nello specifico, NumPy mette a disposizione gli `ndarray`, ovvero delle strutture
dati in grado di rappresentare array a _n_ dimensioni, contenenti dati di tipo _omogeneo_.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Anche `ndarray` è un'abbreviazione che sta per _n_-<em>d</em>imensional _array_
>
> </details>

Il metodo più semplice per creare un array è usare il costruttore `array` a cui
viene passata una lista:

```pycon
>>> a = np.array([1, 2, 3])
```

## Array vs liste

Sono diverse le differenze presenti tra un array e una lista. Le
sono riassunte nella seguente tabella:

| Caratteristica | `ndarray`             | `list`          |
| -------------- | --------------------- | --------------- |
| Dimensione     | Fissa                 | Non fissa       |
| Elementi       | Omogenei              | Eterogenei      |
| Ambito         | Operazioni algebriche | General-purpose |

In pratica:

- un array ha dimensione fissa. Cambiarne la dimensione comporterà la creazione
  di un nuovo array e la cancellazione di quello originario;
- gli elementi di un array devono essere dello stesso tipo (tale limitazione
  non vale ovviamente per le liste);
- gli array sono pensati specificamente per le operazioni algebriche, mentre
  le liste sono pensate per degli scopi generici.

# Operazioni Algebriche con NumPy

Come detto, gli array NumPy sono progettati nello specifico per le operazioni
algebriche. Ovviamente, ciò assume una notevole rilevanza dati i nostri fini.
Per capirlo, facciamo un semplice esempio: moltiplichiamo tra loro due vettori
monodimensionali _elemento-per-elemento_.

## Approccio con liste

Per effettuare la suddetta operazione possiamo usare un ciclo `for` o una
list comprehension:

```python
# ciclo for
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])

# list comprehension
c = [a[i] * b[i] for i in range(len(a))]
```

Il risultato dell'operazione sarà in entrambi i casi **corretto**. Tuttavia,
i cicli sono _computazionalmente costosi_: all'aumentare del numero di elementi
contenuti nei vettori, sarà necessario pagare un costo crescente.

Questo potrebbe essere in qualche modo arginato ricorrendo ad un linguaggio più
efficiente, come ad esempio il C. Tuttavia, provando ad estendere il calcolo a
due dimensioni, il codice diverrà:

```python
for i in range(len(a)):
    for j in range(len(b)):
        c.append(a[i][j]*b[i][j])
```

Il numero di cicli annidati aumenterà in maniera direttamente proporzionale
alla dimensionalità degli array coinvolti. Ciò implica che per un array a _m_
dimensioni avremo altrettanti cicli annidati e con tutto ciò che ne consegue in
termini di complessità di codice.

È proprio in questa situazione che NumPy ci viene in aiuto. Infatti, per
moltiplicare due array di qualsiasi dimensionalità ci basta usare la seguente
istruzione:

```python
c = a * b
```

Dove sia `a` che `b` sono due array creati in precedenza.

Una sintassi di questo tipo risulta essere molto più concisa e semplice
rispetto all'uso dei cicli annidati. È inoltre molto simile a quella che
possiamo trovare sulle formule usate nei libri di testo.

L'uso di questa sintassi si esplicita in due concetti fondamentali sui quali
risulta essere basato NumPy:

- la Vettorizzazione del codice, ovvero la possibilità di scrivere istruzioni
  matriciali senza usare esplicitamente dei cicli;
- il broadcasting, che riguarda la possibilità di usare una sintassi comune e
  indipendente dalla dimensionalità degli array coinvolti nelle operazioni.

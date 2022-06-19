# 07 – NumPy

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [07 – NumPy](#07--numpy)
   1. [Installare NumPy](#installare-numpy)
2. [Introduzione a Numpy](#introduzione-a-numpy)
   1. [Gli `ndarray`](#gli-ndarray)
   2. [Array vs liste](#array-vs-liste)
   3. [Operazioni Algebriche con NumPy](#operazioni-algebriche-con-numpy)
      1. [Approccio con liste](#approccio-con-liste)
3. [Gli array](#gli-array)
   1. [Array e liste](#array-e-liste)
      1. [Array eterogenei](#array-eterogenei)
   2. [Il numero di elementi di un array](#il-numero-di-elementi-di-un-array)
   3. [Altri metodi per creare un array](#altri-metodi-per-creare-un-array)
      1. [Array con valori zero o unitari](#array-con-valori-zero-o-unitari)
      2. [Array vuoti](#array-vuoti)
      3. [Matrice identità](#matrice-identità)
      4. [Matrici diagonali](#matrici-diagonali)
      5. [Matrici triangolari](#matrici-triangolari)
   4. [Accesso agli elementi di un array](#accesso-agli-elementi-di-un-array)
   5. [Maschere booleane](#maschere-booleane)
   6. [Slicing degli array](#slicing-degli-array)
   7. [La funzione `nonzero()`](#la-funzione-nonzero)
   8. [Fancy indexing](#fancy-indexing)

<!-- /TOC -->

</details>

La libreria **NumPy**, il cui nome deriva dalla sincrasi tra <em>Num</em>erical
e <em>Py</em>thon, è una tra le più utilizzate nelle applicazioni
di calcolo scientifico in Python.

Nella pratica, possiamo pensare a NumPy come ad uno standard _de facto_: le
classi e i metodi messi a disposizione dalla libreria sono utilizzati nella
quasi totalità degli altri strumenti Python per le scienze matematiche, chimiche,
fisiche e anche ingegneristiche.

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

# Introduzione a Numpy

## Gli `ndarray`

Abbiamo visto in precedenza che per usare un package o un modulo Python
all'interno dei nostri programmi dovremo per prima cosa importarlo:

```python
import numpy as np
```

Una volta importato, utilizziamo la struttura dati principe della libreria:
l'array, analogo a quelli descritti dalla classica formulazione matematica.

Nello specifico, NumPy mette a disposizione gli `ndarray`, ovvero delle
strutture dati in grado di rappresentare array a _n_ dimensioni, contenenti dati
di tipo _omogeneo_.

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

## Operazioni Algebriche con NumPy

Come detto, gli array NumPy sono progettati nello specifico per le operazioni
algebriche. Ovviamente, ciò assume una notevole rilevanza dati i nostri fini.
Per capirlo, facciamo un semplice esempio: moltiplichiamo tra loro due vettori
monodimensionali _elemento-per-elemento_.

### Approccio con liste

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

# Gli array

Nella lezione precedente abbiamo introdotto il concetto gli array, ovvero la
struttura dati principale dell'ecosistema di NumPy. In questa lezione (e nelle
successive) ne approfondiremo aspetti e caratteristiche principali.

## Array e liste

L'impressione che si può avere osservando gli array è che questi siano molto
simili alle liste. Tuttavia, come abbiamo già visto, esistono diverse
differenze notevoli, riassumibili in linea di massima affermando che è
preferibile usare un array quando si devono svolgere operazioni di tipo
matematico su dati omogenei.

Gli array NumPy sono istanze della classe `ndarray`, crasi che sta per
_n_-dimensional array. Mediante questa classe possiamo rappresentare strutture
dati con un numero arbitrario di dimensioni, ovvero vettori, matrici e tensori.

Il primo passo per utilizzare un array è, come accennato in precedenza,
crearlo. Per farlo ci sono diversi metodi. Ricordiamo quello più semplice, che
prevede l'uso del costruttore `array()` a quale passare una lista di elementi
dello stesso tipo:

```pycon
>>> arry = np.array([1, 2, 3, 4, 5, 6])
>>> arry
array([1, 2, 3, 4, 5, 6])
```

Passando invece una lista i cui elementi sono a loro volta delle liste, potremo
ottenere in uscita un array multidimensionale:

```pycon
>>> marry = np.array([[1, 2, 3], [4, 5, 6]])
>>> marry
array([[1, 2, 3],
       [4, 5, 6]])
```

Notiamo infine che gli array non sono necessariamente numerici. Possiamo, ad
esempio, creare un array di stringhe:

```pycon
>>> sarry = np.array(["str", "ing"])
>>> sarry
array(['str', 'ing'], dtype='<U3')
```

### Array eterogenei

In precedenza si è accennato al fatto che gli array, a differenza delle liste,
debbano contenere dati omogenei. Cosa succederebbe quindi se provassimo a
passare al metodo `array()` una lista composta da dati di tipo eterogeneo?
Partiamo verificando cosa accade ad esempio usando un `int` ed un `float`.

```pycon
>>> test_arry = np.array([1, 1.0])
>>> test_arry
array([1., 1.])
```

È stata effettuata in maniera implicita ed automatica un'operazione di
conversione di tipo, e tutti i valori passati sono stati convertiti in formato
`float`.

Interessante è anche valutare cosa accade se provassimo a passare una lista
contenente un numero ed una stringa:

```pycon
>>> test_arry = np.array([1, "string"])
>>> test_arry
array(['1', 'string'], dtype='<U11')
```

Anche in questo caso è stata effettuata una conversione di tipo, passando
stavolta da intero a stringa.

> <details open>
> <summary>ℹ️ <em>Upcasting</em></summary>
>
> La regola da tenere a mente è che NumPy (e, in generale, Python) seguono il
> principio dell'upcasting: in altre parole, quando deve essere fatta una
> conversione tra diversi tipi di dati, si fa in modo di scegliere il tipo a
> più alta precisione, minimizzando i rischi di perdita di informazioni.
>
> </details>

## Il numero di elementi di un array

Gli array NumPy hanno dimensione prefissata, e sono quindi in grado di
contenere un numero fisso di oggetti di un certo tipo. Per definire (o
conoscere) questo valore si utilizza una proprietà chiamata `shape` che, a
grandi linee, rappresenta la forma dell'array. La `shape` di un array è in
pratica una tupla di numeri interi, ovviamente non negativi, ciascuno dei quali
determina il numero di elementi per ciascuna delle dimensioni dell'array.

Creiamo ad esempio un array che rappresenti una matrice 2×3, ovvero a due righe
e tre colonne:

```pycon
>>> arry = np.array([[1, 2, 3], [4, 5, 6]])
>>> arry
array([[1, 2, 3],
       [4, 5, 6]])
```

Vediamo che valore assume la proprietà shape di questo array:

```pycon
>>> arry.shape
(2, 3)
```

Come ci aspettavamo, il nostro array ha cardinalità due sulla prima dimensione
(ovvero il numero di righe) e tre sulla seconda (ovvero il numero di colonne).

## Altri metodi per creare un array

Oltre al metodo visto in precedenza, possiamo creare un array utilizzando
direttamente il costruttore della classe `ndarray`:

```pycon
>>> ndarry = np.ndarray([3, 3])   # oppure ndarry = np.ndarray(shape=(3, 3))
>>> ndarry
array([[0.00e+000, 0.00e+000, 0.00e+000],
       [0.00e+000, 0.00e+000, 1.82e-321],
       [0.00e+000, 0.00e+000, 0.00e+000]])
```

Il costruttore accetta una lista contenente la `shape` dell'array, che in
questo caso diverrà un 3×3.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> I numeri con cui viene riempito l'array sono casuali.
>
> </details>

Oltre a questa tecnica base, esistono diversi modi per creare array di un certo
tipo. Vediamoli in breve.

### Array con valori zero o unitari

Possiamo creare un array di dimensioni arbitrarie in cui tutti gli elementi
sono pari ad 1. Per farlo, usiamo la funzione `ones()`:

```pycon
>>> oarry = np.ones(shape=(3, 3))
>>> oarry
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
```

In modo simile, possiamo creare array di dimensioni arbitrarie in cui tutti gli
elementi sono pari a zero mediante la funzione `zeros()`:

```pycon
>>> zarry = np.zeros(shape=(3, 3))
>>> zarry
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

### Array vuoti

Possiamo creare un array vuoto mediante la funzione `empty()`:

```pycon
>>> earry = np.empty(shape=(3, 3))
>>> earry
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

Questa funzione può risultare utile quando vogliamo pre-allocare spazio per un
array.

### Matrice identità

Possiamo creare una matrice identità usando la funzione `eye()`:

```pycon
>>> iarry = np.eye(3)
>>> iarry
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> In questo caso, non si può passare una tupla o una lista per indicare le
> dimensioni dell'array. Tuttavia, possiamo specificare sia il numero delle
> righe (con il primo parametro) che il numero delle colonne (con il secondo
> parametro).
>
> </details>

### Matrici diagonali

La funzione `diag()` viene usata sia per creare una matrice diagonale a partire
da un vettore (che sarà poi la diagonale della matrice), sia per estrarre la
diagonale di una matrice. Per capire questa dualità, immaginiamo di avere un
vettore riga a tre elementi, che vogliamo trasformare in modo tale che si
comporti come la diagonale di una matrice.

```pycon
>>> vect = np.array([5, 2, 3])
>>> vect
array([5, 2, 3])
```

Potremo creare una matrice diagonale a partire da questo vettore passandolo
come parametro alla funzione `diag()`:

```pycon
>>> darray = np.diag(vect)
>>> darray
array([[5, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
```

Vediamo invece come affrontare il problema opposto. Immaginiamo di avere un
array e volerne estrarre la diagonale:

```pycon
>>> arry = np.array([[5, 5, 5], [2, 1, 3], [4, 3, 6]])
>>> arry
array([[5, 5, 5],
       [2, 1, 3],
       [4, 3, 6]])
```

Per farlo, dovremo anche questa volta usare la funzione `diag()`:

```pycon
>>> vect = np.diag(arry)
>>> vect
array([5, 1, 6])
```

Il fatto che la funzione `diag()` venga usata per operazioni opposte può
causare confusione. L'importante è ricordare che passando un vettore si ottiene
una matrice, mentre passando una matrice si ottiene un vettore.

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> La funzione `diag()` accetta solo input monodimensionali (vettori) e
> bidimensionali (matrici)!
>
> </details>

### Matrici triangolari

Concludiamo questa breve carrellata mostrando due metodi in grado di estrarre
la matrice triangolare, rispettivamente superiore ed inferiore.

Supponiamo di avere la matrice `arry` definita in precedenza. Per estrarre la
matrice triangolare superiore, dovremo usare la funzione `triu()`:

```pycon
>>> arry_triu = np.triu(arry)
>>> arry_triu
array([[5, 5, 5],
       [0, 1, 3],
       [0, 0, 6]])
```

Per estrarre invece la matrice triangolare inferiore, dovremo usare la funzione
`tril()`:

```pycon
>>> arry_tril = np.tril(arry)
>>> arry_tril
array([[5, 0, 0],
       [2, 1, 0],
       [4, 3, 6]])
```

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> In questo caso, le funzioni `tril()` e `triu()` possono tranquillamente
> essere applicate agli array _n_-dimensionali. Inoltre, non è richiesto che le
> diverse dimensioni dell'array abbiano la stessa cardinalità.
>
> </details>

## Accesso agli elementi di un array

Così come per le liste, il modo più immediato per accedere al valore di un
elemento in un array è usare l'operatore `[]`, specificando contestualmente
l'indice dell'elemento cui si vuole accedere. Ad esempio, per selezionare il
primo elemento di un vettore:

```pycon
>>> vect = np.array([1, 2, 3])
>>> vect[0]
1
```

Nel caso di array ad _n_ dimensioni, è necessario indicare l'indice per
ciascuna delle dimensioni dell'array. Ad esempio, per un array bidimensionale
potremmo selezionare l'elemento alla prima riga e prima colonna con una
sintassi di questo tipo:

```pycon
>>> barry = np.array([[1, 2], [3, 4]])
>>> barry[0][0]
1
```

## Maschere booleane

Possiamo accedere ad un sottoinsieme di elementi dell'array mediante una
maschera, ovvero un altro array di dimensioni uguali a quelle di partenza, al
cui interno sono presenti esclusivamente dei valori booleani. Così facendo,
estrarremo soltanto gli elementi la cui corrispondente posizione all'interno
della maschera ha valore `True`. Ad esempio, possiamo selezionare tutti gli
elementi appartenenti alla prima colonna dell'array `barry`:

```pycon
>>> mask = np.array([[True, False], [True, False]])
>>> barry[mask]
array([1, 3])
```

Ancora, possiamo scegliere tutti gli elementi che soddisfano una certa
condizione logico/matematica:

```pycon
>>> mask = (barry > 2)
>>> mask
array([[False, False],
       [ True,  True]])
>>> barry[mask]
array([3, 4])
```

Interessante notare come la precedente notazione possa essere ulteriormente
sintetizzata usando delle relazioni logiche:

```pycon
>>> barry[barry > 2]
array([3, 4])
```

Possiamo adattare la forma precedente all'uso di espressioni arbitrariamente
complesse:

```pycon
>>> barry[barry%2 == 0]
array([2, 4])
>>> barry[(barry > 1) & (barry < 4)]
array([2, 3])
```

## Slicing degli array

Così come le liste, anche gli array consentono le operazioni di slicing:

```pycon
>>> arry = np.array([1, 2, 3, 4])
>>> arry[0:2]
array([1, 2])
```

Per gli array multidimensionali, lo slicing si intende sulla _n_-ma dimensione
dell'array. Questo concetto è facile da comprendere se si visualizza l'array ad
_n_-dimensioni come un array di array:

```pycon
>>> barry
array([[1, 2],
       [3, 4]])
>>> barry[0:1]   # Lo slicing viene effettuato sulla seconda dimensione
array([[1, 2]])
```

## La funzione `nonzero()`

Possiamo usare la funzione `nonzero()` per selezionare gli elementi e gli
indici di un array il cui valore non sia pari a zero. Ad esempio:

```pycon
>>> tarry = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
>>> tarry
array([[3, 0, 0],
       [0, 4, 0],
       [5, 6, 0]])
>>> np.nonzero(tarry)
(array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
```

La funzione `nonzero()` restituisce una tupla con gli indici per riga e colonna
degli elementi diversi da zero. In particolare, la tupla risultante avrà un
numero di elementi pari a ciascuna delle dimensioni dell'array `x` di ingresso,
e l'𝑖-mo vettore individuerà gli indici relativi alla 𝑖-ma dimensione. Ad
esempio, in questo caso, il primo array rappresenta gli indici relativi alla
prima dimensione dei valori non nulli (in questo caso, gli indici di riga),
mentre il secondo gli indici relativi alla seconda dimensione (indici di
colonna). Notiamo quindi che avremo i seguenti elementi diversi da zero:

| Indice di riga | Indice di Colonna | Valore |
| :------------- | :---------------- | :----- |
| 0              | 0                 | 3      |
| 1              | 1                 | 4      |
| 2              | 0                 | 5      |
| 2              | 1                 | 6      |

<!-- TODO: `s` is undefined
> <details open>
> <summary>ℹ️ <em>Ottenere una lista di tuple</em></summary>
>
> Possiamo ottenere una lista di tuple rappresentative delle coppie di indici
> per gli elementi non nulli sfruttando la funzione `zip()`:
>
> ```pycon
> >>> coords = list(zip(s[0], s[1]))
> >>> coords
> [(0, 0), (1, 1), (2, 0), (2, 1)]
> ```
>
> </details>
> -->

## Fancy indexing

Chiudiamo questa lezione parlando di una tecnica molto interessante chiamata
fancy indexing, consistente nell'usare un array di indici per accedere a più
elementi contemporaneamente. Ad esempio:

```pycon
>>> rand = np.random.RandomState(42)
>>> x = rand.randint(100, size=10)
>>> indexes = np.array([[1, 4], [5, 2]])
>>> x
array([51, 92, 14, 71, 60, 20, 82, 86, 74, 74])
>>> x[indexes]
array([[92, 60],
       [20, 14]])
```

Nel codice precedente, stiamo:

1. usando la funzione `randint()` per generare un array di numeri interi
   casuali compresi tra 0 e 100;
2. generando un array bidimensionale `indexes`;
3. restituendo, mediante il fancy indexing, un array con le dimensioni di
   `indexes` e gli elementi di `x` presi nelle posizioni indicate da `indexes`.

La potenza del fancy indexing sta proprio in questo: non solo siamo in grado di
accedere facilmente a più elementi di un array mediante un'unica operazione, ma
possiamo anche ridisporre questi elementi come più ci aggrada!

# 07 – NumPy

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<a name="top"></a>

<!-- TOC -->

1. [07 – NumPy](#07--numpy)
   1. [Installare NumPy (⮨)](#installare-numpy-)
2. [Introduzione a Numpy (⮨)](#introduzione-a-numpy-)
   1. [Gli `ndarray` (⮨)](#gli-ndarray-)
   2. [Array vs liste (⮨)](#array-vs-liste-)
   3. [Operazioni Algebriche con NumPy (⮨)](#operazioni-algebriche-con-numpy-)
      1. [Approccio con liste (⮨)](#approccio-con-liste-)
3. [Gli array (⮨)](#gli-array-)
   1. [Array e liste (⮨)](#array-e-liste-)
      1. [Array eterogenei (⮨)](#array-eterogenei-)
   2. [Il numero di elementi di un array (⮨)](#il-numero-di-elementi-di-un-array-)
   3. [Altri metodi per creare un array (⮨)](#altri-metodi-per-creare-un-array-)
      1. [Array con valori zero o unitari (⮨)](#array-con-valori-zero-o-unitari-)
      2. [Array vuoti (⮨)](#array-vuoti-)
      3. [Matrice identità (⮨)](#matrice-identità-)
      4. [Matrici diagonali (⮨)](#matrici-diagonali-)
      5. [Matrici triangolari (⮨)](#matrici-triangolari-)
   4. [Accesso agli elementi di un array (⮨)](#accesso-agli-elementi-di-un-array-)
   5. [Maschere booleane (⮨)](#maschere-booleane-)
   6. [Slicing degli array (⮨)](#slicing-degli-array-)
   7. [La funzione `nonzero()` (⮨)](#la-funzione-nonzero-)
   8. [Fancy indexing (⮨)](#fancy-indexing-)
4. [Operazioni fondamentali sugli array (⮨)](#operazioni-fondamentali-sugli-array-)
   1. [Operazioni algebriche di base (⮨)](#operazioni-algebriche-di-base-)
   2. [La funzione `sum()` (⮨)](#la-funzione-sum-)
   3. [La funzione `dot()` (⮨)](#la-funzione-dot-)
   4. [La funzione `sort()` (⮨)](#la-funzione-sort-)
   5. [Concatenare due array (⮨)](#concatenare-due-array-)
   6. [Rimozione e inserimento di elementi in un array (⮨)](#rimozione-e-inserimento-di-elementi-in-un-array-)
      1. [La funzione `delete()` (⮨)](#la-funzione-delete-)
         1. [Array multidimensionali e `delete()` (⮨)](#array-multidimensionali-e-delete-)
      2. [La funzione `insert()` (⮨)](#la-funzione-insert-)
      3. [La funzione `append()` (⮨)](#la-funzione-append-)
   7. [Dimensioni e forma di un array (⮨)](#dimensioni-e-forma-di-un-array-)
   8. [Modificare le dimensioni di un array (⮨)](#modificare-le-dimensioni-di-un-array-)
   9. [Flattening di un array (⮨)](#flattening-di-un-array-)
5. [Operazioni matriciali (⮨)](#operazioni-matriciali-)
   1. [Matrice trasposta (⮨)](#matrice-trasposta-)
   2. [Matrice inversa (⮨)](#matrice-inversa-)
   3. [Prodotti vettoriali e tra matrici (⮨)](#prodotti-vettoriali-e-tra-matrici-)
      1. [La funzione `dot()` (⮨)](#la-funzione-dot--1)
      2. [Prodotto interno (⮨)](#prodotto-interno-)
      3. [Prodotto esterno (⮨)](#prodotto-esterno-)
      4. [La funzione `matmul()` (⮨)](#la-funzione-matmul-)
   4. [Potenza di Matrice (⮨)](#potenza-di-matrice-)
   5. [Decomposizione ai valori singolari (⮨)](#decomposizione-ai-valori-singolari-)
   6. [Autovalori e Autovettori (⮨)](#autovalori-e-autovettori-)
   7. [Norma (⮨)](#norma-)
   8. [Determinante, rango e traccia (⮨)](#determinante-rango-e-traccia-)
   9. [Risoluzione di sistemi di equazioni lineari (⮨)](#risoluzione-di-sistemi-di-equazioni-lineari-)
6. [Operazioni polinomiali in NumPy (⮨)](#operazioni-polinomiali-in-numpy-)
   1. [Addizione di polinomi (⮨)](#addizione-di-polinomi-)
   2. [Sottrazione di polinomi (⮨)](#sottrazione-di-polinomi-)
   3. [Moltiplicazione di polinomi (⮨)](#moltiplicazione-di-polinomi-)
   4. [Divisione tra polinomi (⮨)](#divisione-tra-polinomi-)
   5. [Elevazione a potenza (⮨)](#elevazione-a-potenza-)
   6. [Valore assunto da un polinomio (⮨)](#valore-assunto-da-un-polinomio-)
   7. [Derivate e integrale di funzioni polinomiali (⮨)](#derivate-e-integrale-di-funzioni-polinomiali-)
7. [Statistica in NumPy (⮨)](#statistica-in-numpy-)
   1. [Minimo e massimo di un array (⮨)](#minimo-e-massimo-di-un-array-)
   2. [Percentile e quantile (⮨)](#percentile-e-quantile-)
   3. [Media aritmetica e media pesata (⮨)](#media-aritmetica-e-media-pesata-)
   4. [Varianza e deviazione standard (⮨)](#varianza-e-deviazione-standard-)
   5. [Matrice di covarianza (⮨)](#matrice-di-covarianza-)
   6. [Istogramma (⮨)](#istogramma-)

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

## Installare NumPy ([⮨](#top))

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

# Introduzione a Numpy ([⮨](#top))

## Gli `ndarray` ([⮨](#top))

Abbiamo visto in precedenza che per usare un package o un modulo Python
all'interno dei nostri programmi dovremo per prima cosa importarlo:

```python
import numpy as np
```

Una volta importato, utilizziamo la struttura dati principe della libreria:
l'array, analogo a quelli descritti dalla classica formulazione matematica.

Nello specifico, NumPy mette a disposizione gli `ndarray`, ovvero delle
strutture dati in grado di rappresentare array a $n$-dimensioni, contenenti dati
di tipo _omogeneo_.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Anche `ndarray` è un'abbreviazione che sta per $n$-<em>d</em>imensional _array_
>
> </details>

Il metodo più semplice per creare un array è usare il costruttore `array` a cui
viene passata una lista:

```pycon
>>> a = np.array([1, 2, 3])
```

## Array vs liste ([⮨](#top))

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

## Operazioni Algebriche con NumPy ([⮨](#top))

Come detto, gli array NumPy sono progettati nello specifico per le operazioni
algebriche. Ovviamente, ciò assume una notevole rilevanza dati i nostri fini.
Per capirlo, facciamo un semplice esempio: moltiplichiamo tra loro due vettori
monodimensionali _elemento-per-elemento_.

### Approccio con liste ([⮨](#top))

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
alla dimensionalità degli array coinvolti. Ciò implica che per un array a $m$
dimensioni avremo altrettanti cicli annidati e tutto ciò che ne consegue in
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

# Gli array ([⮨](#top))

Nella lezione precedente abbiamo introdotto il concetto gli array, ovvero la
struttura dati principale dell'ecosistema di NumPy. In questa lezione (e nelle
successive) ne approfondiremo aspetti e caratteristiche principali.

## Array e liste ([⮨](#top))

L'impressione che si può avere osservando gli array è che questi siano molto
simili alle liste. Tuttavia, come abbiamo già visto, esistono diverse
differenze notevoli, riassumibili in linea di massima affermando che è
preferibile usare un array quando si devono svolgere operazioni di tipo
matematico su dati omogenei.

Gli array NumPy sono istanze della classe `ndarray`, crasi che sta per
$n$-dimensional array. Mediante questa classe possiamo rappresentare strutture
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

### Array eterogenei ([⮨](#top))

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

## Il numero di elementi di un array ([⮨](#top))

Gli array NumPy hanno dimensione prefissata, e sono quindi in grado di
contenere un numero fisso di oggetti di un certo tipo. Per definire (o
conoscere) questo valore si utilizza una proprietà chiamata `shape` che, a
grandi linee, rappresenta la forma dell'array. La `shape` di un array è in
pratica una tupla di numeri interi, ovviamente non negativi, ciascuno dei quali
determina il numero di elementi per ciascuna delle dimensioni dell'array.

Creiamo ad esempio un array che rappresenti una matrice $2 \times 3$, ovvero a
due righe e tre colonne:

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

## Altri metodi per creare un array ([⮨](#top))

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
questo caso diverrà un $3 \times 3$.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> I numeri con cui viene riempito l'array sono casuali.
>
> </details>

Oltre a questa tecnica base, esistono diversi modi per creare array di un certo
tipo. Vediamoli in breve.

### Array con valori zero o unitari ([⮨](#top))

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

### Array vuoti ([⮨](#top))

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

### Matrice identità ([⮨](#top))

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

### Matrici diagonali ([⮨](#top))

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

### Matrici triangolari ([⮨](#top))

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
> essere applicate agli array $n$-dimensionali. Inoltre, non è richiesto che le
> diverse dimensioni dell'array abbiano la stessa cardinalità.
>
> </details>

## Accesso agli elementi di un array ([⮨](#top))

Così come per le liste, il modo più immediato per accedere al valore di un
elemento in un array è usare l'operatore `[]`, specificando contestualmente
l'indice dell'elemento cui si vuole accedere. Ad esempio, per selezionare il
primo elemento di un vettore:

```pycon
>>> vect = np.array([1, 2, 3, 4])
>>> vect[0]
1
```

Nel caso di array a $n$ dimensioni, è necessario indicare l'indice per
ciascuna delle dimensioni dell'array. Ad esempio, per un array bidimensionale
potremmo selezionare l'elemento alla prima riga e prima colonna con una
sintassi di questo tipo:

```pycon
>>> barry = np.array([[1, 2], [3, 4]])
>>> barry[0][0]
1
```

## Maschere booleane ([⮨](#top))

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

## Slicing degli array ([⮨](#top))

Così come le liste, anche gli array consentono le operazioni di slicing:

```pycon
>>> arry = np.array([1, 2, 3, 4])
>>> arry[0:2]
array([1, 2])
```

Per gli array multidimensionali, lo slicing si intende sulla $n$-ma dimensione
dell'array. Questo concetto è facile da comprendere se si visualizza l'array a
$n$-dimensioni come un array di array:

```pycon
>>> barry
array([[1, 2],
       [3, 4]])
>>> barry[0:1]   # Lo slicing viene effettuato sulla seconda dimensione
array([[1, 2]])
```

## La funzione `nonzero()` ([⮨](#top))

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
numero di elementi pari a ciascuna delle dimensioni dell'array di ingresso,
e l'$i$-mo vettore individuerà gli indici relativi all'$i$-ma dimensione. Ad
esempio, in questo caso, il primo array rappresenta gli indici relativi alla
prima dimensione dei valori non nulli (in questo caso, gli indici di riga),
mentre il secondo gli indici relativi alla seconda dimensione (indici di
colonna). Notiamo quindi che avremo i seguenti elementi diversi da zero:

| Indice di riga | Indice di Colonna | Valore |
| :------------- | :---------------- | :----- |
| $0$            | $0$               | $3$    |
| $1$            | $1$               | $4$    |
| $2$            | $0$               | $5$    |
| $2$            | $1$               | $6$    |

> <details open>
> <summary>ℹ️ <em>Ottenere una lista di tuple</em></summary>
>
> Possiamo ottenere una lista di tuple rappresentative delle coppie di indici
> per gli elementi non nulli sfruttando la funzione `zip()`:
>
> ```pycon
> >>> s = np.nonzero(tarry)
> >>> s
> (array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
> >>> coords = list(zip(s[0], s[1]))
> >>> coords
> [(0, 0), (1, 1), (2, 0), (2, 1)]
> ```
>
> </details>

## Fancy indexing ([⮨](#top))

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
   casuali compresi tra $0$ e $100$;
2. generando un array bidimensionale `indexes`;
3. restituendo, mediante il fancy indexing, un array con le dimensioni di
   `indexes` e gli elementi di `x` presi nelle posizioni indicate da `indexes`.

La potenza del fancy indexing sta proprio in questo: non solo siamo in grado di
accedere facilmente a più elementi di un array mediante un'unica operazione, ma
possiamo anche ridisporre questi elementi come più ci aggrada!

# Operazioni fondamentali sugli array ([⮨](#top))

## Operazioni algebriche di base ([⮨](#top))

NumPy ci offre la possibilità di effettuare diversi tipi di operazioni
algebriche di base sugli array. Ad esempio, è possibile sommare due array:

```pycon
>>> a = np.array([1, 2])
>>> b = np.array([3, 4])
>>> a + b
array([4, 6])
```

Possiamo ovviamente anche fare le altre operazioni fondamentali:

```pycon
>>> a + b
array([4, 6])
>>> a - b
array([-2, -2])
>>> a * b
array([3, 8])
>>> a / b
array([0.33333333, 0.5])
>>> b / a
array([3., 2.])
```

> <details open>
> <summary>ℹ️ <em>Moltiplicazione e divisione</em></summary>
>
> Per comprendere appieno il comportamento degli operatori `*` e `/`, dovremo
> parlare del broadcasting. Lo faremo in una delle prossime lezioni.
>
> </details>

## La funzione `sum()` ([⮨](#top))

La funzione `sum(axis=None)` ci permette di sommare tutti gli elementi lungo
l'asse specificato. Ad esempio, per sommare tutti gli elementi di un vettore:

```pycon
>>> a = np.array([1, 2, 3, 4])
>>> a.sum()
10
```

In caso di array multidimensionale, dovremo specificare l'asse. Ad esempio, per
sommare gli elementi per colonna, dovremo passare il parametro `0`:

```pycon
>>> barry = np.array([[1, 2], [3, 4]])
>>> barry.sum(axis=0)
array([4, 6])
```

Per sommare gli elementi per riga, invece, dovremo passare il parametro `1`:

```pycon
>>> barry.sum(axis=1)
array([3, 7])
```

## La funzione `dot()` ([⮨](#top))

La funzione `dot()` ci permette di effettuare l'operazione di moltiplicazione
tra matrici standard:

```pycon
>>> a = np.array([[1, 2]])
>>> b = np.array([[3], [4]])
>>> np.dot(a, b)
array([[11]])
>>> np.dot(b, a)
array([[3, 6],
       [4, 8]])
```

## La funzione `sort()` ([⮨](#top))

Mediante la funzione `sort()` è possibile ordinare gli elementi di un array. Ad
esempio:

```pycon
>>> arry = np.array([2, 1, 5, 3, 7, 4, 6, 8])
>>> np.sort(arry)
array([1, 2, 3, 4, 5, 6, 7, 8])
```

L'array viene ordinato in maniera _ascendente_ (ovvero dall'elemento più
piccolo al più grande). In caso di array $n$-dimensionale, possiamo anche
specificare l'asse lungo il quale avviene l'ordinamento, con il parametro
`axis`. Ad esempio:

```pycon
>>> tarry = np.array([[2, 3, 1], [4, 2, 6], [7, 5, 1]])
>>> tarry
array([[2, 3, 1],
       [4, 2, 6],
       [7, 5, 1]])
```

Per ordinare lungo le colonne:

```pycon
>>> np.sort(tarry, axis=0)
array([[2, 2, 1],
       [4, 3, 1],
       [7, 5, 6]])
```

Per ordinare lungo le righe:

```pycon
>>> np.sort(tarry, axis=1)
array([[1, 2, 3],
       [2, 4, 6],
       [1, 5, 7]])
```

Possiamo anche specificare diversi algoritmi di ordinamento mediante
l'argomento `kind`, che ci permette di scegliere tra il quick sort, il merge
sort e l'heap sort.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Esistono anche altre funzioni per l'ordinamento di un array, come [`argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort),
> [`lexsort()`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort),
> [`searchsorted()`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted)
> e [`partition()`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition).
>
> </details>

## Concatenare due array ([⮨](#top))

Possiamo concatenare due array usando la funzione `concatenate()`:

```pycon
>>> a = np.array([1, 2, 3, 4])
>>> b = np.array([5, 6, 7, 8])
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
```

Si può, anche in questo caso, usare il parametro `axis` per specificare l'asse
lungo il quale concatenare due diversi array:

```pycon
>>> x = np.array([[1, 2], [3, 4]])
>>> y = np.array([[5, 6], [7, 8]])
>>> np.concatenate((x, y), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
>>> np.concatenate((x, y), axis=1)
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])
```

Le dimensioni degli array devono essere _coerenti_ affinché vengano
concatenati. Ad esempio, con il seguente array:

```pycon
>>> z = np.array([[9, 10]])
```

La concatenazione per righe è concessa:

```pycon
>>> np.concatenate((x, z), axis=0)
array([[ 1,  2],
       [ 3,  4],
       [ 9, 10]])
```

mentre la concatenazione per colonne produrrà un errore:

<!-- markdownlint-disable MD013 -->

```pycon
>>> np.concatenate((x, z), axis=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 5, in concatenate
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
```

<!-- markdownlint-enable MD013 -->

## Rimozione e inserimento di elementi in un array ([⮨](#top))

### La funzione `delete()` ([⮨](#top))

La funzione `delete(arr, obj, axis=None)` ci permette di rimuovere uno o più
elementi di un array specificandone gli indici. La funzione accetta i seguenti
parametri:

- `arr`: l'array sul quale vogliamo effettuare l'operazione di rimozione;
- `obj`: gli indici degli elementi da rimuovere;
- `axis`: l'asse su cui vogliamo operare.

Ad esempio, immaginiamo di voler rimuovere il primo elemento di un vettore:

```pycon
>>> arry = np.array([1, 2, 3, 4])
>>> np.delete(arry, 0)
array([2, 3, 4])
```

La funzione può essere anche applicata su più indici usando una sequenza:

```pycon
>>> arry = np.array([1, 2, 3, 4])
>>> np.delete(arry, range(2))
array([3, 4])
```

Possiamo usare anche lo slicing:

```pycon
>>> idx = range(2)
>>> np.delete(arry, idx[0:2])
array([3, 4])
```

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> La precedente notazione può essere rimpiazzata dalla funzione
> `slice(start, stop, step)`, che crea un oggetto di classe `slice` sugli
> indici che vanno da `start` a `stop` con passo `step`. Questo può essere
> usato per scopi analoghi ai precedenti; ad esempio:
>
> ```pycon
> >>> np.delete(arr, slice(0, 2, 1))
> array([3, 4])
> ```
>
> </details>

#### Array multidimensionali e `delete()` ([⮨](#top))

La funzione `delete()` può essere usata anche su array multidimensionali. In
questo caso, è opportuno specificare l'asse su cui operare.

Ad esempio, se vogliamo rimuovere la prima riga dal seguente array, dobbiamo
dare il valore `0` al parametro `axis`:

```pycon
>>> mtrx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> np.delete(mtrx, 0, 0)
array([[4, 5, 6],
       [7, 8, 9]])
```

Invece, se volessimo rimuovere la prima colonna, dovremmo passare il valore
`1`:

```pycon
>>> np.delete(mtrx, 0, 1)
array([[2, 3],
       [5, 6],
       [8, 9]])
```

Se non specificassimo alcun valore per il parametro `axis`, otterremmo questo
il seguente risultato:

```pycon
>>> np.delete(mat, 0)
array([2, 3, 4, 5, 6, 7, 8, 9])
```

In altre parole, non specificando un valore per axis, rimuoveremmo il primo
elemento dell'array "vettorizzato".

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Spesso è preferibile usare, al posto della notazione precedente, una maschera booleana:
>
> ```pycon
> >>> mask = np.array([[True, False, True], [False, False, True], [False, True, True]])
> >>> mtrx[mask]
> array([1, 3, 6, 8, 9])
> ```
>
> </details>

### La funzione `insert()` ([⮨](#top))

La funzione `insert(arr, obj, values, axis=None)` permette di inserire un
elemento all'interno di un array. I parametri accettati dalla funzione sono:

- `arr`: l'array sul quale vogliamo effettuare l'operazione di inserzione;
- `obj`: gli indici su cui inserire i nuovi valori;
- `values`: i valori da inserire agli indici specificati da `obj`;
- `axis`: l'asse su cui vogliamo operare.

Ad esempio, per inserire una nuova riga nella matrice precedente, dovremo
specificare l'indice di riga (`3`), gli elementi della riga da inserire
(`[10, 11, 12]`) e l'asse (`0`):

```pycon
>>> np.insert(mtrx, 3, [10, 11, 12], 0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```

Cambiando l'asse in `1`, si effettua l'inserzione sulle colonne:

```pycon
>>> np.insert(mtrx, 3, [10, 11, 12], 1)
array([[ 1,  2,  3, 10],
       [ 4,  5,  6, 11],
       [ 7,  8,  9, 12]])
```

Non specificando alcun asse, infine, si inserisce l'elemento specificato nella
matrice vettorizzata:

```pycon
>>> np.insert(mtrx, 3, [10, 11, 12])
array([ 1,  2,  3, 10, 11, 12,  4,  5,  6,  7,  8,  9])
```

### La funzione `append()` ([⮨](#top))

La funzione `append(arr, values, axis=None)` permette di inserire in coda ad un
array i valori specificati. I parametri accettati dalla funzione sono:

- `arr`: l'array sul quale vogliamo effettuare l'operazione di inserzione;
- `values`: i valori da inserire in coda all'array;
- `axis`: l'asse su cui vogliamo operare.

Al solito, non specificando l'asse effettuiamo la concatenazione sulla matrice
vettorizzata:

```pycon
>>> np.append(mtrx, [[10, 11, 12]])
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```

Se specifichiamo il valore `0` sul parametro `axis`, effettuiamo la
concatenazione per righe:

```pycon
>>> np.append(mtrx, [[10, 11, 12]], axis=0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```

Se specifichiamo il valore `1` sul parametro `axis`, invece, effettuiamo la
concatenazione per colonne:

```pycon
>>> np.append(mtrx, [[10], [11], [12]], axis=1)
array([[ 1,  2,  3, 10],
       [ 4,  5,  6, 11],
       [ 7,  8,  9, 12]])
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Abbiamo utilizzato rispettivamente, un vettore riga e un vettore colonna.
>
> </details>

## Dimensioni e forma di un array ([⮨](#top))

Esistono diverse proprietà di un array che ne descrivono dimensioni e forma.

Tornando alla matrice `mtrx`, possiamo conoscere il numero di assi mediante
l'attributo `ndarray.ndim`:

```pycon
>>> mtrx.ndim
2
```

Il numero di elementi è invece definito dall'attributo `ndarray.size`:

```pycon
>>> mtrx.size
9
```

L'attributo `ndarray.shape` restituisce invece una tupla di interi che indica
il numero di elementi per ciascuno degli assi dell'array:

```pycon
>>> mtrx.shape
(3, 3)
```

## Modificare le dimensioni di un array ([⮨](#top))

Possiamo modificare le dimensioni di un array mediante la funzione
`reshape(arr, new_shape)`. I parametri passati alla funzione sono:

- `arr`: l'array di cui modificare le dimensioni;
- `new_shape`: le nuove dimensioni dell'array.

Se volessimo modificare le dimensioni di una matrice da $4 \times 4$ a
$2 \times 8$, potremmo usare la funzione `reshape()` come segue:

```pycon
>>> mtrx = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
>>> np.reshape(mtrx, (2, 8))
array([[ 1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16]])
```

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Una forma alternativa è la seguente:
>
> ```pycon
> >>> mtrx.reshape((2, 8))
> array([[ 1,  2,  3,  4,  5,  6,  7,  8],
>        [ 9, 10, 11, 12, 13, 14, 15, 16]])
> ```
>
> Ciò significa che la funzione `reshape()` è sia disponibile nella libreria
> NumPy, sia come metodo sugli oggetti di classe `ndarray`.
>
> </details>
>
> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Le dimensioni dell'array devono essere coerenti con quelle dell'array di
> partenza.
>
> </details>

## Flattening di un array ([⮨](#top))

Abbiamo già visto in precedenza la vettorizzazione di un array, effettuata in
automatico in alcune situazioni (come ad esempio la chiamata di `delete()` o
`insert()` senza specificare il parametro `axis`). Tuttavia, possiamo usare la
funzione `flatten()` per effettuare manualmente questa operazione:

```pycon
>>> mtrx.flatten()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])
```

> <details>
> <summary>ℹ️ <em>La funzione <code>ravel()</code></em></summary>
>
> Un altro modo per vettorizzare un array è utilizzare la funzione `ravel()`,
> che restituisce un risultato analogo alla `flatten()`, a meno di una
> importante differenza: infatti, laddove `flatten()` restituisce una copia
> dell'array vettorizzato, `ravel()` mantiene un riferimento all'array
> originario.
>
> </details>

# Operazioni matriciali ([⮨](#top))

NumPy mette a disposizione il package `linalg`, che permette di effettuare
numerose operazioni matriciali. La maggior parte degli esempi che vedremo nel
seguito prevedono l'utilizzo di questo package, per cui possiamo partire
importandolo.

```pycon
>>> from numpy import linalg
```

## Matrice trasposta ([⮨](#top))

La prima operazione che vediamo non richiede l'uso del modulo `linalg`, ed è
quella che ci permette di ottenere la trasposta di una matrice. Per farlo,
usiamo la funzione `transpose()`:

```pycon
>>> mtrx = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.transpose(mtrx)
array([[1, 4],
       [2, 5],
       [3, 6]])
```

## Matrice inversa ([⮨](#top))

Possiamo calcolare l'inversa di una matrice usando la funzione `inv(mtrx)` del
package `linalg`, dove `mtrx` è la matrice da invertire. Ad esempio:

```pycon
>>> mtrx = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
>>> linalg.inv(mtrx)
array([[0.2 , 0.  , 0.  ],
       [0.  , 0.5 , 0.  ],
       [0.  , 0.  , 0.25]])
```

Ovviamente, la matrice mat deve essere invertibile. Nel caso passassimo una
matrice rettangolare, verrebbe lanciato un `LinAlgError`:

```pycon
>>> mtrx = np.array([[1, 2, 3], [4, 5, 6]])
>>> linalg.inv(mtrx)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 180, in inv
  File "~\<env>\lib\site-packages\numpy\linalg\linalg.py", line 540, in inv
    _assert_stacked_square(a)
  File "~\<env>\lib\site-packages\numpy\linalg\linalg.py", line 203, in _assert_stacked_square
    raise LinAlgError('Last 2 dimensions of the array must be square')
numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
```

Lo stesso accade per una matrice singolare:

```pycon
>>> mtrx = np.array([[1, 1, 1], [2, 2, 2], [0, 0, 1]])
>>> linalg.inv(mtrx)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 180, in inv
  File "~\<env>\lib\site-packages\numpy\linalg\linalg.py", line 545, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "~\<env>\lib\site-packages\numpy\linalg\linalg.py", line 88, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
```

## Prodotti vettoriali e tra matrici ([⮨](#top))

<!-- markdownlint-disable MD024 -->

### La funzione `dot()` ([⮨](#top))

<!-- markdownlint-enable MD024 -->

Nella scorsa lezione abbiamo visto un esempio di uso della funzione
`dot(a, b)`, necessaria a calcolare il prodotto tra matrici tra gli array `a` e
`b`. Ovviamente, si applicano tutte le regole valide per il calcolo del
prodotto tra matrici (ovvero quello relativo alla moltiplicazione righe per
colonne); riassumiamole nella seguente tabella sulla base delle dimensionalità
di `a` ed `b`.

<!-- markdownlint-disable MD013 -->

| Dimensionalità `a`           | Dimensionalità `b`           | Risultato                                   | Note                                                       |
| :--------------------------- | :--------------------------- | :------------------------------------------ | :--------------------------------------------------------- |
| Monodimensionale (vettore)   | Monodimensionale (vettore)   | Prodotto scalare                            |                                                            |
| Bidimensionale (matrice)     | Bidimensionale (matrice)     | Prodotto tra matrici                        | Preferibile la funzione `matmul()`                         |
| Scalare/<br>$n$-dimensionale | $n$-dimensionale/<br>Scalare | Prodotto scalare per array $n$-dimensionale | Preferibile la funzione `multiply(a, b)` o l'operatore `*` |

<!-- markdownlint-enable MD013 -->

Nel caso entrambi gli array siano $n$-dimensionali, si applicano altre regole,
che è possibile recuperare a [questo indirizzo](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot).

### Prodotto interno ([⮨](#top))

Possiamo usare la funzione `inner(a, b)` per calcolare il _prodotto interno_ (o
scalare) tra i vettori `a` e `b`:

```pycon
>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>> np.inner(a, b)
32
```

> <details open>
> <summary>ℹ️ <em>Definizione di prodotto interno</em></summary>
>
> Ricordiamo che per due generici vettori monodimensionali
> $\nu = [\nu_1, \dotsc, \nu_j], \omega = [\omega_1, \dotsc, \omega_j]$, il prodotto
> scalare è dato da:
>
> $$
> p = \sum_{i=1}^j \nu_i \cdot \omega_i
> $$
>
> </details>

Un lettore attento avrà notato che, nella pratica, per vettori
monodimensionali, le funzioni `inner()` e `dot()` restituiscono lo stesso
risultato:

```pycon
>>> np.inner(a, b)
32
>>> np.dot(a, b)
32
```

La differenza tra le due funzioni è visibile quando si utilizzano array a
dimensionalità maggiore di $1$ (anche comuni matrici). Infatti:

```pycon
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.inner(a, b)
array([[17, 23],
       [39, 53]])
>>> np.dot(a, b)   # oppure a.dot(b)
array([[19, 22],
       [43, 50]])
```

In pratica, riprendendo la documentazione:

- per quello che riguarda la funzione `dot()`, questa è equivalente a
  `matmul()`, e quindi rappresenta una moltiplicazione matriciale che, nel caso
  di vettori monodimensionali, equivale al prodotto vettoriale, mentre per $n$
  dimensioni è la somma dei prodotti tra l'ultima dimensione del primo vettore
  e delle dimensioni che vanno da $2$ ad $n$ del secondo;
- per quello che riguarda la funzione `inner()`, rappresenta il prodotto
  vettoriale nel caso ad una dimensione, mentre nel caso di $n$ dimensioni
  rappresenta la somma dei prodotti lungo l'ultima dimensione.

In altri termini:

<!-- TODO: controlla, non mi convince. perché sono uguali? -->
<!-- la documentazione numpy scrive:
```python
# If a is an N-D array and b is an M-D array (where M>=2), it is a sum product
# over the last axis of a and the second-to-last axis of b:
dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])

# More generally, if ndim(a) = r > 0 and ndim(b) = s > 0, explicitly:
np.inner(a, b) = sum(a[:]*b[:])
np.inner(a, b)[i0,...,ir-2,j0,...,js-2]
     = sum(a[i0,...,ir-2,:]*b[j0,...,js-2,:])
``` -->

```pycon
a.dot(b) == sum(a[i, :] * b[:, j])
np.inner(a, b) == sum(a[i, :] * b[j, :])
```

ovvero:

$$
\newcommand{\mtrx}[2]{\begin{pmatrix}#1 \\ #2\end{pmatrix}}
\newcommand{\ms}[4]{#1 \cdot #2 + #3 \cdot #4}

\begin{align*}
{\tt dot()}   &= \mtrx{1 & 2}{3 & 4} \cdot \mtrx{5 & 6}{7 & 8}
               = \mtrx{\ms{1}{5}{2}{7} & \ms{1}{6}{2}{8}}{\ms{3}{5}{4}{7} &
                 \ms{1}{6}{4}{8}}
               = \mtrx{19 & 22}{43 & 50}   \\
{\tt inner()} &= \mtrx{1 & 2}{3 & 4} \cdot \mtrx{5 & 6}{7 & 8}
               = \mtrx{17 & 23}{39 & 53}
\end{align*}
$$

### Prodotto esterno ([⮨](#top))

Possiamo usare la funzione `outer(a, b)` per calcolare il prodotto esterno tra
due vettori. In particolare, dati due vettori $a = [a_1, a_2, \dotsc, a_n]$ e
$b = [b_1, b_2, \dotsc, b_n]$, il prodotto esterno è definito come la matrice
$P$ tale che:

$$
P = \begin{bmatrix}
        a_1 \cdot b_1 & a_1 \cdot b_2 & \cdots & a_1 \cdot b_n  \\
        a_2 \cdot b_1 & a_2 \cdot b_2 & \cdots & a_2 \cdot b_n  \\
        \vdots        & \vdots        & \ddots & \vdots         \\
        a_n \cdot b_1 & a_n \cdot b_2 & \cdots & a_n \cdot b_n
    \end{bmatrix}
$$

Ad esempio:

```pycon
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.outer(a, b)
array([[ 5,  6,  7,  8],
       [10, 12, 14, 16],
       [15, 18, 21, 24],
       [20, 24, 28, 32]])
```

### La funzione `matmul()` ([⮨](#top))

Quando abbiamo parlato della funzione `dot(a, b)` abbiamo visto come sia
possibile usarla per effettuare il prodotto tra matrici. Tuttavia, esiste
un'altra possibilità, che è anche quella consigliata, ovvero usare la funzione
`matmul(a, b)`:

```pycon
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.matmul(a, b)
array([[19, 22],
       [43, 50]])
```

La funzione `matmul()` ha una differenza fondamentale rispetto alla funzione
`dot()`, in quanto non accetta scalari come parametro (anche se è possibile
passare vettori ed array $n$-dimensionali). Esiste in realtà un'altra
differenza importante, che riguarda le operazioni $n$-dimensionali, ma che non
tratteremo in questa sede.

## Potenza di Matrice ([⮨](#top))

La funzione `matrix_power(a, n)` del package `linalg` permette di elevare a
potenza `n` una matrice `a`. Ad esempio:

```pycon
>>> linalg.matrix_power(a, 5)
array([[1069, 1558],
       [2337, 3406]])
```

## Decomposizione ai valori singolari ([⮨](#top))

La _decomposizione ai valori singolari_, detta anche **SVD** dall'acronimo
inglese _Singular Value Decomposition_, è una tecnica di decomposizione di una
matrice che permette di scomporla in modo da semplificarci la vita in alcune
situazioni.

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Per un'approfondimento sui principi alla base della SVD, consultare
> l'[appendice E.1].
>
> </details>

L'implementazione da zero della **SVD** è estremamente complessa; tuttavia,
NumPy ci viene quindi in aiuto con la funzione `svd(mat)` del package `linalg`:

```pycon
>>> (u, s, v) = linalg.svd(a)
>>> u
array([[-0.40455358, -0.9145143 ],
       [-0.9145143 ,  0.40455358]])
>>> s
array([5.4649857 , 0.36596619])
>>> v
array([[-0.57604844, -0.81741556],
       [ 0.81741556, -0.57604844]])
```

## Autovalori e Autovettori ([⮨](#top))

Per calcolare gli autovalori e gli autovettori di una matrice, NumPy ci mette a
disposizione la funzione `eig(a)`, sempre appartenente al package `linalg`, che
restituisce gli autovalori e gli autovettori destri di una matrice quadrata:

```pycon
>>> (v, w) = linalg.eig(a)
>>> v
array([-0.37228132,  5.37228132])
>>> w
array([[-0.82456484, -0.41597356],
       [ 0.56576746, -0.90937671]])
```

## Norma ([⮨](#top))

La funzione `linalg.norm(a)` ci permette di calcolare la norma di una matrice.
Opzionalmente, possiamo specificare tre parametri, ovvero:

- `ord`: rappresenta l'ordine della norma da calcolare (di default, viene
  calcolata la norma di Frobenius);
- `axis`: indica l'asse (o gli assi, in caso di array multidimensionale) su cui
  operare;
- `keepdims`: per restituire, opzionalmente, l'asse su cui viene calcolata la
  norma.

Per calcolare la norma di Frobenius della matrice mat possiamo usare questa
sintassi:

```pycon
>>> linalg.norm(a)
5.477225575051661
```

## Determinante, rango e traccia ([⮨](#top))

Possiamo calcolare rapidamente determinante, rango e traccia di una matrice
mediante le funzioni `det(a)`, `matrix_rank(a)` e `trace(a)`, quest'ultima non
appartenente al package `linalg`. Ad esempio:

```pycon
>>> linalg.det(a)
-2.0000000000000004
>>> linalg.matrix_rank(a)
2
>>> np.trace(a)
5
```

La funzione `trace()` può anche essere usata per calcolare la sommatoria delle
sovra/sotto diagonali specificando il parametro `offset`. Ad esempio:

```pycon
>>> mtrx = np.array([[ 5,  2,  9], [ 2,  3,  1], [ 4, -2, 12]])
>>> np.trace(mtrx, offset=1)
3
>>> np.trace(mtrx, offset=-1)
0
```

## Risoluzione di sistemi di equazioni lineari ([⮨](#top))

Chiudiamo questa (necessariamente breve!) carrellata sulle operazioni di
algebra lineare con la funzione `solve(a, b)`, che permette di risolvere un
sistema di equazioni lineari nel quale la matrice `a` è la matrice dei
coefficienti, mentre il vettore `b` è il vettore dei termini noti. Ad esempio:

```pycon
>>> b = np.array([3, 2, 3])
>>> linalg.solve(mtrx, b)
array([-7.5,  4.5,  3.5])
```

Ovviamente, la matrice `a` deve essere quadrata, mentre il vettore `b` deve
avere esattamente $n$ elementi, con $n$ ordine di `a`!

# Operazioni polinomiali in NumPy ([⮨](#top))

Il modulo `numpy.polynomial.polynomial` ci offre numerose classi e funzionalità
per il trattamento dei polinomi. Vediamo quali sono le principali.

Immaginiamo di avere due diversi polinomi (a cui non assoceremo alcun
significato fisico), ovvero:

$$
\begin{cases}
    c_1 \coloneqq 2x + 1        \\
    c_2 \coloneqq x^2 + 3x + 2
\end{cases}
$$

Vediamo come usare dei metodi forniti dal modulo `polynomial` per effettuare
delle operazioni su di loro.

Prima di partire, però, introduciamo gli oggetti di classe `poly1d`, che ci
permettono di rappresentare in maniera compiuta un polinomio. In particolare,
partendo dai coefficienti di un generico polinomio `p`, potremo ottenere un
oggetto `poly1d` invocando l'omonimo costruttore:

```pycon
p_pol = np.poly1d(p)
```

Il vantaggio principale degli oggetti `poly1d` sta sia nella loro
rappresentazione, sia nel fatto che possono essere direttamente utilizzati
all'interno delle funzioni per il calcolo polinomiale che vedremo in seguito.

## Addizione di polinomi ([⮨](#top))

Per effettuare l'addizione di due polinomi, possiamo usare il metodo
`polyadd(c1, c2)`, che accetta come parametri due vettori `c1` e `c2` che
rappresentano, rispettivamente, i coefficienti del polinomio $1$ e $2$. Volendo
sommare il primo ed il secondo polinomio, potremo scrivere:

```pycon
>>> from numpy.polynomial import polynomial as poly
>>> c1 = (0, 2, 1)
>>> c2 = (1, 3, 2)
>>> poly.polyadd(c1, c2)
array([1., 5., 3.])
```

Questa operazione ci darà il risultato atteso, ovvero $x^2 + 5x + 3$.

Notiamo come le dimensioni di `c1` e di `c2` debbano essere tra loro
_coerenti_. Se infatti omettessimo il coefficiente $0$ del termine di secondo
grado di `c1`, il risultato sarebbe il seguente:

```pycon
>>> c3 = (2, 1)
>>> poly.polyadd(c3, c2)
array([3., 4., 2.])
```

Ovviamente, il risultato precedente può essere errato in base al valore assunto
dal polinomio `c3`.

## Sottrazione di polinomi ([⮨](#top))

Possiamo poi sottrarre due polinomi usando la funzione `polysub(c1, c2)`, i cui
parametri sono identici a quelli passati a `polyadd()`:

```pycon
>>> poly.polysub(c2, c1)
array([1., 1., 1.])
```

## Moltiplicazione di polinomi ([⮨](#top))

Le considerazioni precedenti possono essere banalmente traslate al caso della
moltiplicazione tra polinomi, ottenibile mediante la funzione
`polymul(c1, c2)`:

```pycon
>>> poly.polymul(c1, c2)
array([0., 2., 7., 7., 2.])
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Nelle ultime versioni di NumPy, i coefficienti sono ordinati da quello a
> grado più basso a quello di grado più alto!
>
> </details>

## Divisione tra polinomi ([⮨](#top))

La divisione tra polinomi è un'operazione leggermente più complessa delle
altre, e prevede l'uso della funzione `polydiv(c1, c2)`, che restituirà
stavolta due array: il primo, `q`, rappresenta i coefficienti del polinomio
quoziente, mentre il secondo, `r`, indica i coefficienti del polinomio resto.

Nel nostro caso:

```pycon
>>> (q, r) = poly.polydiv(c1, c2)
>>> q; r
array([0.5])
array([-0.5,  0.5])
```

Anche in questo caso, i coefficienti sono ordinati da quello a grado più basso
a quello a grado più alto.

## Elevazione a potenza ([⮨](#top))

Chiudiamo questa breve panoramica parlando dell'elevazione a potenza di un
polinomio, effettuabile mediante la funzione `polypow(c, pow)`, con `c` vettore
dei coefficienti, e `pow` potenza a cui elevare:

```pycon
>>> poly.polypow(c1, 2)
array([0., 0., 4., 4., 1.])
```

Anche in questo caso, vengono riportati i termini pari a zero nei risultati.

## Valore assunto da un polinomio ([⮨](#top))

Per valutare il valore $y$ assunto dal polinomio per un determinato valore di
$x$, usiamo la funzione `polyval(x, p)`, che accetta come argomento un intero
(o una lista di interi) `x` ed un polinomio `p`.

Se volessimo valutare il valore assunto da $y$ per $x \in [1, 2]$ sulla retta
rappresentata dal polinomio `c1`, ad esempio, potremmo usare `polyval()` come
segue:

```pycon
>>> poly.polyval([1, 2], c1)
array([3., 8.])
```

## Derivate e integrale di funzioni polinomiali ([⮨](#top))

Concludiamo questa breve carrellata con due metodi in grado di calcolare,
rispettivamente, la derivata e l'integrale di una funzione polinomiale.

Il metodo `polyder(p, m)`, infatti, permette di calcolare la derivata di ordine
`m` del polinomio `p` (di default, `m=2`):

```pycon
>>> poly.polyder(c1)
array([2., 2.])
```

L'altro metodo è `polyint(p, m)`, che prevedibilmente calcola l'integrale di
ordine `m` del polinomio `p`:

```pycon
>>> poly.polyint(c1)
array([0., 0., 1., 0.33333333])
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Entrambe le funzioni si aspettano i coefficienti del polinomio passato
> ordinati dal grado più basso a quello più alto.
>
> </details>

# Statistica in NumPy ([⮨](#top))

NumPy ci mette a disposizione diverse funzioni per il calcolo statistico.
Vediamone assieme una breve carrellata.

## Minimo e massimo di un array ([⮨](#top))

Partiamo con due funzioni che possono essere utili per determinare il valore
minimo e massimo di un array `a`, ovvero `amin(a)` ed `amax(a)`. Entrambe
queste funzioni accettano (opzionalmente) un valore per il parametro `axis`,
indicante al solito la direzione lungo la quale viene effettuata l'operazione.

Ad esempio, se volessimo trovare il minimo ed il massimo di un vettore generato
casualmente:

```py
>>> rng = np.random.default_rng(42)
>>> a = rng.integers(low=0, high=10, size=5)
>>> a
array([0, 7, 6, 4, 4], dtype=int64)
>>> np.amin(a)
0
>>> np.amax(a)
7
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Nel codice precedente abbiamo usato la funzione `default_rng()` del package
> `random` di NumPy per generare un vettore di numeri casuali.
>
> </details>

Per una matrice, ed in generale per ogni array $n$-dimensionale, il
procedimento da seguire è analogo:

```py
>>> b = rng.integers(low=0, high=10, size=(3, 3))
>>> b
array([[8, 0, 6],
       [2, 0, 5],
       [9, 7, 7]], dtype=int64)
>>> np.amin(b)
0
>>> np.amax(b)
9
```

Immaginiamo adesso di voler trovare il minimo ed il massimo _per colonna_ per
`b`. Per farlo, specifichiamo il parametro `axis`, che assumerà valore pari a
`0`:

```pycon
>>> np.amin(b, axis=0)
array([2, 0, 5], dtype=int64)
>>> np.amax(b, axis=0)
array([9, 7, 7], dtype=int64)
```

Ovviamente, per trovare il minimo ed il massimo _per riga_, dovremo cambiare il
valore di `axis` in `1`:

```pycon
>>> np.amin(b, axis=1)
array([0, 0, 7], dtype=int64)
>>> np.amax(b, axis=1)
array([8, 5, 9], dtype=int64)
```

Possiamo anche specificare una tupla per il valore del parametro `axis`; in tal
caso, la ricerca del massimo o del minimo avverrà lungo tutti gli assi
specificati dalla tupla. Ad esempio, specificando `(0, 1)`, effettueremo la
ricerca del minimo (o del massimo) elemento nella matrice:

```pycon
>>> np.amin(b, axis=(0, 1))
0
>>> np.amax(b, axis=(0, 1))
9
```

## Percentile e quantile ([⮨](#top))

Ricordiamo che il $q$-_percentile_ di un vettore $v$ di lunghezza $n$ è
definito come il valore pari a $q/100$ calcolato a partire da una copia
ordinata di $v$.

Per fare un esempio, supponiamo di avere un vettore ordinato di elementi che
vanno da $1$ a $10$, e di calcolare il $50$-percentile mediante la funzione
`percentile()` di Numpy:

```pycon
>>> a = np.arange(1, 11)
>>> np.percentile(a, 50)
5.5
```

Esistono diversi modi di calcolare il $q$-percentile, sarebbe opportuno
consultare la [reference](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html)
e l'articolo
[_Sample Quantiles in Statistical Packages, Rob J. Hyndman & Yanan Fan_](https://www.tandfonline.com/doi/abs/10.1080/00031305.1996.10473566).

In realtà, la funzione `percentile(a, q)` usa, per il $50$-percentile, il
calcolo della mediana, per cui è equivalente alla funzione `median(a)`. In
questo caso specifico, avremo un discostamento dal risultato atteso, dovuto ad
errori di interpolazione introdotti da NumPy:

```pycon
>>> np.percentile(a, 50)
5.5
>>> np.median(a)
5.5
```

(Anche se sono uguali (??))

Il concetto di _quantile_ è analogo a quello di percentile; tuttavia, in questo
caso, non abbiamo a che fare con valori percentuali, bensì con valori
normalizzati tra $0$ e $1$. Per cui, se usassimo la funzione `quantile(a, q)`
come in precedenza:

```pycon
>>> np.quantile(a, .5)
5.5
```

Anche le funzioni `percentile()` e `quantile()` prevedono come argomento
opzionale il parametro `axis`. Ad esempio:

```pycon
>>> np.percentile(b, 50, axis=0)
array([8., 0., 6.])
>>> np.percentile(b, 50, axis=1)
array([6., 2., 7.])
```

Come previsto, dando il valore `0` al parametro `axis` avremo il calcolo del
percentile su ciascuna colonna, mentre passando il valore `1` avremo il calcolo
del percentile su ciascuna riga.

## Media aritmetica e media pesata ([⮨](#top))

Per il calcolo del valore medio di un array, NumPy mette a disposizione due
metodi. Il primo è la funzione `average(a, weights)`, che viene usata per
calcolare una media pesata degli elementi di `a` ponderati per gli elementi di
`weights` (a patto che, ovviamente, le dimensioni dei due array siano
coerenti).

Il calcolo che viene effettuato da NumPy con la funzione `average()` è quindi
il seguente:

```pycon
avg = sum(a * weights) / sum(weights)
```

Per cui, se volessimo assegnare un peso maggiore al primo e al quarto elemento
di un array `a` generato casualmente, potremmo fare come segue:

```pycon
>>> w = np.array([3, 1, 1, 3, 1])
>>> np.average(a, weights=w)
3.2222222222222223
```

Il risultato si discosta leggermente dalla semplice media, calcolata come:

```pycon
>>> np.average(a)
4.2
```

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Teniamo sempre a mente che la media è _ponderata_ per la sommatoria dei
> valori assunti dai pesi!
>
> </details>

La funzione `mean(a)` è invece rappresentativa della media _aritmetica_ degli
elementi di un array e equivale alla funzione `average(a)`, senza la specifica
del vettore dei pesi. Ad esempio:

```pycon
>>> np.mean(a)
4.2
```

Concludiamo ricordando che anche in questo caso possiamo specificare il valore
del parametro `axis`:

```pycon
>>> np.mean(b, axis=0)
array([6.33333333, 2.33333333, 6.        ])
>>> np.mean(b, axis=1)
array([4.66666667, 2.33333333, 7.66666667])
```

## Varianza e deviazione standard ([⮨](#top))

Non possono mancare le funzioni `std(a)` e `var(a)`, dedicate al calcolo della
deviazione standard e della varianza di un vettore:

```pycon
>>> np.std(a)
2.4
>>> np.var(a)
5.76
```

Anche in questo caso, possiamo specificare gli assi lungo i quali effettuare
l'operazione desiderata:

```pycon
>>> np.var(b, axis=0)
array([ 9.55555556, 10.88888889,  0.66666667])
>>> np.var(b, axis=1)
array([11.55555556,  4.22222222,  0.88888889])
```

## Matrice di covarianza ([⮨](#top))

La _matrice di covarianza_ è la matrice che racchiude tutti i _coefficienti di_
_correlazione_, che ci permettono di valutare come una certa variabile $x_i$
vari al variare di un'altra variabile $x_j$.

In generale, esistono diversi tipi di coefficienti di correlazione. Il più
semplice è quello di Pearson, che stima una correlazione di tipo _lineare_
(ovvero, aumenta di valore tanto più le due variabili crescono secondo un
rapporto lineare) ed è quello usato dalle funzioni `cov(a)` e `corrcoef(a)`. La
seconda riporta i valori normalizzati dei risultati, ottenibili anche con la
prima. In questo caso, `a` può essere monodimensionale o bidimensionale, ma
ogni _riga_ di `a` rappresenta una _variabile_, mentre ogni _colonna_
rappresenta un'_osservazione_.

Facciamo qualche esempio. Immaginiamo di avere due variabili che assumono
rispettivamente valori `[1, 2, 3]` e `[4, 5, 6]`. In questo caso, è evidente
come la correlazione sia massima, in quanto le osservazioni della seconda
variabile hanno un semplice _offset_ (o _bias_) rispetto a quelle della prima.
Proviamo a calcolare la matrice di correlazione:

```pycon
>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.cov(x)
array([[1., 1.],
       [1., 1.]])
>>> np.corrcoef(x)
array([[1., 1.],
       [1., 1.]])
```

Dato che i coefficienti di correlazione assumono valore pari a $1$, le due
variabili sono fortemente correlate tra loro. Se invece avessimo una situazione
di questo tipo:

```pycon
>>> x = np.array([[1, 2, 3], [-1, -2, -3]])
>>> np.cov(x)
array([[ 1., -1.],
       [-1.,  1.]])
>>> np.corrcoef(x)
array([[ 1., -1.],
       [-1.,  1.]])
```

avremmo che le variabili siano _anti-correlate_, il che significa che quando la
prima aumenta, la seconda diminuisce e viceversa.

Per apprezzare le differenze tra le funzioni `cov()` e `corrcoef()`, dobbiamo
usare valori differenti (e non banali) per `x`. Ad esempio:

```pycon
>>> x = np.array([[2, 3, -1], [1, 5, 2], [4, 2, 2]])
>>> np.cov(x)
array([[ 4.33333333,  2.16666667,  0.66666667],
       [ 2.16666667,  4.33333333, -1.66666667],
       [ 0.66666667, -1.66666667,  1.33333333]])
>>> np.corrcoef(x)
array([[ 1.        ,  0.5       ,  0.2773501 ],
       [ 0.5       ,  1.        , -0.69337525],
       [ 0.2773501 , -0.69337525,  1.        ]])
```

In sostanza, `corrcoef()` restituisce la matrice dei coefficienti $R$, la cui
relazione con la matrice di covarianza $C$ restituita da `cov()` è:

$$
R_{ij} = \frac{C_{ij}}{\sqrt{C_{ii} \cdot C_{jj}}}
$$

I valori di $R$ compresi tra $-1$ e $1$ inclusi.

## Istogramma ([⮨](#top))

Un istogramma offre una visualizzazione grafica dei valori contenuti in un
vettore, raggruppandoli all'interno di un certo numero di partizioni, detto
_bin_.

Ad esempio, una possibile rappresentazione a due partizioni del vettore
$A = [1, 2, 3, 4]$ è data dal vettore $[2, 2]$.
Questo si spiega col fatto che le due partizioni suddividono il range di valori
assunti da $A$ in due parti: la prima inerente agli elementi $1$ e $2$, la
seconda agli elementi $3$ e $4$. Una volta calcolate le partizioni, queste
andranno "riempite" contando il numero di elementi presenti in ciascuna
partizione, il che ci riporta al vettore $[2, 2]$.

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> È possibile specificare, oltre al numero di partizioni, anche gli estremi
> delle stesse, che potrebbero non coincidere con quelli del vettore.
>
> </details>

NumPy permette di ottenere l'istogramma di un vettore mediante l'insieme di
funzioni `histogram(a, bins, range)`, che ci permette di calcolare l'istogramma
(monodimensionale) dell'array `a` in funzione del numero di partizioni
(opzionale) e del range (opzionale). Ad esempio:

```py
>>> a = np.arange(1, 11)
>>> h, b = np.histogram(a)
>>> h; b
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int64)
array([ 1. ,  1.9,  2.8,  3.7,  4.6,  5.5,  6.4,  7.3,  8.2,  9.1, 10. ])
```

In questo caso, abbiamo lasciato il valore di default di `bins`, ovvero $10$.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Notiamo che la funzione `histogram()` restituisce due valori: il primo dato
> dai valori assunti dall'istogramma (ovvero dal numero di elementi che ricade
> in ciascun bin), mentre il secondo dato dai limiti di ogni bin.
>
> </details>

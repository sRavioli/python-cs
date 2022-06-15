# 01 – Introduzione a Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<!-- TOC -->

1. [01 – Introduzione a Python](#01--introduzione-a-python)
2. [Introduzione a Python](#introduzione-a-python)
   1. [Python e la tipizzazione](#python-e-la-tipizzazione)
      1. [Duck Typing](#duck-typing)
3. [L'interprete Python](#linterprete-python)
4. [Operazioni matematiche](#operazioni-matematiche)
   1. [Tabella riassuntiva](#tabella-riassuntiva)
5. [Stringhe](#stringhe)
   1. [Stringhe in righe multiple](#stringhe-in-righe-multiple)
   2. [Concatenazione di Stringhe](#concatenazione-di-stringhe)
      1. [Concatenazione con l'operatore `+`](#concatenazione-con-loperatore-)
      2. [Concatenazione di stringhe _literal_](#concatenazione-di-stringhe-literal)
      3. [Concatenazione con l'operatore `+=`](#concatenazione-con-loperatore--1)
      4. [Concatenazione col metodo `.join()`](#concatenazione-col-metodo-join)
      5. [Concatenazione con il `%`-formatting](#concatenazione-con-il--formatting)
      6. [Concatenazione con il metodo `.format()`](#concatenazione-con-il-metodo-format)
      7. [Concatenazione con le _f_-strings](#concatenazione-con-le-f-strings)
      8. [Che metodo usare?](#che-metodo-usare)
   3. [Indicizzazione delle stringhe](#indicizzazione-delle-stringhe)
   4. [Slicing su stringhe](#slicing-su-stringhe)
   5. [Lunghezza di una stringa](#lunghezza-di-una-stringa)
   6. [Immutabilità di una stringa](#immutabilità-di-una-stringa)
6. [Liste](#liste)
   1. [Concatenazione, indicizzazione e slicing su liste](#concatenazione-indicizzazione-e-slicing-su-liste)
      1. [Esempi](#esempi)
   2. [Mutabilità di una lista](#mutabilità-di-una-lista)
   3. [Operazioni sulle liste](#operazioni-sulle-liste)
   4. [Le liste sono eterogenee](#le-liste-sono-eterogenee)

<!-- /TOC -->
</details>

# Introduzione a Python

Prima di iniziare a parlare del linguaggio Python, è opportuno verificare che
l'interprete sia installato nel nostro sistema. Per farlo, apriamo un
terminale (Shell o Command Prompt, a seconda del nostro sistema), e scriviamo:

```sh
$ python --version
Python 3.9.7
```

> Il simbolo `$` indica l'input in bash. È importante che la versione di Python
> sia `3.9.n`.
>
> <details>
>     <summary>Per i curiosi</summary>
>
> - [What does ~$ stand for?](https://askubuntu.com/a/304023);
> - [What does the $ mean when running commands?](https://stackoverflow.com/a/19986337/14879005);
> - [What is the origin of the UNIX $ (dollar) prompt?](https://superuser.com/a/57613).
>
> </details>

<!-- https://stackoverflow.com/a/19986337/14879005 -->

Se il messaggio precedente non compare, sarà necessario installare python o
seguendo le istruzioni del [sito ufficiale](https://www.python.org) o da una
distribuzione come [Anaconda](https://www.anaconda.com).

> Se Anaconda non fa per te, prova [miniconda](https://docs.conda.io/en/latest/miniconda.html).

A differenza del C, Python è un linguaggio _pseudocompilato_: un interprete si
occupa di analizzare il codice sorgente (semplici file testuali con estensione
`.py`) e, se sintatticamente corretto, di eseguirlo. In Python, non esiste una
fase di compilazione separata (come avviene in C, per esempio) che generi un
file eseguibile partendo dal sorgente.

Dunque dopo aver installato l'interprete lo si potrà chiamare da riga di
comando e interagirvi.

> Questo non significa che non si possano scrivere programmi "classici".

Facciamolo:

```pycon
$ python
Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

> <details>
>     <summary>Se scaricato tramite Anaconda</summary>
>
> ```pycon
> $ python
> Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
> Type "help", "copyright", "credits" or "license" for more information.
> >>>
> ```
>
> </details>

Possiamo ora chiuderlo, lo useremo in seguito:

```pycon
>>> quit()
```

> A differenza della shell che usa `$`, indichiamo con `>>>` l'input
> nell'interprete Python.

## Python e la tipizzazione

Python è un linguaggio a tipizzazione dinamica. Questo significa che
l'interprete valuta il tipo di variabile a _runtime_ e, dato che il tipo può
cambiare durante l'esecuzione del programma, non è necessario specificarlo
al momento della dichiarazione della variabile.

Ma questo che significa? Immaginiamo di dover dichiarare una variabile in
C/C++, scriveremo

```CPP
int var = 0;
```

Abbiamo dichiarato che `var` è un intero e gli abbiamo assegnato il valore di
`0`. In Python sarà sufficiente scrivere

```python
var = 0
```

Vogliamo ora convertire `var` da tipo intero a tipo `float`. In C++ dovremo
effettuare il _casting_

```CPP
float fVar = float(var);
fVar + 1.1;
```

Questo passaggio non è necessario in Python, è possibile effettuare
direttamente le operazioni desiderate

```python
var + 1.1   # ovvero 1.1
```

Questo è, apparentemente, una grande semplificazione poiché non è più
necessario preoccuparsi del tipo della variabile. Non è però tutto oro ciò
che luccica: per comprenderlo, infatti è il momento di parlare del (pilatesco)
principio del _duck typing_.

### Duck Typing

Il nome del concetto si riferisce al _duck test_ attribuito a James W. Riley che
afferma:

> If it walks like a duck and it quacks like a duck, then it must be a duck.

che in italiano sarebbe "Se cammina come un papero, e starnazza come un papero,
allora dev'essere un papero". Ma che significa?

Immaginiamo, tramite l'interprete Python, di assegnare alla nostra variabile
`var` il valore di `1`. Per l'interprete `var` si _comporta_ come un numero
intero e quindi stabilisce che lo sia.

Proviamo a sommare a `var` il valore `1.1`, il risultato sarà un numero
decimale, `2.1`, quindi l'interprete "cambierà idea" poiché i comportamenti
assunti da `var` sono assimilabili ad una variabile di tipo `float`.

<!-- Possiamo verificarlo con l'interprete

```pycon
$ python
Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> var = 1
>>> type(var)
<class 'int'>
>>> type(var + 1.1)
<class 'float'>
>>>
```

> Abbiamo invocato la funzione `type()`, che usiamo per conoscere il tipo della
> variabile `var`. Vedremo più avanti cosa sono le funzioni. -->

L'utilità del _duck typing_ è evidente: permette allo sviluppatore di omettere
delle operazioni di casting, rendendo il codice più semplice da scrivere e
mantenere. Tuttavia, **bisogna** tenere conto di questa proprietà nel momento
in cui si usano classi e oggetti, dato che l'interprete proverà ad inferire
ed usare automaticamente un tipo in base al contesto in cui viene usata la
variabile, con le comodità (ma anche i disastri) che questo comporta.

# L'interprete Python

Nella sezione [introduttiva](#introduzione-a-python) abbiamo visto come
installare Python, in modo da avere un ambiente di lavoro accessibile da riga di
comando. Apriamo una shell (Powershell, bash, etc.) e invochiamo l'interprete
usando il seguente comando:

```pycon
$ python
Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Possiamo ora utilizzare Python in maniera interattiva.

# Operazioni matematiche

Possiamo usare l'interprete come se fosse una calcolatrice, semplicemente
digitiamo le operazioni che vogliamo eseguire e premiamo <kbd>Enter</kbd>.
Proviamo con le quattro operazioni aritmetiche:

```pycon
>>> 2 + 2
4
>>> 4 - 1
3
>>> 3 * 8
24
>>> 10 - 2 * 4
2
>>> 24 / 2
12.0
```

Notiamo immediatamente una stranezza nella divisione, il risultato è di tipo
`float` nonostante i due operandi fossero di tipo `int`.

> <details>
>     <summary>Possiamo verificarlo...</summary>
>
> ... invocando la _funzione_ `type()` che ci permette di verificare quale sia
> il tipo di una variabile. Vedremo in seguito cosa è una funzione.
>
> ```pycon
> >>> type(24); type(2)
> <class 'int'>
> <class 'int'>
> >>> type(24 / 2)
> <class 'float'>
> ```
>
> </details>

Questo accade perché le divisioni restituiscono **sempre** un numero in virgola
mobile. Proviamo nuovamente:

```pycon
>>> 16 / 3
5.333333333333333
>>> 2 / 2
1.0
```

Sono presenti altri tre operatori, vediamoli:

```pycon
>>> 16 // 3
5
>>> 16 % 3
1
>>> 16 ** 3
4096
```

Il primo operatore (`//`) è quello della _divisione intera_ e dunque restituisce
il quoziente di una divisione, il secondo (`%`) è l'operatore _modulo_ che
quindi sarebbe il resto di una divisione, l'ultimo (`**`) è l'elevazione a
potenza.

> <details>
> <summary>ℹ️ <em>Tipi numerici in Python</em></summary>
>
> Finora abbiamo parlato soltanto di numeri interi o decimali. Python supporta
> anche altri tipi, ad esempio `Decimal` e `Fraction`. È inoltre presente un
> supporto nativo per i numeri complessi, `j` indica la parte immaginaria:
>
> ```pycon
> >>> 1j + 3j
> 4j
> ```
>
> </details>

Abbiamo visto vari operatori matematici, riassumiamoli.

## Tabella riassuntiva

| Operatore | Descrizione          |
| --------: | :------------------- |
|       `+` | Addizione            |
|       `-` | Sottrazione          |
|       `*` | Moltiplicazione      |
|       `/` | Divisione            |
|      `//` | Divisione intera     |
|       `%` | Modulo               |
|      `**` | Elevazione a potenza |

# Stringhe

In Python le stringhe possono indifferentemente essere racchiuse tra virgolette
singole (`'...'`) o doppie (`"..."`).

```pycon
>>> "una stringa"
'una stringa'
>>> 'un\'altra stringa'
"un'altra stringa"
```

Notiamo nella seconda istruzione l'uso del carattere di escape (`\`) che
precede l'apostrofo. Se venisse omesso, l'interprete ci restituirebbe un errore
sintattico (`SyntaxError`):

```pycon
>>> 'un'altra stringa'
  File "<stdin>", line 1
    'un'altra stringa
            ^
SyntaxError: invalid syntax
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Tutti i caratteri preceduti dal simbolo `\` saranno interpretati come
> dei caratteri speciali, a meno di aggiungere il simbolo `r` prima dell'inizio
> della stringa:
>
> ```pycon
> >>> print('C:\nuova_cartella')
> C:
> uova_cartella
> >>> print(r'C:\nuova_cartella')
> C:\nuova_cartella
> ```
>
> In parole povere, `r'...'` viene interpretata letteralmente, ignorando le
> sequenze di escape (`'\n'`, etc.).
>
> </details>

## Stringhe in righe multiple

> <details>
> <summary>ℹ️ <em>Stringhe e liste</em></summary>
>
> La maggior parte dei concetti che vedremo nel seguito sono applicabili anche
> alle liste. Anzi, per essere precisi, derivano proprio dalle liste, in quanto
> Python considera una stringa un particolare tipo di lista.
>
> </details>

Le stringhe possono articolarsi su più righe. Per stampare una stringa
in righe multiple è necessario usare le _triple-quotes_, ovvero tre virgolette
di seguito, ad indicare inizio e fine della stringa:

```pycon
>>> print("""Questo è un
... esempio di
... stringa \
... multilinea""")
Questo è un
esempio di
stringa multilinea
```

Possiamo usare anche le virgolette singole:

```pycon
>>> print('''Altra stringa
... multi\
... linea''')
Altra stringa
multilinea
```

Notiamo l'utilizzo del backslash (`\`). Inserire questo carattere comunica
all'interprete di non inserire il carattere _newline_ (`\n`) al termine della
riga. Infatti viene stampato `linea` subito dopo `multi\` generando così
`multilinea`.

## Concatenazione di Stringhe

Python permette di concatenare le stringhe in vari modi. Vediamoli.

### Concatenazione con l'operatore `+`

Il metodo più semplice per concatenare molteplici stringhe è quello di usare
l'operatore `+`:

```pycon
>>> strg = "concatenazione" + " col +"
>>> strg
'concatenazione col +'
```

L'operatore `+` funziona sia per le stringhe _literal_ che per le variabili. Ad
esempio:

```pycon
>>> str1 = "stringa"
>>> str2 = str1 + " concatenata col +"
>>> str2
'stringa concatenata col +'
```

### Concatenazione di stringhe _literal_

Per concatenare due o più stringhe _literal_, basta piazzarle una dopo l'altra.
Per esempio:

```pycon
>>> strg = "Stringa" " concatenata"
>>> strg
'Stringa concatenata'
```

> ✏️ Nota
>
> Questo approccio non funzionerà per le variabili di tipo stringa.
>
> <details>
>     <summary>Infatti...</summary>
>
> ... se provassimo a concatenare un _literal_ e una variabile otterremo il
> seguente errore:
>
> ```pycon
> >>> strg = "str"
> >>> strg "inga"
>   File "<stdin>", line 1
>     strg "inga"
>         ^
> SyntaxError: invalid syntax
> ```
>
> Lo stesso errore si presenterebbe se al posto della variabile `strg` usassimo
> il risultato di una operazione di concatenazione:
>
> ```pycon
> >>> ("st" + "r") "inga"
>   File "<stdin>", line 1
>     ("st" + "r") "inga"
>                  ^
> SyntaxError: invalid syntax
> ```
>
> In questi casi sarebbe meglio usare l'operatore standard `+`
>
> </details>

### Concatenazione con l'operatore `+=`

Simile all'operatore `+`, può essere usato per concatenare più stringhe. Ad
esempio:

```pycon
>>> strg = "stringa"
>>> strg += " concatenata"
>>> strg
'stringa concatenata'
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Scrivere `strg += "..."` equivale a scrivere `strg = strg + "..."`
>
> </details>

### Concatenazione col metodo `.join()`

Il metodo `.join()` ci permette di concatenare una lista di stringhe in una
singola stringa:

```pycon
>>> str1 = "stringa"
>>> str2 = "concatenata"
>>> "".join([str1, str2])
'stringaconcatenata'
```

Esso ci consente di definire il delimitatore tra le stringhe. Ad esempio:

```pycon
>>> str1 = "stringa"
>>> str2 = "concatenata"
>>> " ".join([str1, str2])
'stringa concatenata'
```

Possiamo anche usare la virgola:

```pycon
>>> str1 = "una"
>>> str2 = "stringa"
>>> str3 = "concatenata"
>>> ",".join([str1, str2, str3])
'una,stringa,concatenata'
```

### Concatenazione con il `%`-formatting

Gli oggetti di tipo stringa offrono la possibilità di utilizzare l'operatore `%`
per la formattazione delle stesse. Può essere anche usato per concatenare le
stringhe:

```pycon
>>> str1 = "una"
>>> str2 = "stringa"
>>> str3 = "concatenata"
>>> "%s %s %s" % (str1, str2, str3)
>>> 'una stringa concatenata'
```

In questo esempio, Python sostituisce il `%s` nel _literal_ con la variabile
di tipo stringa corrispondente nelle parentesi tonde che seguono l'operatore
`%`.

### Concatenazione con il metodo `.format()`

È possibile concatenare delle stringhe col metodo `.format()`. Ad esempio:

```pycon
>>> str1 = "concatenazione"
>>> str2 = "di stringhe"
>>> str3 = "in Python"
>>> "{} {} {}".format(str1, str2, str3)
'concatenazione di stringhe in Python'
```

In questo esempio, utilizziamo le parentesi graffe `{}` nel _literal_ e passiamo
la stringa da concatenare al metodo `.format()`. Quest'ultimo sostituisce le
parentesi graffe `{}` con la stringa corrispondente nell'argomento del metodo.

### Concatenazione con le _f_-strings

Python 3.6 introduce le _f_-strings per formattare l'output in maniera più
elegante e concisa. Possiamo usare le _f_-strings per concatenare le stringhe.
Vediamo come:

```pycon
>>> str1 = "concatenazione"
>>> str2 = "di stringhe"
>>> str3 = "in Python"
>>> f"{str1} {str2} {str3}"
'concatenazione di stringhe in Python'
```

### Che metodo usare?

Nonostante sono presenti molteplici modi per concatenare stringhe in Python, è
raccomandato usare o l'operatore standard `+` o il metodo `.join()` o il metodo
`.format()` o le _f_-strings.

## Indicizzazione delle stringhe

Python definisce le stringhe come degli _array di caratteri_, dunque è possibile
indicizzarli. Ad esempio:

```pycon
>>> strg = "Python"
>>> strg[0]
'P'
```

Notiamo che Python (e molti altri linguaggi) hanno come primo indice lo `0`.
Dunque per accedere al primo carattere, useremo l'indice `0` e **non**
l'indice `1`.

Anche i singoli caratteri sono considerati come delle stringhe ma di lunghezza
unitaria:

```pycon
>>> lettera = "P"
>>> lettera[0]
'P'
```

Gli indici che usiamo per accedere alle stringhe possono essere anche negativi,
Python dunque considererà gli elementi che vanno da destra verso sinistra.
Ad esempio:

```pycon
>>> strg[-1]
'n'
```

## Slicing su stringhe

L'operazione, detta di _slicing_, permette di estrarre una determinata parte di
una stringa. In generale, il comando, assume il seguente aspetto:

```python
strg[<inizio>:<fine>:<step>]
```

sono tutti e tre dei valori numerici interi, per la precisione:

- `<inizio>` rappresenta la posizione (indice) da cui far partire lo slicing;
- `<fine>` rappresenta la posizione (indice) in cui fermarsi per lo slicing;
- `<step>` rappresenta l'incremento con cui procedere.

Ad esempio:

```pycon
>>> strg = "slicing"
>>> strg[0:2]   # è come scrivere strg[0:2:1]
'sl'
>>> strg[2:5]
'ici'
>>> strg[0:6:2]
'sii'
```

Dunque lo `<step>` è di default pari a `1` e quindi può essere omesso.

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> L'elemento di indice `<inizio>` sarà **incluso** nella stringa finale, al
> contrario, l'elemento di indice `<fine>` verrà **escluso**, infatti:
>
> ```pycon
> >>> strg[0:2]
> 'sl'   # s ha indice 0, l ha indice 1
> ```
>
> </details>

Per stampare tutti i caratteri che precedono `<fine>` (escluso) possiamo usare
`[:<fine>]`. Ad esempio:

```pycon
>>> strg[:5]
'slici'
```

Per stampare tutti i caratteri che seguono `<inizio>` (incluso) possiamo usare
`[<inizio>:]`. Ad esempio:

```pycon
>>> strg[2:]
'icing'
```

Anche le stringe supportano gli indici negativi. Ad esempio se volessimo
stampare tutti i caratteri dalla terzultima lettera in poi, possiamo scrivere:

```pycon
>>> strg[-3:]
'ing'
```

Se invece volessimo stampare tutti fino alla terzultima lettera (esclusa),
possiamo scrivere:

```pycon
>>> strg[:-3]
'slic'
```

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Per ottenere l'intera stringa in un'operazione di slicing basta non inserire
> né `<inizio>` né `<fine>` né `<step>`. Ad esempio:
>
> ```pycon
> >>> strg[:]
> 'slicing'
> ```
>
> </details>

Un modo per ricordarsi il funzionamento dello slicing consiste nel pensare che
gli indici siano compresi tra i caratteri della stringa. L'estremo sinistro del
primo carattere avrà indice `0`, l'estremo destro dell'ultimo carattere di una
stringa di `n` caratteri avrà indice `n`. Ad esempio:

```txt
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

Nella prima riga di numeri sono presenti gli indici delle posizioni `0...6`
nella stringa; nella seconda riga sono presenti gli indici negativi
corrispondenti. Lo slicing da `i` a `j` consisterà di tutti i caratteri compresi
tra gli estremi di indice rispettivamente `i` e `j`.

## Lunghezza di una stringa

Per ottenere la lunghezza di una stringa possiamo usare la funzione `len()`:

```pycon
>>> strg = "stringa"
>>> len(strg)
7
```

## Immutabilità di una stringa

In Python le stringhe sono _immutabili_ e come indica la parola stessa, **non**
possono essere modificate. Se, ad esempio, provassimo a ridefinire uno o più
elementi a cui accediamo mediante indice, otterremo un errore:

```pycon
>>> strg = "stringa"
>>> strg[0] = "t"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Possiamo assegnare alla variabile la stringa modificata:
>
> ```pycon
> >>> strg = "ttringa"
> >>> strg
> 'ttringa'
> ```
>
> Facendo questo però, non sarà più possibile accedere al valore precedente di
> `str` (`"stringa"`), esso non viene eliminato immediatamente dalla memoria,
> però non c'è più modo di accedervi.
>
> Per evitare questo spiacevole inconveniente, possiamo assegnare il valore
> modificato ad una variabile differente:
>
> ```pycon
> >>> str1 = "ttringa"
> >>> str1
> 'ttringa'
> >>> str
> 'stringa'
> ```
>
> </details>

# Liste

Come detto precedentemente, le stringhe non sono altro che un caso particolare
di una lista. Dunque cos'è una lista?

La lista è uno dei quattro tipi di strutture _built-in_ che Python offre per
memorizzare delle sequenze di dati. Esse sono concettualmente simili agli
_array_ di altri linguaggi di programmazione come il C, seppur con alcune
significative differenze.

Una lista è, appunto, una lista di elementi separati da una virgola e
racchiusi tra parentesi quadre (`[...]`). Dichiariamo, ad esempio una lista di
numeri:

```pycon
>>> lst = [0, 1, 2, 3, 4]
>>> lst
[0, 1, 2, 3, 4]
```

## Concatenazione, indicizzazione e slicing su liste

Come per le stringhe anche per le liste è possibile effettuare operazioni di
indicizzazione, slicing e concatenazione:

```pycon
>>> lst = [0, 1, 2, 3, 4, 5]
>>> lst[0]
0
>>> lst[2:]
[2, 3, 4, 5]
>>> lst_2 = [6, 7, 8]
>>> lst + lst_2
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> lst + [6]
[0, 1, 2, 3, 4, 5, 6]
```

Possiamo dunque accedere ai vari elementi di una lista attraverso l'utilizzo
degli indici. Questi ultimi si comportano allo stesso modo di quelli delle
stringhe. D'altronde le stringhe sono un caso particolare di lista.

### Esempi

Prendiamo in considerazione la stringa:

```pycon
>>> lst = [0, 1, 2, 3, 4, 5, 6]
```

Stampiamo ora tutti gli elementi di indice pari:

```pycon
>>> lst[0::2]
[0, 2, 4, 6]
```

Oppure tutti gli elementi di indice pari, a partire dal terzultimo:

```pycon
>>> lst[-3::2]
[4, 6]
```

Partendo dal terzultimo elemento, arriviamo al primo:

```pycon
>>> lst[-3::-1]
[4, 3, 2, 1, 0]
```

Partendo dall'ultimo elemento arriviamo al terzultimo elemento, in ordine
inverso:

```pycon
>>> lst[:3:-1]
[6, 5, 4]
```

Prendiamo gli ultimi tre elementi, in ordine inverso:

```pycon
>>> lst[len(lst) - 1:len(lst) - 4:-1]
[6, 5, 4]
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Abbiamo utilizzato la _funzione_ `len()`, questa ci restituisce la lunghezza
> di un qualsiasi tipo di struttura dati.
>
> </details>

Prendiamo gli elementi di indice pari, in ordine inverso:

```pycon
>>> lst[::-2]
[6, 4, 2, 0]
```

## Mutabilità di una lista

Al contrario delle stringhe, le liste sono oggetti _mutabili_, dunque possiamo
modificarne il contenuto. Ad esempio:

```pycon
>>> lst = [0, 1, 2, 3, 4, 5]
>>> lst[0] = 99
lst
[99, 1, 2, 3, 4, 5]
```

Gli elementi che compongono una lista non devono necessariamente essere dei
numeri.

## Operazioni sulle liste

Si possono effettuare varie operazioni su una lista. Ad esempio, possiamo
eliminare degli elementi di una liste con `[]` combinato all'operazione di
slicing:

```pycon
>>> lst[4:] = []
>>> lst
[0, 1, 2, 3]
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> L'oggetto `[]` non è altro che una lista vuota. Stiamo sostituendo tutti gli
> elementi selezionati dall'operazione di slicing, con una lista vuota.
>
> </details>
>
> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Possiamo eliminare ogni singolo elemento contenuto in una lista utilizzando lo
> slicing e la lista vuota `[]`:
>
> ```pycon
> >>> lst[:] = []
> >>> lst
> >>> []
> ```
>
> Possiamo anche omettere l'operazione di slicing:
>
> ```pycon
> >>> lst = [0, 1, 2, 3, 4, 5]
> >>> lst
> [0, 1, 2, 3, 4, 5]
> >>> lst = []
> >>> lst
> []
> ```
>
> </details>

Possiamo inoltre aggiungere degli elementi in coda ad una lista col metodo
`.append()`, ad esempio:

```pycon
>>> lst.append(6)
>>> lst
[0, 1, 2, [3, '4', 5], 6]
```

Possiamo ovviamente aggiungere anche una lista, ad esempio:

```pycon
>>> lst.append([7, 8])
>>> lst
[0, 1, 2, [3, '4', 5], 6, [7, 8]]
```

## Le liste sono eterogenee

Una lista può contenere elementi tra lista eterogenei, ad esempio:

```pycon
>>> lst = [0, 1, 2, '3']
>>> lst
[0, 1, 2, '3']
```

Essa può contenere anche degli iterabili, come altre liste. Questo permette di
avere delle _liste di liste_, ad esempio:

```pycon
>>> lst = [0, 1, 2, [3, '4', 5]]
>>> lst
[0, 1, 2, [3, '4', 5]]
```

Se volessimo accedere alla lista più interna, scriveremo:

```pycon
>>> lst[3]
[3, '4', 5]
```

Per accedere ad un elemento della lista più interna, scriveremo:

```pycon
>>> lst[3][1]
'4'
```

Se provassimo ad accedere ad un elemento della lista interna che non esiste,
otterremmo il seguente errore:

```pycon
>>> lst = [0, 1, 2, [3, '4', 5]]
>>> lst[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

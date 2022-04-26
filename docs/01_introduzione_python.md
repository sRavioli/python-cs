# 01 – Introduzione a Python

> Corso di Python per il Calcolo Scientifico

> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it


<details>
    <summary>Outline</summary>

<!-- TOC -->

- [01 – Introduzione a Python](#01--introduzione-a-python)
- [Introduzione a Python](#introduzione-a-python)
    - [Python e la tipizzazione](#python-e-la-tipizzazione)
        - [Duck Typing](#duck-typing)
- [L'interprete Python](#linterprete-python)

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

> Il simbolo `$` indica l'input in bash. È importante che la versione di Python sia `3.9.n`.
>
> <details>
>     <summary>Per i curiosi</summary>
>
> -   [What does ~$ stand for?](https://askubuntu.com/a/304023);
> -   [What does the $ mean when running commands?](https://stackoverflow.com/a/19986337/14879005);
> -   [What is the origin of the UNIX $ (dollar) prompt?](https://superuser.com/a/57613).
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

che in italiano sarabbe "Se cammina come un papero, e starnazza come un papero,
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

```sh
$ python
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
> ```pycon
> >>> type(24); type(2)
> <class 'int'>
> <class 'int'>
> >>> type(24 / 2)
> <class 'float'>
> ```
> </details>

Questo accade perché le divisioni restituiscono **sempre** un numero in virgola
mobile. Proviamo nuovamente:

```pycon

```

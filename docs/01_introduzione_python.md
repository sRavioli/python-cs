# 01 – Introduzione a Python

> Corso di Python per il Calcolo Scientifico

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<!-- TOC -->

- [01 – Introduzione a Python](#01--introduzione-a-python)
    - [Introduzione a Python](#introduzione-a-python)
    - [L'interprete di Python](#linterprete-di-python)
        - [Python e la tipizzazione](#python-e-la-tipizzazione)
        - [Duck Typing](#duck-typing)

<!-- /TOC -->
</details>

## Introduzione a Python

Prima di iniziare a parlare del linguaggio Python, è opportuno verificare che
l'interprete sia installato nel nostro sistema. Per farlo, apriamo un
terminale (Shell o Command Prompt, a seconda del nostro sistema), e scriviamo:

```sh
~$ python --version
Python 3.9.7
```

> I simboli `~$` indicano l'input in bash. È importante che la versione di Python sia `3.9.n`.
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


## L'interprete di Python

A differenza del C, Python è un linguaggio _pseudocompilato_: un interprete si
occupa di analizzare il codice sorgente (semplici file testuali con estensione
`.py`) e, se sintatticamente corretto, di eseguirlo. In Python, non esiste una
fase di compilazione separata (come avviene in C, per esempio) che generi un
file eseguibile partendo dal sorgente.

Dunque dopo aver installato l'interprete lo si potrà chiamare da riga di
comando e interagirvi.

> Questo non significa che non si possano scrivere programmi "classici".

Facciamolo:

```sh
~$ python
Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

> <details>
>     <summary>Se scaricato tramite Anaconda</summary>
>
> ```bash
> ~$ python
> Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
> Type "help", "copyright", "credits" or "license" for more information.
> >>>
> ```
> </details>

Possiamo ora chiuderlo, lo useremo in seguito:

```py
>>> quit()
```


### Python e la tipizzazione

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
var + 1.1   # ovvero 0 + 1.1 = 1.1
```

Questo è, apparentemente, una grande semplificazione poiché non è più
necessario preoccuparsi del tipo della variabile. Non è però tutto oro ciò
che luccica: per comprenderlo, infatti è il momento di parlare del (pilatesco)
principio del _duck typing_.

### Duck Typing

Il nome del concetto si riferisce al duck test attribuito a James W. Riley che
afferma:

> If it walks like a duck and it quacks like a duck, then it must be a duck.

ovvero, all'incirca,

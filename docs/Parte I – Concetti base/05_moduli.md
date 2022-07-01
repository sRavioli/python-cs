# 05 – Moduli

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<a name="top"></a>

<!-- TOC -->

1. [05 – Moduli](#05--moduli)
   1. [Script e Moduli (⮨)](#script-e-moduli-)
   2. [Primo script (⮨)](#primo-script-)
      1. [I moduli (⮨)](#i-moduli-)
         1. [I moduli `geometria` e `trigonometria` (⮨)](#i-moduli-geometria-e-trigonometria-)
      2. [Utilizzare gli `import` (⮨)](#utilizzare-gli-import-)
      3. [Alias (⮨)](#alias-)
   3. [La funzione `dir()` (⮨)](#la-funzione-dir-)
      1. [Moduli della libreria standard (⮨)](#moduli-della-libreria-standard-)
   4. [Packages](#packages)

<!-- /TOC -->

</details>

## Script e Moduli ([⮨](#top))

Usando Python, la tentazione è quella di interagire direttamente con
l'interprete, lanciandolo da terminale e eseguendo volta per volta, riga per
riga le istruzioni necessarie. Questo approccio, seppur immediato, presenta
diversi svantaggi. Ad esempio:

- non avremo a disposizione il syntax highlighting che un normale IDE offre;
- non potremo recuperare il codice una volta chiuso l'interprete;
- non potremo né modificato, né verificare facilmente il funzionamento del
  codice.

È evidente che usare l'interprete non sia un modo ottimale di sviluppare codice
in Python. Di conseguenza sarà necessario definire, mediante una IDE di
riferimento, degli script che saranno salvati sotto forma di file con estensione
`.py`. Ognuno dei quali conterrà una serie di istruzioni necessarie
all'esecuzione del programma.

## Primo script ([⮨](#top))

Proviamo a creare il primo script in Python. Per farlo, apriamo una IDE come
Visual Studio Code e creiamo un file chiamato `main.py`. All'interno del file
inseriamo il seguente codice:

```python
# main.py
def hello_world():
    print("Hello, world!")


hello_world()
```

Apriamo ora un terminale e spostiamoci nella cartella nel quale è contenuto lo
script e eseguiamolo:

```sh
$ cd path/to/script
$ python main.py
Hello, world!
```

Le istruzioni precedenti servono a:

1. cambiare cartella (`cd` sta per _change directory_), spostandoci nella
   cartella dove risiede lo script;
2. invocare l'interprete Python per lanciare lo script.

L'ultima riga è l'output dello script Python che abbiamo eseguito.

### I moduli ([⮨](#top))

Quando le dimensioni della _code base_ (ovvero la quantità di codice presente
nel programma) iniziano ad essere particolarmente grandi, sarebbe opportuno
adottare un approccio modulare, separando in file differenti parti di codice
differenti. Ad esempio, immaginiamo di voler scrivere un programma che definisca
delle funzioni per calcolare l'area delle principali figure geometriche.
Modifichiamo il file `main.py` come segue:

```python
# main.py
def calc_area_quadrato(lato):
    return lato ** 2


def calc_area_rettangolo(base, altezza):
    return base * altezza


def calc_area_triangolo(base, altezza):
    return (base * altezza) / 2

area_quadrato = calc_area_quadrato(4)
area_rettangolo = calc_area_rettangolo(2, 3)
area_triangolo = calc_area_triangolo(2, 3)
```

Vogliamo adesso una funzione di calcolo trigonometrico:

```python
# main.py
import math

def calc_tangente(angolo):
    return math.sin(angolo) / math.cos(angolo)


tan_pi = calc_tangente(math.pi)
```

Il codice di `main.py` comprenderà funzioni di tipo trigonometrico e geometrico.

Che succederebbe se volessimo integrare delle funzioni di calcolo integrale o di
altro tipo? Ci sarebbe sia un aumento delle dimensioni delle _code base_, sia
un "mix" di fare funzioni che definiscono ambiti differenti (seppur simili tra
loro). Sarebbe ideale separare le diverse parti del programma, raggruppando
magari le funzioni geometriche nel file `geometria.py`, le funzioni
trigonometriche nel file `trigonometria.py` e via discorrendo.

Questi file che conterranno al loro interno prevalentemente funzioni (ma non
solo), sono chiamati moduli.

> <details open>
> <summary>✏️ <strong>Nota</strong></summary>
>
> La lina che distingue gli script dai moduli è molto sottile e è difficile fare
> confusione e utilizzarli in maniera intercambiabile. Va sottolineato però che,
> idealmente, gli script contengono al loro interno soltanto del codice che
> verrà eseguito, mentre i moduli contengono solo codice che verrà invocato da
> degli script.
>
> </details>
>
> <details>
> <summary>ℹ️ <em>Interprete e nome di un modulo</em></summary>
>
> L'interprete è in grado di risalire al nome di un modulo dal nome del file in
> cui è contenuto. Se, ad esempio, definiamo un modulo nel file `geometria.py`,
> l'interprete assocerà a quel modulo il nome geometria. Tale nome è inoltre
> accessibile globalmente e anche dall'interno del modulo richiamando
> variabile globale `__name__`.
>
> </details>

#### I moduli `geometria` e `trigonometria` ([⮨](#top))

Creiamo il file `geometria.py`, all'interno del quale spostiamo le funzioni
definite in precedenza per il calcolo geometrico:

```python
# geometria.py
def calc_area_quadrato(lato):
    return lato ** 2


def calc_area_rettangolo(base, altezza):
    return base * altezza


def calc_area_triangolo(base, altezza):
    return (base * altezza) / 2
```

Analogamente, nel file `trigonometria.py` andremo a definire la funzione per
il calcolo della tangente:

```python
# trigonometria.py
import math

def calc_tangente(angolo):
    return math.sin(angolo) / math.cos(angolo)
```

Modifichiamo ora il file `main.py`:

```python
# main.py
import geometria
import trigonometria

def main():
    print(geometria.calc_area_quadrato(4))
    print(trigonometria.calc_tangente(math.pi))

if __name__ == "__main__":
    main()
```

Notiamo due cose:

1. stiamo richiamando le funzioni `calc_area_quadrato()` e `calc_tangente()`
   definite nei moduli `geometria` e `trigonometria`, rispettivamente. Questi
   moduli sono importanti all'interno del nostro script mediante la direttiva
   `import`;
2. La strana sintassi presente nelle ultime righe viene usata per dichiarare
   che quello è il `main`, ovvero il punto di "accesso" al codice del programma.
   Il `main` è normalmente presente in tutti i linguaggi di programmazione, alle
   volte in modo differente tuttavia, nel caso di script particolarmente
   semplici, il `main` può essere omesso.

Eseguiamo lo script:

```sh
$ python main.py
16
0
```

### Utilizzare gli `import` ([⮨](#top))

Abbiamo usato una sola funzione del modulo `geometria`, `calc_area_quadrato()` e
abbiamo trascurato le altre due funzioni presenti nel modulo. In queste
circostanze, possiamo usare una versione modificata della direttiva `import`,
che assume la seguente forma:

```python
from <modulo> import import <funzione/classe>
```

che, nel nostro caso specifico, diventa:

```python
from geometria import calc_area_quadrato
```

In questo modo, importiamo soltanto quello che ci serve. Questo risulta essere
particolarmente utile a migliorare l'efficienza del nostro codice. Il perché
sarà chiaro a breve.

### Alias ([⮨](#top))

La direttiva `import` ci permette di definire degli alias, utili nel caso in cui
si usino dei package con nomi complessi. Ad esempio:

```python
import trigonometria as trig

print(trig.calc_tangente(math.pi))
```

## La funzione `dir()` ([⮨](#top))

La funzione `dir()` restituisce una lista con tutti i nomi (sia di funzione, che
di classe) definiti da un modulo. Ad esempio:

<!-- markdownlint-disable MD013-->

```pycon
>>> dir(geometria)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_area_quadrato', 'calc_area_rettangolo', 'calc_area_triangolo']
```

<!-- markdownlint-enable MD013 -->

È interessante notare che, oltre alle funzioni, classi e variabili da noi
definite, nel modulo geometria siano automaticamente definite altre variabili,
che saranno importate con `import`:

```python
if __name__ == "__main__":
    print(geometria.__file__)
    print(geometria.calc_area_quadrato(4))
```

Notiamo che possiamo accedere alla variabile `__file__` del modulo `geometria`,
che indica il percorso del modulo all'interno dal file system. Ovviamente,
questa variabile non è quasi mai utile, ma comporta un ulteriore carico sul
codice, per questo è importante l'uso della direttiva `from`.

### Moduli della libreria standard ([⮨](#top))

Python ha diversi moduli che appartengono ad una libreria standard, questi sono
automaticamente disponibili dal momento dell'installazione dell'interprete.
Alcuni tra i più utilizzati sono:

- `sys`: è integrato nell'interprete e offre diverse _utility_ necessarie al suo
  funzionamento;
- `os`: delegato all'interazione con il sistema operativo;
- `time`: usato per _utility_ riguardanti il "cronometraggio" del tempo di
  esecuzione di una funzione;
- `datetime`: usato per le funzionalità di data e ora;
- `copy`: usato per gestire la _deep copy_ di un oggetto, e altro.

Per una lista esaustiva, si rimanda alla
[Python Library Reference](https://docs.python.org/3/library/).

## Packages

Facciamo un brevissimo accenno ai packages, ovvero delle vere e proprie
"collezioni" che raggruppano moduli tra loro coerenti, in modo da facilitarne
l'accesso. Sostanzialmente i packages non sono altro che delle cartelle
contenenti più moduli (ovvero file con estensione `.py`), oltre ad un file
chiamato `__init__.py` che permette all'interprete di riconoscere quella cartella
come package e, occasionalmente, contiene delle istruzioni di inizializzazione
del package.

Per accedere ad un modulo contenuto all'interno di un package, usiamo la
direttiva `import`, modificandola come segue:

```python
import <nome_package>.<nome_modulo>
# oppure
from <nome_package>.<nome_modulo >import <nome_funzione>
```

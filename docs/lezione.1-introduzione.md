# 00 – Programma e obiettivi del Corso

> Corso di python per il calcolo scientifico

(Angelo Cardellicchio – angelo.cardellicchio@uniba.it)

In questo primo set di slide vediamo il corso. Le slide le carica.

---

## info

- Email angelo.cardellicchio@uniba.it
- Lezioni ibride
- Obbligatorio il 70% delle lezioni
- materiale didattico: <https://python.angelocardellicchio.it>

---

## Programma del corso

> Parte 1 (fondamentali)

1. Introduzione al corso
   - Introduzione a Python;
2. Concetti sintattici fondamentali
   - Strutture dati;
3. Classi, moduli e package in Python;
4. Introduzione a NumPy;
   - Array in NumPy.
5. Aritmetica ed algebra in NumPy;
6. Operazioni polinomiali e statistica in NumPy;
7. Jupyterlab
   - Visualizzazione dei risultati in Matplotlib e Seaborn;
8. Introduzione a SciPy;
   - Pandas e dataframe
9. ...

---

## Modalità di valutazione

- Orale (ble)

- tema d'anno: sviluppo tema, ppt da 12 slide, relaz max 4pagg

---

# Introduzione a Python

La IDE che utilizzeremo è VScode (ST3 va bene), vscode ha supporto integrato per i jupyter notebook

---

## Interprete python

Quando installiamo python bisogna verificare che

---

## Pyhon e tipizzazione

{[ mentre il C dichiara staticamenet le variabilit, python no. Questo porta al duck typing. l'interprete python conferisce il valore della variabile a seconda del suo comportamento. non ffarà un cast (una conversione di tipo). i tipi sono il formato del dato della variabile che usiamo. se diciamo che è un intero, occupa 32bit, se è long occupa 64bit. C è leggermente a più basso livello e quindi richiede la tipizzazione statica, python non lo richiede e lo stabilisce automaticamente. Il problema lo si ha se usiamo u intero come un float; l'intero si comporta da intero e quindi si ha un errore in C, in python non la fa questa cosa e sopperisce alle nostre mancanze. nei programmi più complessi se noi sbagliamo la classe, lo script complierà con degli errori. python effettua controlli non forti a runtime. non abbiamo errori finché non si arriva alla riga. troveremo un errore solo quando eseguiremo il codice. ]}

- Python ha tipizzazione dinamica

---

dichiarare una stringa può essere fatto con `"stringa"` ma anche con `'stringa'`

```python
>>> s = "stringa"
'stringa'
>>> s = 'stringa'
'stringa'
```

<!-- {[ la stringa ha una caratteristica: quella di essere immutabile ]} -->

in python una lista la dichiariamo così `l = [1, 2, 3]`

in C `l = ['1', 2, 3]` errore, in python no. fornisce la possibilità di avere liste eterogenee.

```py
l = [[1, 2, 3], 1, 2]
```

ho inserito una lista in una lista, c non lo accetta, il python sì. possiamo accedere ad un elemento di una lista. usiamo l'indice. in MATHLAB si parte da 1, in C e python si parte da 0.

```py
>>> l[0]
[1, 2, 3]
```

```py
>>> l[1] = 'pippo'
>>> l
[[1, 2, 3], 'pippo', 2]
```

alla fine è come se fosse un array multidimensionale. in C si usa `l[0][0]`

```py
>>> l[0][0]
1
>>> l[0][2]
3
>>> l[0][3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

abbiamo usato un indice al di fuori della lista perché l'ultimo indice della lista è `2`, non c'è un 4o elemento.

Tutto ciò per dire che possiamo cambiare il valore di una lista. proviamo a farlo per una stringa

```py
>>> s = 'stringa'
>>> s[0]
's'
>>> s[0] = 'p'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

possiamo però fare

```py
>>> s = 'pippo'
```

ma non `s[0] = 'p'`, perché la stringa è immutabile e quindi non si può modificare un singolo elemento della stringa. non c'è alcun modo di accedere alla stringa precedente, non viene immediatamente cancellata dalla memoria, quindi non vi si può più accedere.

((
per vedere il tipo di variabile usiamo `type(<obj>)`

```python
>>> type(l)
<class 'list'>
```

))

una cosa interessante è che è presente un'operazione chiamata slicing. presente anche in MATHLAB. volendo si può accedere a degli elementi ben definiti di una stringa:

```py
>>> ll = [1, 2, 3, 4, 5]
>>> ll[2:]
[3, 4, 5]
>>> ll[:]
[1, 2, 3, 4, 5]
>>> ll[-1]
5
>>> ll[4]
5
>>> ll[-2]
4
>>> len(ll)
5
>>> l2 = ['a', 'b', 'c']
>>> len(l2)
3
```

`len()` è una funzione. mettiamo che devo calcolare il perimetro di un quadrato: `lato = 4` il perimetro è `lato_doppio = lato + lato` `perimetro = lato_doppio + lato_doppio`, `perimetro_2 = lato_doppio + lato_doppio` anziché fare sempre così, creo una funzione.

```py
>>> def calcola_perimetro_doppio(lato):
...    perimetro = lato * 4
...    return perimetro
...

```

il C usa la parentesi graffa per iniziare una funzione. python usa i due punti e l'indentazione. python richiede che il codice nello stesso ambito sia allo stesso livello di intentazione.

non sto definendo il tipo di `#!py return`. come lato mi aspetto un intero o al più un decimale, che sia positivo. non sto inserendo controlli di alcun tipo. sta alla mia coscienza scrivere bene.

```py
>>> calcola_perimetro_quadrato('4')
'4444'
>>> s * 2
'pippopippo'
>>> s + ' paperino'
'pippo paperino'
```

python non ha detto che è un errore, ha eseguito normalmente. sta a noi inserire un controllo.

usiamo le parentesi tonde per contraddistinguere i paramentri delle funzioni

```py
>>> len(l2)
3
```

---

La funzione `append()` permette di concatenare le stringhe


~~~py
>>> l = [1, 2, 3]
>>> l.append(5)
>>> l
[1, 2, 3, 5]
~~~

`#!py len()` accetta sia stringa che lista. len è una funzione definita in maniera esterna ad una classe, come se fosse statica circa. .append() è definita sull'oggetto lista, sull'istanza. per questo si usa l'operatore `#!py .`. ricordiamo la funzione `#!py type()`. è una funzione usata per le liste, in questo caso la stiamo chiamando specificatamente per la lista `#!py l2`


---
***
---

# 02 – Concetti sintattici fondamentali




{[ ((
## la programmazione strutturata (non la chiede all'esame).

~~~
10 int 1 = 0
20 i = i + 1
30 i = i + 2
40 if i <= 10 then goto 70
50 print "Programma terminato"
60 end
70 print i & " al quadrato = " & i * i
80 goto 70
~~~

NON si usa il goto. è fortemente criticato

teorema di Bohm-Jacopini afferma che
Ogni algoritmo può essere costruito a partire da tre strutture di controllo fonamentali: sequenza, controllo e iterazione.

La sequenza è una lista di cose


~~~
distanza_x =
distanza_y =
????
~~~


selezione



~~~
a = 1
b = 2
if (a > b):
    then scrivi 'a è minore di b'
else:
    scrivi 'a è minore di b'
~~~
)) ]}


python non usa le graffe per le strutture di controllo, le usa per i dizionari.

l'ambito è delimitato dall'indentazione


~~~py
>>> a = 5
>>> b = 6
>>> if a > b:
...     a = a * 2
...     print(a)
... elif a == b:
...     print("sonon uguali")
... else:
...     print("non saprei")
...
non saprei
>>> a = 8
>>> if a > b:
...     a = a * 2
... print(a)
  File "<stdin>", line 3
    print(a)
    ^
SyntaxError: invalid syntax
~~~


mantenere stesso livello di indentazione

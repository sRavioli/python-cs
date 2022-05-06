    # 02 – Concetti sintattici fondamentali

{[ ((

## la programmazione strutturata (non la chiede all'esame).

```
10 int 1 = 0
20 i = i + 1
30 i = i + 2
40 if i <= 10 then goto 70
50 print "Programma terminato"
60 end
70 print i & " al quadrato = " & i * i
80 goto 70
```

NON si usa il goto. è fortemente criticato

teorema di Bohm-Jacopini afferma che
Ogni algoritmo può essere costruito a partire da tre strutture di controllo fondamentali: sequenza, controllo e iterazione.

La sequenza è una lista di cose

```
distanza_x =
distanza_y =
????
```

selezione

```
a = 1
b = 2
if (a > b):
    then scrivi 'a è minore di b'
else:
    scrivi 'a è minore di b'
```

)) ]}

python non usa le graffe per le strutture di controllo, le usa per i dizionari.

l'ambito è delimitato dall'indentazione

```py
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
```

mantenere stesso livello di indentazione

## REgole sintattiche fondamentali

parentesi:

- tonde - per funzione, esprimere precedenza nelle operazioni. altrimenti opzionali
- quadre - creazione e accesso elementi strutture dati
- graffe - insiemi e dizionario

if

```python
if (condizione):
    istruzioni()
elif (condizione2):
    istruzioni()
else:
    istruzioni()
```

switch case, esiste nella forma match case

```python
match comando:
    case "caso 1":
        istruzioni()
    case "caso 2":
        altre_istruzioni()
```

for loop - utilizza una sequenza iterabile

```python
for elemento in sequenza:
    istruzioni()
```

while

```python
while (condizione):
    istruzioni()
```

```pycon
>>> a = 5
>>> b = 6
>>> if a > 5:
... print("a è maggiore di 5")  # proviamo senza tab
  File "<stdin>", line 2
    print("a è maggiore di 5")
    ^
>>> if a > b:
...     print("a è maggiore di b")
... else:
...     print("b è maggiore o uguale a a")
...
b è maggiore o uguale a a
```

```pycon
>>> l = [1, "stringa", [1, 2, 3]]
>>> for elemento in l:
...     print(elemento)
...
1
stringa
[1, 2, 3]
>>> len(l)
3
```

for loop

```pycon
>>> s = 'python'
>>> for char in s:
...     print(char)
...
p
y
t
h
o
n
```

while loop

```pycon
>>> while (i < 10):
...     print(i)
...     i += 1
...
5
6
7
8
9
```

la funzione `range()` permette di definire un range di valori

la sintassi è tipo `range(<inizio>, <fine>, <step>)`

**NON** è una lista

break, continue, break

```python
while True:
    if ... :
        ...
        continue
    else:
        ...
        break
```

---

vediamo degli esempi

```pycon
>>> r = range(0, 10)
>>> r
range(0, 10)
>>> type(r)
<class 'range'>
>>> list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

a step 2

```pycon
>>> r1 = range(0, 20, 2)
>>> list(r1)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

possiamo combinare le funzioni

```pycon
>>> r3 = list(range(0, 10))
>>> r3
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

esempio break continue

```pycon
>>> for el in r3:
...     if (el % 2 == 0):
...             continue
...     else:
...             print(el)
...
1
3
5
7
9
```

---

definire una funzione
si usa la kword `def`, sintassi:

```python
def nome(params):
    istruzione()
    return valore_ritorno
```

non viene definito un valore di ritorno, tanto meno per i parametri.
se non si mette return python non restituisce niente

---

esercizio - func che iteri finché il valore associato ad un contatore intero è
minore di 10 col while.

le var passate ad una funz sono una copia delle var globali

---

---

# Strutture dati in python

python ha il metodo `.append()` che inserisce un elemento in cima alla lista.
il metodo `.pop(<posizione>)` che estrae un elemento in posizione`<posizione>`.
di default è `len(<lista>) - 1`

per inserire c'è anche il metodo `.insert(<posizione>, <elemento>)` per inserire
l'elemento `<elemento>` in posizione `<posizione>`.

list comprehension:

```python
lista_output = [funzione(elemento) for elemento in lista_input]
```

esempio:

```pycon
>>> l = [1, 2, 3, 4]
>>> l_out = [el * 2 for el in l]
>>> l_out
[2, 4, 6, 8]
```

anche con la funzione:

```pycon
>>> def prodotto(elemento):
...     return elemento * 2
...
>>> l_out2 = [prodotto(el) for el in l]
>>> l_out2
[2, 4, 6, 8]
```

anche col ciclo for, la list comprehension è più compatta

```pycon
>>> l_out3 = []
>>> for el in l:
...     l_out3.append(el * 2)
...
>>> l_out3
[2, 4, 6, 8]
```

**NON** abusare della list comprehension, una volta imparata la sintassi, la si
usa spesso. tuttavia la lista comprehension serve a generare una lista da liste
esistenti. se non bisogna generare una lista, non usiamo la list comprehension.
non va forzata.

PER CASA: eleva a potenza lista || determina se pari o dispari, stampa liste.

creiamo un dizionario

```pycon
>>> dizionario = dict()
>>> dizionario
{}
```

aggiungiamo una chiave-valore:

```pycon
>>> dizionario['pippo'] = 'pluto'
>>> dizionario
{'pippo': 'pluto'}
```

ad esempio nelle pagine gialle

```pycon
>>> elenco = dict()
>>> elenco['cardellicchio'] = '123456789'
>>> elenco['cicciocappuccio] = '987654321'
>>> elenco
{'cardellicchio': '123456789', 'cicciocappuccio': '987654321'}
>>> elenco['cardellicchio']
'123456789'
>>> elenco.values()
dict_values(['123456789', '987654321'])
>>> elenco.keys()
dict_keys(['cardellicchio', 'cicciocappuccio'])
>>> list(elenco.keys())
['cardellicchio', 'cicciocappuccio']
>>> list(elenco.items())
[('cardellicchio', '123456789'), ('cicciocappuccio', '987654321')]
```

esiste anche la dictionary comprehension

```python
output = {chiave: valore for val in lista}
```

# 02 – Programmare in Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<!-- TOC -->

1. [02 – Programmare in Python](#02--programmare-in-python)
2. [Alcuni concetti sintattici fondamentali](#alcuni-concetti-sintattici-fondamentali)
   1. [Uso delle parentesi](#uso-delle-parentesi)
   2. [Istruzioni e ambito](#istruzioni-e-ambito)
3. [Programmazione strutturata](#programmazione-strutturata)
   1. [Istruzioni condizionali (`if`)](#istruzioni-condizionali-if)
   2. [Pattern matching](#pattern-matching)
   3. [Cicli](#cicli)
      1. [Ciclo `for`](#ciclo-for)
      2. [Ciclo `while`](#ciclo-while)
4. [La funzione `range()`](#la-funzione-range)
5. [Istruzioni `break` e `continue`](#istruzioni-break-e-continue)
6. [Definire una funzione](#definire-una-funzione)
   1. [Passaggio di parametri ad una funzione](#passaggio-di-parametri-ad-una-funzione)
   2. [L'istruzione `pass`](#listruzione-pass)

<!-- /TOC -->
</details>

# Alcuni concetti sintattici fondamentali

Oltre al _duck typing_, esistono altri concetti che caratterizzano la sintassi
di Python.

## Uso delle parentesi

Le **parentesi tonde** si usano per:

1. racchiudere gli argomenti di una funzione

   ```python
   funzione(argomento)
   funzione(argomento, altro_argomento)
   ```

2. la creazione di tuple

   ```python
   tupla = (0, 1)
   lista_tuple = [(0, 1), (1, 2)]
   ```

3. esprimere la precedenza nelle operazioni

   ```python
   a, b, c = 2, 3, 4

   r1 = a + b * c   # risultato: 14
   r2 = (a + b) * c   # risultato: 20
   if a > 2:   # equivalente a `if (a > 2):`
       pass
   ```

Negli altri casi sono opzionali e si possono omettere.

Le **parentesi quadre** si usano per:

1. la creazione di liste

   ```python
   lst = [0, 1, 2, 3, 4, 5]
   lst1 = [0, "lista", 2, "di elementi", [3, "4"], (5, 6)]
   ```

2. accedere agli elementi di una struttura dati

   ```python
   lst = [0, 1, 2, 3, 4, 5]
   print(lst[0])   # stamperemo: 0

   tupla = (6, 7)
   print(tupla[0]) # stamperemo: 6
   ```

Le **parentesi graffe** si usano per:

1. la creazione di un dizionario

   ```python
   dizionario = {"a": 1, "b": 2, "c": 3}
   print(dizionario[a])   # otterremo: 1, il valore associato alla chiave "a"
   ```

2. la creazione di un insieme

   ```python
   # l'insieme è simile ad una lista, però gli elementi non si possono ripetere
   insieme = {1, 2, 3, 4, 1}
   print(insieme[1])   # errore! non si può accedere tramite indice
   ```

## Istruzioni e ambito

In C, ad esempio, per terminare un'istruzione si usa il punto e virgola `;`.
In Python questo non è necessario poiché l'interprete prevede che un'istruzione
termini quando si va a capo. Questo significa che

```python
a = 1
```

è un'istruzione. Insomma, in Python è possibile omettere il punto e virgola.
Questo però non vuol dire che non lo si possa usare, infatti:

```python
a = 1; b = 2; c = 3;
```

sono istruzioni valide in Python. In ogni caso è sconsigliato l'utilizzo del
punto e virgola.

In Python il codice e quindi anche le variabili, possono essere salvati in due
ambienti diversi, l'_Ambito Locale_ e l'_Ambito Globale_, chiamati in inglese
_Global Scope_ e _Local Scope_.

Possiamo pensare che questi due ambienti siano dei contenitori distinti in cui
vengono definite e assegnate le variabili, un contenitore **Globale** e un
contenitore **Locale**. Quando uno di questi contenitori viene distrutto, quindi
quando uno di questi ambiti viene distrutto, lo stesso accade per i valori delle
variabili in esso salvate, che vengono quindi dimenticati.

Un ambito _Locale_ viene creato ogni volta che una funzione viene chiamata e
viene distrutto dopo che la funzione restituisce un valore con `return`.
Potremmo semplificare il concetto pensando che ogni volta che la funzione viene
processata, Python le fornisse un contenitore nel quale riporre tutte le sue
variabili e tutto il codice. Le variabili dichiarate all'interno di qualsiasi
funzione, quindi nell'ambito _Locale_ della funzione, sono chiamate
_Variabili Locali_.

Possono dunque esistere tanti _Local scopes_ (ambiti locali), tante quante
sono le funzioni in esecuzione.

Al contrario, esiste un unico _ambito Globale_, che viene creato automaticamente
da Python all'avvio del programma e distrutto alla chiusura del programma.
Questo è l'ambito principale: tutte le variabili che vengono dichiarate
all'esterno di una funzione sono chiamate proprio _Variabili Globali_, e restano
pertanto in vita dall'avvio alla chiusura del programma principale.

Mentre possiamo accedere alle _Variabili Globali_ in qualsiasi punto del
programma, possiamo accedere alle _Variabili Locali_ solamente nell'_Ambito_
_Locale_ della funzione in cui sono contenute

Per quanto riguarda la definizione di un ambito (ad esempio locale all'interno
di una funzione), Python utilizza i _due punti_ e il numero di _indentazioni_.

> <details open>
> <summary>💡 <em>Suggerimento</em></summary>
>
> In generale possiamo dire che le istruzioni allo stesso livello di
> indentazione sono considerate dall'interprete Python come istruzioni
> appartenenti al medesimo ambito.
>
> <details>
> <summary><em>Infatti...</em></summary>
>
> ...se non rispettassimo la corretta indentazione, l'interprete ci restituirà un
> errore
>
> ```pycon
> >>> a, b = 8, 6
> >>> if a > b:
> ...     a *= 2
> ... print(a)
>   File "<stdin>", line 3
>     print(a)
>     ^
> SyntaxError: invalid syntax
> ```
>
> </details>
>
> </details>

Dunque, per dichiarare una funzione, scriveremo:

```python
# l'inizio dell'ambito Locale è contrassegnato dai due punti `:`
def funzione(): # <- inizio del Local Scope
   # tutto ciò che appartiene alla funzione, deve mantenere lo stesso livello
   # di indentazione
   a = 1
   return a


# <- fine del Local Scope
# secondo le convenzioni, dopo una funzione seguono due linee vuote
print(a)   # l'interprete restituirà un errore
```

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> Per ottenere l'indentazione occorre usare il tasto <kbd>Tab</kbd> della
> tastiera, oppure quattro <kbd>Space</kbd>. È **_fondamentale_** non mischiare
> le due tecniche.
>
> </details>

# Programmazione strutturata

Python utilizza una sintassi per le strutture di controllo differente rispetto
a quelle usate nei tipici linguaggi C-like.

## Istruzioni condizionali (`if`)

In Python, l'istruzione condizionale `if`, ha una sintassi di questo tipo:

```python
if <condizione>:
   istruzioni()
elif <condizione>:
   istruzioni()
else:
   istruzioni()
```

Python utilizza la _keyword_ `elif` come sincrasi di `else if` che altri
linguaggi utilizzano. Se, ad esempio, volessimo verificare il valore di una
variabile intera, potremmo scrivere:

```python
a = 5
if a < 5: # <- condizione
   print("a è minore di 5") # <- istruzioni
elif a == 5:
   print("a è uguale a 5")
else:
   print("a è maggiore di 5")
```

L'output sarà il seguente:

```txt
a è uguale a 5
```

## Pattern matching

Fino alla versione 3.10, Python non offriva il costrutto `switch/case`. A
partire da quest'ultima versione il _pattern matching_ è stato implementato con
la seguente sintassi:

```python
match <comando>:
   case "caso 1":
      istruzioni()
   case "caso 2":
      istruzioni()
   case "altro caso":
      print("Comando sconosciuto")
```

## Cicli

### Ciclo `for`

Il ciclo `for` itera su una _sequenza_, come una stringa o una lista, e ha una
sintassi del tipo:

```python
for elemento in sequenza:
   istruzioni()
```

Ad esempio, stampiamo i numeri che vanno da `0` a `4`:

```python
numbers = [0, 1, 2, 3, 4]
for num in numbers:
   print(num)
```

otterremo:

```python
0
1
2
3
4
```

Rispetto ai linguaggi "classici", il ciclo `for` opera esclusivamente su
_iterabili_. Questa caratteristica di Python comporta anche una maggiore
semplicità del codice, ad esempio, iteriamo su una stringa:

```python
strg = "Python"
for char in strg:
   print(char)
```

otterremo:

```python
P
y
t
h
o
n
```

> <details>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Come ci ricorda il _no free lunches theorem_, non esistono pasti gratuiti!
> Infatti, la maggiore semplicità sintattica offerta da Python non è indolore.
> Uno script Python, per quanto ottimizzato, non potrà quasi mai offrire
> performance paragonabili ad un codice ottimizzato in C o C++, a meno di non usare
> particolari (ed avanzati) accorgimenti.
>
> </details>

### Ciclo `while`

A differenza del ciclo `for`, il funzionamento del `while` è analogo a quello
delle controparti degli altri linguaggi di programmazione. La sintassi è la
seguente:

```python
while condizione:
   istruzioni()
```

Ad esempio:

```python
import random as rnd

condition = True
while condition:
   if rnd.randint(-5, 5) > 0:
      print("continuo")
   else:
      print("mi fermo")
      condition = False
```

Il codice precedente non fa altro che generare un valore numerico intero in
maniera casuale nell'intervallo `[-5, 5]` mediante il metodo `randint()`, della
libreria `random`. Se tale valore è superiore a `0`, il ciclo continua,
altrimenti viene interrotto.

Otterremo, ad esempio:

```python
continuo
continuo
continuo
continuo
continuo
continuo
mi fermo
```

oppure:

```python
mi fermo
```

> <details open>
> <summary>ℹ️ <em>I valori booleani in Python</em></summary>
>
> Notiamo che i valori booleani sono stati scritti come `True` e `False`. Questo
> non è un errore, la prima lettera è maiuscola, a differenza di altri linguaggi.
>
> </details>

# La funzione `range()`

Riprendiamo il ciclo `for` visto in precedenza:

```python
numbers = [0, 1, 2, 3, 4]
for num in numbers:
   print(num)
```

Nonostante il codice sia già compatto, scrivere manualmente la lista da iterare
può diventare un'operazione abbastanza complessa. Python dispone della funzione
`range()`, la cui sintassi è la seguente:

```python
range(<inizio>, <fine>, <step>)
```

Questa funzione genera automaticamente una sequenza di numeri compresi tra
`<inizio>` (incluso) e `<fine>` (escluso) con incremento `<step>`.
L'unico valore che va inserito obbligatoriamente è `<fine>`, `<inizio>` è di
default `0`, `<step>` è di default `1`. Generiamo, ad esempio, i numeri compresi
tra `0` e `4`:

```pycon
>>> rng = range(0, 5, 1)
>>> print(list(rng))
[0, 1, 2, 3, 4]
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Per ottenere in output i valori di `rng` è necessario convertirli in lista con
> `list(rng)`.
>
> </details>

Dunque nell'esempio precedente potremmo omettere tutti i valori tranne `5`:

```pycon
>>> rng = range(5)
>>> print(list(rng))
[0, 1, 2, 3, 4]
```

**Esercizio:** Iteriamo su tutti i valori della lista
`["Pippo", "Pluto", 5, "Paperino"]`.

**Soluzione:** Usiamo la funzione `range()` e la funzione `len()`:

```python
lst = ["Pippo", "Pluto", 5, "Paperino"]
for item in range(len(lst)):
   print(lst[item])

# Output:
# Pippo
# Pluto
# 5
# Paperino
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Avremmo potuto scrivere:
>
> ```python
> lst = ["Pippo", "Pluto", 5, "Paperino"]
> for item in lst:
>    print(item)
> ```
>
> e avremmo ricevuto lo stesso output, però bisogna esercitarsi con `range()`.
>
> </details>

Poiché `len(lst)` ci restituisce il numero di elementi presenti nella lista
(ovvero 4), definiamo un `range` che va da `0` a `3`. Dopodiché stampiamo
elemento per elemento i valori contenuti all'interno della lista e otterremo il
risultato desiderato.

# Istruzioni `break` e `continue`

Le istruzioni `break` e `continue` permettono rispettivamente di
_uscire dal ciclo_ o di _saltare all'iterazione successiva_. Ad esempio:

```python
import random as rnd

while True:
   if rnd.randint(-5, 5) > 0:
      print("continuo")
      continue
   else:
      print("esco")
      break

print("ciclo terminato")
```

Le istruzioni precedenti usciranno dal ciclo quando viene generato casualmente
un numero negativo, al contrario continueranno l'iterazione quando verrà
generato casualmente un numero positivo.

# Definire una funzione

Possiamo definire una funzione nel seguente modo:

```python
def nome_funzione(parametro, altro_parametro, ...):
   # istruzioni...
   return valore_di_ritorno
```

È importante notare che:

1. non è necessario definire un tipo ma soltanto un _valore_ di ritorno. Qualora
   la funzione non restituisca alcun valore, possiamo omettere `return`;
2. non è (strettamente) necessario definire il tipo di ciascuno dei parametri
   passati
3. possiamo inserire dei parametri _opzionali_, con valori di default.

**Esercizio:** creiamo una funzione che, ad una lista, concateni i valori
presenti nella stessa ma raddoppiati.

**Soluzione:** usiamo il metodo `.append()` per aggiungere alla lista i nuovi
elementi della stessa.

```python
def raddoppia_lista(lst):
   for item in range(len(lst)):
      lst.append(lst[item] * 2)

   return print(lst)

lista = [1, 2]
raddoppia_lista(lista)

# Output: [1, 2, 3, 4]
```

**Esercizio:** creiamo una funzione che restituisca una lista di numeri
generati casualmente tra `0` e `10` (escluso). Usiamo un parametro opzionale per
specificarne la lunghezza.

**Soluzione:** usiamo i metodi `append()` e `randint()` della libreria `random`.

```python
import random as rnd

def genera_lista_casuale(lunghezza=5):
   lst = []
   for i in range(lunghezza):
      lst.append(rnd.randint(0, 10))
   return print(lst)


genera_lista_casuale()     # Possibile output: [3, 9, 7, 2, 3]
genera_lista_casuale(10)   # Possibile output: [2, 4, 8, 1, 5, 3, 1, 3, 0, 9]
```

> <details open>
> <summary>⚠️ <strong>Attenzione!</strong></summary>
>
> Il duck typing fa sì che non venga effettuato alcun controllo sui parametri in
> ingresso. Questo però non significa che non sia possibile chiamare la funzione
> `genera_lista_casuale()` passandogli come parametro una stringa; questo
> causerà, ovviamente, un errore.
>
> </details>

## Passaggio di parametri ad una funzione

Python prevede che i parametri di una funzione le siano passati secondo una
modalità ibrida chiamata _call-by-assignment_. In sostanza, il passaggio avviene
esclusivamente per valore, ma con effetti differenti sui tipi mutabili e
immutabili.

Ad esempio, provando a passare un valore primitivo (come un intero), Python si
comporterà come se si stesse effettuando un passaggio per valore:

```python
def raddoppia(intero):
   intero *= 2
   print(f"Valore all'interno della funzione: {intero}")
```

Il risultato sarà:

```pycon
>>> intero = 2
>>> raddoppia(intero)
Valore all'interno della funzione: 4
>>> print(f"Valore all'esterno della funzione: {intero}")
Valore all'esterno della funzione: 2
```

Ciò è legato al fatto che il passaggio viene effettuato per valore, per cui
la funzione `raddoppia()` agirà su una _copia_ della variabile passata come
argomento e non sulla variabile originale. Se invece usassimo una funzione che
modifica una lista:

```python
def aggiungi_a_lista(lst, elemento):
   lst.append(elemento)
   print(f"Valore all'interno della funzione: {lst}")
```

Il risultato sarà:

```pycon
>>> lista = [1, 2]
>>> aggiungi_a_lista(lista, 3)
Valore all'interno della funzione: [1, 2, 3]
>>> print(f'Valore all\'esterno della funzione: {lista}')
Valore all'esterno della funzione: [1, 2, 3]
```

In questo caso, essendo la lista mutabile, il passaggio viene effettuato per
_reference_: questo significa che le operazioni compiute all'interno della
funzione `aggiungi_a_lista()` agiranno sulla lista originaria.

> <details open>
> <summary>ℹ️ <em>Shallow e deep copy</em></summary>
>
> Di default, Python copia le variabili per mezzo di una _shallow copy_: ciò
> significa che un'operazione di _assignment_ del tipo `a = b` fa in modo che
> `a` punti allo stesso indirizzo di memoria di `b` e, di conseguenza, ogni
> modifica a `b` si rifletta su `a`. Per evitare un fenomeno di questo tipo
> occorre usare una _deep copy_ grazie alla funzione `deepcopy()` della libreria
> `copy`.
>
> </details>

## L'istruzione `pass`

Chiudiamo accennando all'istruzione pass. Questa non fa assolutamente nulla; è
utile, ad esempio, quando vogliamo inserire una funzione (o una classe) vuota,
che definiremo per qualche motivo in seguito:

```pycon
>>> def funzione_vuota():
>>> ... pass
>>> ...
>>> funzione_vuota()
```

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> Anche se inizialmente potrebbe non essere evidente, esistono diverse
> situazioni in cui l'istruzione `pass` risulta essere estremamente utile.
>
> </details>

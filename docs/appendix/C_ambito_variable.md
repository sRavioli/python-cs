# Appendice D – Ambito di una Variabile

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [Appendice D – Ambito di una Variabile](#appendice-d--ambito-di-una-variabile)
   1. [C.1 – Istruzioni e ambito](#c1--istruzioni-e-ambito)
   2. [C.2 – Prima modifica](#c2--prima-modifica)
   3. [C.3 – Seconda modifica](#c3--seconda-modifica)

<!-- /TOC -->

</details>

All'interno di un programma ogni variabile ha una sorta di _ciclo di vita_, che
ne prevede la creazione, utilizzo e distruzione.

## C.1 – Istruzioni e ambito

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

Facciamo un esempio. Definiamo una funzione `calcolo_voto_accesso_laurea()` che
accetta in ingresso un argomento, ovvero la lista con i voti degli esami:

```python
>>> def calcolo_voto_accesso_laurea(voti_esami):
...    somma_voti = 0
...    for voto in voti_esami:
...       somma_voti += voto
...    voto_medio = somma_voti / len(voti_esami)
...    voto_accesso = voto_medio / 3 * 11
...    return voto_accesso
```

Proviamo a chiamarla.

```py
>>> lista_voti = [18, 20, 19, 30, 24, 30]
>>> print('Il voto di accesso è: ', calcolo_voto_accesso_laurea(lista_voti))
Il voto di accesso è:  86.16666666666666
```

## C.2 – Prima modifica

Facciamo una prima modifica:

```py
>>> lista_voti = [18, 20, 19, 30, 24, 30]
>>> def calcolo_voto_accesso_laurea(voti_esami):
...    print(f'La lista dei voti è: {lista_voti}')
...    somma_voti = 0
...    for voto in voti_esami:
...       somma_voti += voto
...    voto_medio = somma_voti/len(voti_esami)
...    voto_accesso = voto_medio / 3 * 11
...    return voto_accesso
...
>>> print('Il voto di accesso è: ', calcolo_voto_accesso_laurea(lista_voti))
La lista dei voti è: [18, 20, 19, 30, 24, 30]
Il voto di accesso è:  86.16666666666666
```

Otterremo due valori in output.

## C.3 – Seconda modifica

Proviamo a modificare ancora il codice:

```py
>>> lista_voti = [18, 20, 19, 30, 24, 30]
>>> def calcolo_voto_accesso_laurea(voti_esami):
...     somma_voti = 0
...     for voto in voti_esami:
...         somma_voti += voto
...     voto_medio = somma_voti/len(voti_esami)
...     voto_accesso = voto_medio / 3 * 11
...     return voto_accesso
...
>>> print('Il voto medio è: ', voto_medio)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'voto_medio' is not defined
>>> print('Il voto di accesso è: ', calcolo_voto_accesso_laurea(lista_voti))
Il voto di accesso è:  86.16666666666666
```

Cosa è successo? Andiamo un attimo a ritroso e partiamo dalla prima modifica.

Abbiamo provato ad accedere alla variabile _globale_ `lista_voti`, definita nel
corpo "principale" dello script, dall'interno della funzione
`calcola_voto_accesso_laurea()`. Ciò è evidentemente possibile, in quanto
possiamo accedere ad una variabile globale da un ambito locale.

Il contrario, tuttavia, non è possibile: infatti, nella seconda modifica,
proviamo ad accedere ad una variabile locale alla funzione
`calcola_voto_accesso_laurea()` dall'esterno della funzione stessa. Questo non
può avvenire, perché le variabili locali "scompaiono" al termine della funzione
in cui sono definite, per cui l'interprete ci restituirà un errore.

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
   2. [Ambito e termine di un'istruzione](#ambito-e-termine-di-unistruzione)

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

## Ambito e termine di un'istruzione

In C, ad esempio, l'istruzione termina con il punto e virgola. In Python questo
non è necessario dato che prevede che termini un'istruzione quando si va a capo.
Questo significa che

```python
a = 1
```

è un'istruzione. Dunque possiamo omettere il punto e virgola.

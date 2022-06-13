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

---

<a name="top"></a>

# Appendice E – Consigli Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [Appendice E – Consigli Python](#appendice-e--consigli-python)
   1. [E.1 – Tabella degli operatori booleani (⮨)](#e1--tabella-degli-operatori-booleani-)
   2. [E.2 – Gestione delle Eccezioni (⮨)](#e2--gestione-delle-eccezioni-)
      1. [E.2.1 – I decorator (⮨)](#e21--i-decorator-)
         1. [E.2.1.1 – Funzioni come oggetti (⮨)](#e211--funzioni-come-oggetti-)
         2. [E.2.1.2 – Funzioni come argomenti di altre funzioni (⮨)](#e212--funzioni-come-argomenti-di-altre-funzioni-)
         3. [E.2.1.3 – Definizione ed uso di decorator (⮨)](#e213--definizione-ed-uso-di-decorator-)

<!-- /TOC -->

</details>

## E.1 – Tabella degli operatori booleani ([⮨](#top))

| Operatore | Operazione logica | Esempio             | Risultato |
| --------- | ----------------- | ------------------- | --------- |
| `and`     | AND               | `1 and 2`           | `True`    |
| `or`      | OR                | `True or False`     | `True`    |
| `not`     | NOT               | `True is not False` | `True`    |

## E.2 – Gestione delle Eccezioni ([⮨](#top))

### E.2.1 – I decorator ([⮨](#top))

Prima di continuare a parlare dei metodi che è possibile definire all'interno
di una classe Python, è necessario introdurre il concetto di _decorator_,
ovvero una particolare notazione che viene usata in Python (e in altri
linguaggi di programmazione) per indicare una funzione che "decora" un'altra
funzione.

#### E.2.1.1 – Funzioni come oggetti ([⮨](#top))

Python tratta le funzioni come degli _oggetti_. E' quindi possibile che una
funzione _restituisca_ una _funzione_:

```py
def main_character(series):
    def supernatural():
        return "Sam Winchester"

    def breaking_bad():
        return "Walter White"

    if series == "Supernatural":
        return supernatural
    elif series == "Breaking Bad":
        return breaking_bad
```

Il valore di ritorno è quindi un oggetto. Possiamo provare a chiamarlo dal
nostro script:

```py
>>> mc = main_character("Supernatural")
```

Se provassimo a mandarlo a schermo trattandolo come una variabile, avremmo in
uscita una reference a funzione:

```py
>>> mc
<function main_character.<locals>.supernatural at 0x00000170C448BA60>
```

Per visualizzare il risultato, trattiamolo come se fosse una chiamata a funzione:

```py
>>> mc()
'Sam Winchester'
```

#### E.2.1.2 – Funzioni come argomenti di altre funzioni ([⮨](#top))

Possiamo passare una funzione come argomento ad un'altra funzione:

```py
>>> def favorite_series(func):
...     def internal_check():
...         print("Checking my favorite series...")
...         func()
...         print("Got it!")
...     return internal_check
...
>>> def check():
...     print('Sons of Anarchy')
...
```

Dal nostro script:

```py
>>> print_fav_series = favorite_series(check)
>>> print_fav_series()
Checking my favorite series...
Sons of Anarchy
Got it!
```

Vediamo quindi come la funzione passata come argomento sarà correttamente
chiamata internamente al metodo `favorite_series()`.

#### E.2.1.3 – Definizione ed uso di decorator ([⮨](#top))

La sintassi che abbiamo usato è, per dirla con Manzoni, _ampollosa_. Python
offre una sintassi equivalente ma più accessibile per usare una funzione come
argomento di un'altra funzione: i decorator. Infatti:

```py
>>> @favorite_series
... def print_fav_series_decorated():
...     print('Breaking Bad')
...
>>> print_fav_series_decorated()
Checking my favorite series...
Breaking Bad
Got it!
```

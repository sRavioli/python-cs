# array

sono rappresentazione a n dimensioni di un Tensore. Ad
nel pc un tensore è un'immagine, formata dall'intersezione di tre liste(??)

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
```

possono ricordare delle liste, però c'è una differenza. gli array sono omogenei.
hanno anche la proprietà `shape()`. Ad

l'accesso avviene tramite indicizzazione, come per le liste. si possono anche
usare delle maschere booleane, si possono sommare gli array, moltiplicazione etc.

esiste il metodo `.dot()` per moltiplicazione tra matrici.

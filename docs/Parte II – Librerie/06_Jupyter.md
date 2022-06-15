# 6 – Jupyter

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [6 – Jupyter](#6--jupyter)
2. [iPython e Jupyter Lab](#ipython-e-jupyter-lab)
3. [Anatomia di un Notebook](#anatomia-di-un-notebook)
4. [Installazione e lancio di Jupyter](#installazione-e-lancio-di-jupyter)
5. [Il primo notebook](#il-primo-notebook)
6. [Altre operazioni utili](#altre-operazioni-utili)

<!-- /TOC -->

</details>

# iPython e Jupyter Lab

Fino ad ora ci siamo limitati a lanciare script Python direttamente da riga di
comando. Tuttavia è evidente come questo approccio sia limitato, specialmente in
applicazioni in ambito data science.

Per ovviare a queste problematiche, all'interno del framework `SciPy` viene
proposto [Jupyter Lab](https://jupyter.org), che introduce uno tra gli strumenti
più utilizzati dai data analyst al giorno d'oggi, ovvero i _notebook_.

# Anatomia di un Notebook

Un notebook è un ambiente interattivo che permette di scrivere e testare il
nostro codice. In particolare, potremo scrivere una o più istruzioni, e
eseguirle in maniera separata dalle altre, mediante il meccanismo delle celle.
Queste non sono altro che dei singoli "blocchi" di codice.

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> I notebook Jupyter ci permettono di inserire anche commenti, descrizioni ed
> equazioni utilizzando due linguaggi di markup molto noti, ovvero
> [Markdown](https://daringfireball.net/projects/markdown/) e [Latex](https://www.latex-project.org).
>
> </details>

Vediamo come creare e utilizzare il primo notebook.

# Installazione e lancio di Jupyter

> <details open>
> <summary>ℹ️ <em>Installazione di una libreria</em></summary>
>
> Ricordiamo che le diverse opzioni utilizzabili per installare una libreria
> sono descritte nel dettaglio nell'[appendice B].
>
> </details>

Per installare Jupyter Lab, ricorriamo all'utilizzo di `pip`, preferibilmente
all'interno di un ambiente virtuale (creato con `conda` o altri):

```sh
$ conda activate <my-env>
(<my-env>) ~$ pip install jupyterlab
```

A differenza delle altre librerie, Jupyter non andrà (necessariamente) importato;
infatti, è possibile lanciare un ambiente interattivo utilizzando la seguente
istruzione da riga di comando:

```sh
$ jupyter-lab
[I 2022-06-15 12:12:29.172 ServerApp] jupyterlab | extension was successfully linked.
# ...
```

> <details>
> <summary>ℹ️ <em>Importare iPython</em></summary>
>
> Teoricamente sarebbe possibile importare iPython e utilizzare i metodi e le
> classi messe a disposizione come una qualsiasi libreria. Però spesso ci si
> limita ad utilizzare l'ambiente interattivo offerto dai notebook.
>
> </details>

# Il primo notebook

Dopo aver lanciato Jupyter Lab, ci troveremo di fronte ad una schermata del
genere:

![Jupyter-lab homepage](./img/jupyter-lab.jpg)

Creiamo il nostro primo notebook cliccando sul pulsante "Python 3 (ipykernel)"
nella sezione Notebook. Una volta terminata la procedura possiamo interagire con
l'ambiente. Prima di procedere diamo un nome al notebook dal menù a sinistra.

Facciamo qualcosa di semplice: creiamo una funzione che sommi due variabili
numeriche, restituendo il risultato e chiamiamola su due valor.

Per prima cosa scriviamo il codice del della funzione all'interno della cella:

```python
def somma(a, b):
    return a + b
```

Per eseguire il codice all'interno della cella, basta fare click sul tasto Play,
oppure premere <kbd>Shift</kbd> + <kbd>Enter</kbd>. Dopo l'esecuzione della
prima cella, Jupyter ne creerà in automatico un'altra e al suo interno, potremo
scrivere le istruzioni necessarie a chiamare la funzione somma su due diversi
valori:

```python
somma(5, 7)
```

Eseguiamo l'istruzione. Subito sotto la cella apparirà il risultato.

# Altre operazioni utili

Jupyter ci permette di effettuare varie operazioni utili, tra cui:

- cancellare un'intera cella;
- inserire una cella al di sopra o al di sotto di quella attualmente selezionata;
- stoppare il _kernel_;
- riavviare il _kernel_.

Soffermiamoci brevemente sulle ultime due operazioni.

Può capitare, che ci sia la necessità di interrompere l'esecuzione delle
istruzioni, oppure che sia necessario riavviare il notebook. Dato che Jupyter si
basa sul concetto di _kernel_, il quale è il responsabile dell'esecuzione del
notebook, diremo in gergo che possiamo interrompere, o _stoppare_, il kernel,
oppure che possiamo riavviarlo.

L'interruzione del kernel si limita a fermare l'esecuzione della cella attuale.
Ciò non comporta alcuna perdita di dati e potremo riprendere ad eseguire il
codice nel notebook in ogni momento, sia dall'inizio di quella cella, sia che da
un'altra.
Il riavvio del kernel, invece, interrompe completamente l'esecuzione, andando a
cancellare anche le variabili presenti in memoria: si tratta, di un vero e proprio
**reset**. Andrebbe utilizzato quando, ad esempio, abbiamo la necessità di
riorganizzare il codice, oppure quando abbiamo effettuato un numero eccessivo di
modifiche per il quale i risultati iniziano a non essere coerenti con le quelli
attesi.

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

# Appendice B – Installazione di una libreria Python

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [Appendice B – Installazione di una libreria Python](#appendice-b--installazione-di-una-libreria-python)
   1. [B.1 – Opzione A: il _package-manager_ `pip`](#b1--opzione-a-il-package-manager-pip)
   2. [B.2 – Opzione B: un ambiente virtuale](#b2--opzione-b-un-ambiente-virtuale)
   3. [B.3 – Opzione C: una distribuzione per il calcolo scientifico](#b3--opzione-c-una-distribuzione-per-il-calcolo-scientifico)
   4. [B.4 – Opzione D: un package manager come `pipenv`](#b4--opzione-d-un-package-manager-come-pipenv)

<!-- /TOC -->

</details>

Per installazione una libreria Python, ci sono varie opzioni. Vediamole nel
dettaglio e immaginiamo di voler installare NumPy.

## B.1 – Opzione A: il _package-manager_ `pip`

La prima opzione, probabilmente quella maggiormente utilizzata, è `pip`. Questo
è il _package-manager_ (gestore di pacchetti) di Python.

Apriamo un terminale con i permessi amministratore. Per Linux scriveremo
`sudo`, per Windows apriremo il terminale come amministratore. Scriveremo:

```sh
pip install numpy
```

L'installazione risulta semplicissima ma ha uno svantaggio: l'installazione
è **globale**, avviene per l'intera macchina.

Questo potrebbe essere percepita come una cosa poco rilevante. Tuttavia, in
determinate situazioni, è necessario installare diversi pacchetti, andando
a generare diverse combinazioni di versioni delle librerie. Installando una
libreria **globalmente**, _tutti_ i programmi dovranno usare la versione
installata. Questo potrebbe essere un grosso vincolo poiché delle versioni
di un pacchetto potrebbero richiedere determinate versioni di un altro
pacchetto; lavorando su diversi progetti andremmo a creare dei conflitti.

## B.2 – Opzione B: un ambiente virtuale

La seconda opzione è quella di utilizzare un _ambiente virtuale_ (sempre usando
`pip`).

Un ambiente virtuale non è altro che un ambiente, per l'appunto virtuale,
separato, sempre all'interno della macchina. In questo ambiente potremo
inserire tutte le librerie che verranno usate per il progetto, con specifiche
versioni.

Iniziamo creando un ambiente virtuale. usiamo la libreria Python, che
installeremo globalmente.

> <details>
> <summary>✏️ <strong>Nota</strong></summary>
>
> L'installazione **globale** delle librerie per la gestione dell'ambiente
> virtuale è necessaria e non contraddice il concetto descritto
> precedentemente. Possiamo creare un ambiente virtuale in qualsiasi momento.
>
> </details>

Installiamo (per Linux) [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/)
oppure (per Windows) [`virtualenvwrapper-win`](https://pypi.org/project/virtualenvwrapper-win/):

| Linux                           | Windows                             |
| :------------------------------ | :---------------------------------- |
| `pip install virtualenvwrapper` | `pip install virtualenvwrapper-win` |

Una volta completata l'installazione, usiamo il comando `mkvirtualenv <nome>`
per creare un ambiente virtuale con nome `<nome>`. Ad esempio:

```sh
mkvirtualenv pcs
```

A sinistra del terminale sarà comparso il nome dell'ambiente virtuale:

```sh
(pcs) ~$
```

Questo indica che siamo all'interno dell'ambiente virtuale. Installiamo la
libreria `numpy` usando `pip`:

```sh
(pcs) ~$ pip install numpy
```

Così facendo, installiamo numpy **esclusivamente** all'interno dell'ambiente
virtuale. Per verificarlo eseguiamo l'istruzione `pip freeze`, che restituisce
tutte le librerie presenti nell'ambiente in cui siamo attualmente, con le
relative versioni.

> <details>
> <summary>ℹ️ <em>Il file <code>requirements.txt</code></em></summary>
>
> È pratica comune memorizzare tutte le librerie presenti in un ambiente
> virtuale in un file chiamato `requirements.txt`. In questo modo, un altro
> programmatore sarà in grado di clonare l'ambiente virtuale. Per salvare il
> file, usiamo il seguente comando:
>
> ```sh
> $ pip freeze > requirements.txt
> ```
>
> Per clonare l'ambiente:
>
> ```sh
> $ pip install -r requirements.txt
> ```
>
> Dove il flag `-r` sta per _recursively_ e indica di installare ricorsivamente
> le librerie presenti nel `requirements.txt`
>
> </details>

## B.3 – Opzione C: una distribuzione per il calcolo scientifico

La terza opzione è quella di utilizzare una distribuzione Python pensata
proprio per il calcolo scientifico. Un esempio è [Anaconda](https://www.anaconda.com/products/distribution).
Scarichiamo l'installer dal sito ufficiale e seguiamo la normale procedura di
installazione.

Il vantaggio dell'utilizzare una distribuzione di questo tipo sta nell'avere
a disposizione, _di default_, la maggior parte delle librerie utilizzate in
ambito scientifico. È necessario ricordare che la libreria è pensata solo per
il calcolo scientifico e va tenuto a mente se si volesse usare Python per altri
scopi.

> <details open>
> <summary>ℹ️ <em>Il package-manager di Anaconda</em></summary>
>
> La distribuzione di Anaconda ha il suo package manager, chiamato `conda`.
> Questo sostituisce (ma non del tutto) `pip`.
>
> </details>

## B.4 – Opzione D: un package manager come `pipenv`

L'ultima opzione, che è quella suggerita per l'utilizzo professionale e
eterogeneo di Python, è quella di usare `pipenv`.

Questo package-manager automatizza e semplifica la creazione di un ambiente
virtuale, sempre usando `pip`. Lo strumento offre un'interfaccia utente snella
e si occupa autonomamente di selezionare le ultime versioni disponibili dei
pacchetti che utilizziamo.

Installiamo `pipenv`:

```sh
$ pip install pipenv
Collecting pipenv
  Downloading pipenv-2022.6.7-py2.py3-none-any.whl (3.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 12.0 MB/s eta 0:00:00
```

Dopo l'installazione, spostiamoci nella cartella in cui vogliamo creare
l'ambiente virtuale (che conterrà solo numpy) e scriviamo:

```sh
$ pipenv install numpy
Pipfile: C:\Users\pc\prova\Pipfile
Using C:/Python310/python.exe (3.10.5) to create virtualenv...
[==  ] Creating virtual environment...created virtual environment
# ...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

Al termine della procedura, verranno generati due file:

- `Pipfile`, conterrà tutte le dipendenze che son state aggiunte al progetto;
- `Pipfile.lock`, conterrà delle informazioni dettagliate sulle librerie usate,
  incluse versioni, repository, etc.

`pipenv` non si limita a creare questi due file poiché provvede a definire,
automaticamente, un nuovo ambiente virtuale. All'interno di questo saranno
memorizzate tutte le librerie installate per il progetto.
Per accedere all'ambiente virtuale useremo il comando `pipenv shell`, Se invece
non volessimo accedervi, useremo il comando `pipenv run <comando-da-eseguire>`
dove `<comando-da-eseguire>` è il comando che vogliamo eseguire.

Se volessimo eseguire un ipotetico script `run.py` _accedendo_ all'ambiente
virtuale, scriveremo:

```sh
$ pipenv shell
Launching subshell in virtual environment...
# ...
$ python run.py
'Hello, World!'
```

Se invece non volessimo accedere all'ambiente virtuale, scriveremo:

```sh
$ pipenv run python run.py
'Hello, World!'
```

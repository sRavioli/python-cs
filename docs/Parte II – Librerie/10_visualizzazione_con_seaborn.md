# 10 – Visualizzazione di dati in Seaborn

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
<summary>Outline</summary>

<!-- TOC -->

1. [10 – Visualizzazione di dati in Seaborn](#10--visualizzazione-di-dati-in-seaborn)
   1. [Installazione di Seaborn](#installazione-di-seaborn)
2. [Lettura dei dati](#lettura-dei-dati)
   1. [Visualizzare le relazioni tra dati](#visualizzare-le-relazioni-tra-dati)
3. [Analisi della distribuzione dati](#analisi-della-distribuzione-dati)
   1. [Plot di dati categorici](#plot-di-dati-categorici)
4. [Heatmap](#heatmap)

<!-- /TOC -->

</details>

Seaborn è una libreria che estende [Matplotlib](https://python.angelocardellicchio.it/material/02_libs/08_matplotlib/lecture/)
aggiungendone diverse funzionalità, tutte nell'ottica della data analysis e
sulla scia di quello che abbiamo presentato in Pandas nella lezione precedente.
Ciò permette di mantenere un'interfaccia molto simile a quella di Matplotlib,
estendendone al contempo le possibilità. Vediamo qualche esempio.

## Installazione di Seaborn

Come sempre, installiamo la libreria:

```sh
$ conda activate <my-env>
(<my-env>) ~$ pip install seaborn
```

Importiamo la libreria e diamole un alias:

```python
import seaborn as sns
```

# Lettura dei dati

Seaborn è utile specialmente nel momento in cui si vogliono valutare
visivamente le relazioni che intercorrono tra diverse feature presenti
all'interno di un dataset.

In tal senso, proviamo innanzitutto a caricare un insieme di dati, affidandoci
al metodo `load_dataset()`, che estrae uno dei dataset già presenti nella
libreria. Ad esempio:

```pycon
>>> tips = sns.load_dataset("tips")
```

> <details>
> <summary>ℹ️ <em>Dataset supportati</em></summary>
>
> L'elenco dei dataset supportati da Seaborn è presente a [questo indirizzo](https://github.com/mwaskom/seaborn-data).
>
> </details>

Ispezionando il tipo di `tips` possiamo scoprire che si tratta di un dataframe.
Di conseguenza, possiamo esplorarne liberamente la struttura utilizzando
Pandas. In particolare, vediamo che questi sono organizzati secondo la seguente
tabella:

```pycon
>>> tips.head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

La struttura della tabella è la seguente:

- ogni riga è associata ad una specifica ordinazione;
- le colonne sono associate rispettivamente a conto (`total_bill`), mancia
  (`tip`), sesso (`sex`), fumatore (`smoker`), giorno (`day`), orario (`time`)
  e numero di clienti (`size`).

## Visualizzare le relazioni tra dati

Seaborn ci offre la funzione `relplot()` che ci permette di analizzare
velocemente diversi aspetti inclusi del dataset. Ad esempio, potremmo vedere
come cambiano conto e mancia al variare della giornata:

```python
sns.relplot(data=tips, x="total_bill", y="tip", col="day")
```

Abbiamo passato al parametro data il valore tips, indicando quindi la sorgente
dei dati. Metteremo poi sull'asse delle ascisse il conto totale, mentre su
quello delle ordinate la mancia ricevuta. In ultimo, il parametro `col` ci
permette di generare tanti grafici quanti sono i diversi valori presenti nella
tabella `day`, ognuno dei quali rappresenterà ovviamente l'andamento dei conti
e delle mance per quello specifico giorno.

![Mancia e conto in base al giorno (sns, `relplot()`)](../img/seaborn/tip-bill_per_day.png)

È possibile avere un singolo grafico utilizzando l'opzione `hue`:

```python
sns.relplot(data=tips, x="total_bill", y="tip", hue="day")
```

![Mancia e conto il base al giorno, singolo (sns, `relplot()`)](../img/seaborn/tip-bill_per_day_HUE.png)

Un altro esperimento consiste nel valutare la differenza tra conto e mance
pagati da uomini e donne. In questo caso, andiamo anche ad aumentare la
dimensione del punto in maniera direttamente proporzionale alla mancia
percepita:

```python
sns.relplot(data=tips, x="total_bill", y="tip", col="sex", size="tip")
```

ottenendo il seguente grafico:

![Differenza tra conto e mance in base al sesso (sns, `relplot()`)](../img/seaborn/tip-bill_sex.png)

Una funzione simile alla `relplot()` è la `lmplot()`, che permette anche di
mostrare un'approssimazione ai minimi quadrati dei dati. Ad esempio:

```python
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="day")
```

![Approssimazione ai minimi quadrati dei dati (sns, `lmplot()`)](../img/seaborn/tips_lmplot.png)

# Analisi della distribuzione dati

Possiamo effettuare un'analisi della distribuzione delle variabili all'interno
del nostro dataset. La funzione `displot()` ci permette di vedere come si vanno
a distribuire i dati in base a determinate condizioni mediante l'uso di un
istogramma.

Ad esempio, potremmo visualizzare la distribuzione dei clienti in base al loro
sesso ed al momento della giornata in cui effettuano la consumazione:

```python
sns.displot(data=tips, x="sex", col="time", kde=True)
```

Otterremo il seguente risultato:

![Distribuzione dei clienti in base al sesso e orario (sns, `displot()`)](../img/seaborn/client-time-sex_displot.png)

Specificando il parametro `kde`, è possibile ottenere un'approssimazione della
distribuzione mediante _kernel density estimation_, come mostrato nella figura
seguente:

![Distribuzione dei clienti in base al sesso e orario con kde (sns, `displot()`)](../img/seaborn/client-time-sex_displot_kde.png)

## Plot di dati categorici

Seaborn offre anche dei plot specializzati per la creazione e visualizzazione
di dati (o feature) di tipo categorico, ovvero dati appartenenti ad una tra le
diverse possibili categorie. In tal senso, un esempio di feature categorica è
il genere dei clienti del ristorante, che nel dataset sono soltanto uomini o
donne.

I plot di questo tipo possono essere generati mediante la funzione [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html),
delegata alla definizione di plot a diversi livelli di granularità, come ad
esempio i violin plot.

```python
sns.catplot(data=tips, kind="violin", x="day", y="tip", hue="sex", split=True)
```

![Distribuzione delle mance al variare del sesso, giorno per giorno (sns, `catplot()`)](../img/seaborn/tips_catplot.png)

In particolare, il grafico mostrato in figura descrive la distribuzione delle
mance giorno per giorno al variare del sesso del cliente.

> <details>
> <summary>💡 <em>Suggerimento</em></summary>
>
> In realtà, è possibile usare la `catplot()` con dati non categorici, come
> numeri interi. Tuttavia, vi è il rischio (o meglio, la certezza) che il
> risultato sia non interpretabile, in quanto la funzione assegnerà una
> categoria ad ogni possibile valore assunto dalla feature di riferimento, il
> che ovviamente comporterà l'illeggibilità del grafico nel caso di valori
> reali.
>
> </details>

# Heatmap

Un'ultima funzione che vale la pena menzionare è quella che ci permette di
visualizzare le _heatmap_, ovvero delle strutture grafiche che consentono di
visualizzare rapidamente gli intervalli in cui ricadono i valori di diversi
tipi di matrici. Questa funzione è, per l'appunto, chiamata `heatmap()`, e
richiede in ingresso almeno il parametro relativo alla matrice da cui sarà
estratta la figura. Ad esempio (considerando importato numpy):

```python
ar = np.array([[5, 12], [4, 3]])
sns.heatmap(ar, cmap="jet", annot=True, xticklabels=False, yticklabels=False)
```

Nella precedente invocazione della funzione `heatmap()` specifichiamo i
parametri indicati in modo da passare un array (o similari) come primo
argomento, seguito da una `colormap` (`cmap`), ovvero i colori da utilizzare.
Specifichiamo inoltre che vogliamo inserire i valori dell'array su ciascuna
delle celle dell'heatmap (mediante il parametro `annot`) e che non vogliamo
visualizzare i label sugli assi $x$ e $y$ (`xticklabels` e `yticklabels`
rispettivamente). Otterremo questo risultato:

![Heatmap di un array (sns, `heatmap()`)](../img/seaborn/array_heatmap.png)

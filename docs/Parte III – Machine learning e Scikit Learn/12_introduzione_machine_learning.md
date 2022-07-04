# 12 – Introduzione al machine learning

> Corso di Python per il Calcolo Scientifico
>
> Appunti redatti da Simone Fidanza, s.fidanza1@studenti.uniba.it

Angelo Cardellicchio, angelo.cardellicchio@stiima.cnr.it

<details>
    <summary>Outline</summary>

<a name="top"></a>

<!-- TOC -->

1. [12 – Introduzione al machine learning](#12--introduzione-al-machine-learning)
   1. [Tipi di sistemi di machine learning (⮨)](#tipi-di-sistemi-di-machine-learning-)
   2. [Sistemi ad apprendimento supervisionato (⮨)](#sistemi-ad-apprendimento-supervisionato-)
      1. [Modelli di regressione (⮨)](#modelli-di-regressione-)
      2. [Modelli di classificazione (⮨)](#modelli-di-classificazione-)
   3. [Sistemi ad apprendimento non supervisionato (⮨)](#sistemi-ad-apprendimento-non-supervisionato-)
   4. [Sistemi di reinforcement learning (⮨)](#sistemi-di-reinforcement-learning-)

<!-- /TOC -->

</details>

Il _machine learning_ è alla base di alcune delle più importanti tecnologie
odierne. Le sue applicazioni sono molteplici: dagli strumenti di traduzione
automatica ai veicoli autonomi ma anche sistemi di videosorveglianza e software
per scrivere codice.

L'avvento del machine learning ha offerto un modo alternativo e più efficace
di risolvere problemi estremamente complessi.
Potremmo dire che questo rappresenta il procedimento che insegna ad un software,
chiamato _modello_, a fare predizioni significative a partire da un insieme di
dati. In altri termini:

> Un modello di machine learning rappresenta la relazione matematica
> intercorrente tra i dati che il sistema derivante utilizza per effettuare
> predizioni.

Come esempio, immaginiamo di creare un software che effettui la predizione del
quantitativo di pioggia che cadrà in una zona. Per farlo, possiamo usare due
approcci:

- nell'approccio **tradizionale**, creeremo una rappresentazione fisica
  dell'atmosfera e della superficie terrestre, risolvendo equazioni
  estremamente complesse come quelle di Navier-Stokes;
- nell'approccio **basato sul machine learning**, daremo ad un modello un
  quantitativo adeguato (molto spesso enorme) di dati riguardanti le
  condizioni meteorologiche, fino a che il modello stesso non apprenderà le
  relazioni sottostanti i diversi pattern di feature meteorologiche che
  permettono di produrre diversi quantitativi di pioggia.

In entrambi i casi, una volta completata l'implementazione (per l'approccio
tradizionale) o l'addestramento (per l'approccio con machine learning) passeremo
al software i dati sulla condizione meteorologica attuale, per poi predire il
quantitativo di pioggia previsto.

## Tipi di sistemi di machine learning ([⮨](#top))

I sistemi di machine learning sono divisi in tre diverse categorie, distinte
tra loro sulla base del modello di apprendimento di determinate azioni

## Sistemi ad apprendimento supervisionato ([⮨](#top))

I sistemi ad apprendimento supervisionato (_supervised learning_) effettuano
una predizione dopo aver appreso le relazioni intercorrenti tra un numero più
o meno grande di dati e i corrispondenti valori da predire. Un sistema di questo
tipo è un po' come uno studente di matematica che, dopo aver appreso i metodi
per la risoluzione di un problema di analisi mediante la risoluzione di un gran
numero degli stessi, si prepara a sostenere l'esame.

> <details>
> <summary>ℹ️ <em>Perché supervisionato?</em></summary>
>
> L'appellativo supervisionato deriva dal fatto che è (di solito) un esperto
> di dominio a fornire al sistema i dati con i risultati corretti.
>
> </details>

I più importanti approcci all'apprendimento supervisionato sono la
**_regressione_** e la **_classificazione_**.

### Modelli di regressione ([⮨](#top))

Un _modello di regressione_ predice un valore numerico. Ad esempio, un modello
meteorologico di regressione, potrebbe predire il quantitativo di pioggia in
millimetri, mentre un altro modello di regressione potrebbe valutare
l'andamento dei prezzi delle proprietà immobiliari sulla base di dati come i
metri quadri, la posizione e le caratteristiche della casa, nonché la
situazione attuale dei mercati finanziario ed immobiliare.

### Modelli di classificazione ([⮨](#top))

Esistono due macro-categorie di modelli di classificazione:

- **binari**: distinguono esclusivamente tra due valore, ad esempio un modello
  di classificazione delle email che indica se il messaggio è di spam o meno;
- **multiclasse**: distinguono tra più classi, ad esempio un modello di
  riconoscimento di foto che può riconoscere oggetti di classe gatto, gane,
  gallina, oca, etc.

## Sistemi ad apprendimento non supervisionato ([⮨](#top))

I _sistemi ad apprendimento non supervisionato_ compiono delle predizioni a
partire da dati che non contengono alcuna informazione sulla classe di
appartenenza o sul valore di regressione. In pratica, i modelli non
supervisionati hanno il compito di identificare pattern significativi
_direttamente nei dati_, senza alcun "indizio" a priori, ma limitandosi ad
inferire automaticamente le proprie regole.

Algoritmi comunemente utilizzati in tal senso sono quelli di _clustering_, nei
quali il modello individua come i dati vanno a "disporsi" utilizzando delle
regole basate su distanze o capacità di "agglomerarsi".

Il clustering differisce dagli algoritmi supervisionati e, in particolare,
dalla classificazione principalmente perché le categorie non sono definite a
priori da un esperto di dominio. Ad esempio, un algoritmo di clustering
potrebbe raggruppare i campioni in un dataset meteo esclusivamente sulla base
delle temperature, rivelando delle suddivisioni che definiscono le diverse
stagioni, o anche gli orari del giorno. Sarà poi nostro compito "provare" a dare
un nome a questi cluster sulla base della nostra interpretazione del dataset.

## Sistemi di reinforcement learning ([⮨](#top))

I sistemi di _reinforcement learning_ effettuano delle predizioni a partire da
ricompense o penalità basate sulle azioni effettuate da un _agente_ all'interno
di un _ambiente_. Sulla base di queste osservazioni, il sistema di reinforcement
learning genera una _policy_ che definisce la strategia migliore per raggiungere
lo scopo prefissato.

Le applicazioni dei sistemi di questo tipo sono varie, e spaziano
dall'addestramento dei robot per svolgere task anche complesse, alla creazione
di programmi come Alpha Go che sfidino (e battano) gli umani al gioco del Go.

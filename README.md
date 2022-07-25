# ![Python](./docs/img/py.png) Python per il calcolo scientifico

> Al momento il progetto è in fase di sviluppo

In questa repository sono presenti appunti, esercizi e codice relativi al corso
"Python per il calcolo scientifico", avente una [sua repository](https://github.com/anhelus/python-calcolo-numerico).

Questo progetto propone un ampliamento degli appunti caricati nella repository
precedente, nonché includere gli esercizi svolti sia a lezione che non.

## Struttura della repository

La struttura della repository è semplice:

- `📁 docs` contiene tutti gli appunti del corso;
- `📁 jbooks` contiene tutti i Jupyter Notebooks relativi al corso;
- `📁 py` contiene tutti i file `.py` relativi al corso;
- `📁 .husky` contiene i _Git hooks_.

### `📁 docs`

Ogni file Markdown ([GitHub Flavoured Markdown](https://github.github.com/gfm/)),
corrisponde ad un argomento/capitolo differente. Per facilitarne la navigazione
presentano un indice a due cifre seguito da un'abbreviazione del
titolo dell'argomento, ad esempio: `00_introduzione_corso.md`.

### `📁 jbooks`

Ogni notebook corrisponde ad un esempio o esercizio relativo ad un argomento.
Per facilitarne la consultazione è presente un indice ([index.md](jbooks/index.md)).

### `📁 py`

Ogni file Python corrisponde ad un esercizio svolto a lezione, oppure che è
stato assegnato. Per facilitarne la navigazione, sono divisi a seconda
dell'argomento o del capitolo, inoltre presenteranno il seguente formato:

- un numero, corrispondente al numero dell'esercizio;
- una lettera maiuscola indicante se l'esercizio è stato svolto a lezione (`L`)
  oppure a casa (`H`);
- un nome, che è un breve riassunto della traccia.

Dunque i file saranno del tipo `<num>_<L/H>_<nome_breve>.py`,
ad esempio: `01_L_itera_while.py`.

Nelle prime righe di ogni file di esercizi sarà riportata la traccia dello
stesso.

I file presenteranno una soluzione, dopo questa sarà presente quella del
professore che sarà commentata. Ogni esercizio sarà commentato a dovere.

### `📁 .husky`

[Husky](https://github.com/typicode/husky) è un pacchetto che semplifica la
creazione dei _Git hooks_.

Nella cartella sono presenti due _hooks_:

1. L'hook creato da [commitlint](https://github.com/conventional-changelog/commitlint),
   che controlla che i messaggi di _commit_ seguano la specifica
   [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/);
2. Un hook personalizzato. Questo, prima di effettuare il _push_, controlla se
   il file `noodles.yaml` (dove viene esportato l'ambiente _conda_) è stato
   aggiornato.

## Importare l'ambiente conda

Come importare l'ambiente conda dal file `noodles.yaml`. È necessario aprire una
finestra di terminale per i seguenti passaggi:

1. Creare l'ambiente dal file `noodles.yaml`:

   ```shell
   conda env create -f noodles.yaml
   ```

2. Attivare l'ambiente appena creato:

   ```shell
   conda activate noodles
   ```

3. Verificare che l'ambiente sia stato installato correttamente:

   ```shell
   conda env list
   ```

   oppure `conda info --envs`

Maggiori informazioni sono disponibili su [docs.conda.io](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

## License

The content of the project itself is licensed under the
[GNU General Public License v3.0](https://github.com/sRavioli/pythoncs/blob/main/LICENCE.txt).

The content of this project takes heavy inspiration from the repository
[anhelus/python-calcolo-numerico](https://github.com/anhelus/python-calcolo-numerico),
which is licensed under the [MIT License](https://github.com/anhelus/python-calcolo-numerico/blob/master/LICENSE).

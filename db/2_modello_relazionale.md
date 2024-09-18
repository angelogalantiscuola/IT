## Modello Relazionale <!-- omit in toc -->

- [Relazioni e Tabelle](#relazioni-e-tabelle)
- [Caratteristiche del Modello Relazionale](#caratteristiche-del-modello-relazionale)
- [Operazioni sulle Relazioni](#operazioni-sulle-relazioni)


Il **modello relazionale** è un approccio alla gestione dei dati introdotto da Edgar F. Codd nel 1970. Questo modello ha rivoluzionato il modo in cui i dati vengono organizzati e gestiti, rendendoli più accessibili e facilmente manipolabili. L'idea di base è quella di rappresentare i dati sotto forma di tabelle (o *relazioni*), in cui ogni tabella rappresenta un insieme di entità con caratteristiche comuni.

### Relazioni e Tabelle

Nel modello relazionale, i dati sono strutturati in tabelle, che rappresentano delle **relazioni**. Ogni tabella è composta da righe e colonne:
- **Righe**: rappresentano le singole occorrenze delle entità, chiamate anche **tuple**.
- **Colonne**: corrispondono agli attributi dell'entità, ovvero le proprietà o caratteristiche che descrivono le tuple.

Ad esempio, una tabella che rappresenta un insieme di studenti potrebbe avere colonne come "ID", "Nome", "Cognome" e "Età", e ogni riga della tabella rappresenterebbe un singolo studente.

### Caratteristiche del Modello Relazionale

Il modello relazionale si basa su alcune proprietà chiave che lo rendono efficace:

- **Integrità dei dati**: Grazie a regole precise (come le chiavi e i vincoli di integrità, trattati nella lezione successiva), i dati sono sempre consistenti e conformi alle specifiche definite.
  
- **Accessibilità tramite linguaggi dichiarativi**: I dati in un database relazionale possono essere interrogati e manipolati utilizzando linguaggi di alto livello come SQL, che permette agli utenti di descrivere *cosa* vogliono ottenere senza specificare *come* il sistema debba eseguire l'operazione.

- **Indipendenza fisica e logica dei dati**: Nel modello relazionale, l'archiviazione fisica dei dati è separata dalla rappresentazione logica. Questo significa che gli utenti possono lavorare con una rappresentazione astratta (le tabelle), senza preoccuparsi di come i dati siano effettivamente salvati sul disco.

### Operazioni sulle Relazioni

Il modello relazionale si basa su un insieme di operazioni che permettono di manipolare i dati contenuti nelle tabelle. Queste operazioni costituiscono l'**algebra relazionale** e includono:

- **Selezione**: consente di estrarre righe specifiche da una tabella in base a determinati criteri.
  
- **Proiezione**: permette di selezionare solo alcune colonne di una tabella, eliminando le altre.

- **Join**: questa operazione unisce due o più tabelle in base a una relazione comune tra di esse. Ad esempio, una tabella "Studenti" può essere collegata a una tabella "Corsi" attraverso un attributo condiviso come "IDStudente".
  
- **Unione e Intersezione**: consentono di combinare o confrontare i risultati di due query, unendo insiemi di tuple o trovando le tuple comuni.

Queste operazioni sono fondamentali per ottenere e manipolare dati nel contesto di un database relazionale, e sono formalmente espresse attraverso SQL (approfondito nella lezione dedicata al linguaggio SQL).

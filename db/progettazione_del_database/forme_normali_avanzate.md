## Forme Normali Avanzate <!-- omit in toc -->

- [Boyce-Codd Normal Form (BCNF)](#boyce-codd-normal-form-bcnf)
  - [Esempio di violazione della BCNF](#esempio-di-violazione-della-bcnf)
- [Quarta Forma Normale (4NF)](#quarta-forma-normale-4nf)
  - [Esempio di violazione della 4NF](#esempio-di-violazione-della-4nf)
- [Quinta Forma Normale (5NF)](#quinta-forma-normale-5nf)
  - [Esempio di violazione della 5NF](#esempio-di-violazione-della-5nf)
- [Conclusione](#conclusione)


Le **forme normali avanzate** rappresentano estensioni e rafforzamenti delle forme normali di base (1NF, 2NF, 3NF) viste in precedenza. In particolare, si concentrano sulla risoluzione di problematiche più complesse legate alla ridondanza dei dati e alle dipendenze funzionali tra gli attributi. Le forme normali avanzate più importanti sono la **Boyce-Codd Normal Form (BCNF)** e la **Quarta e Quinta Forma Normale (4NF e 5NF)**.

Queste forme sono utilizzate quando la complessità della struttura dei dati richiede un'ulteriore suddivisione delle tabelle, riducendo così al minimo le anomalie e migliorando l'integrità dei dati.

### Boyce-Codd Normal Form (BCNF)

La **BCNF** è una forma normale che rappresenta un'estensione della Terza Forma Normale (3NF), con una condizione più rigorosa per eliminare le dipendenze non desiderate. Una tabella è in **BCNF** se soddisfa le seguenti condizioni:
1. È in 3NF.
2. Ogni determinante (un attributo o un insieme di attributi che determina un altro attributo) deve essere una chiave candidata.

In parole semplici, la BCNF rimuove le situazioni in cui esistono dipendenze che non coinvolgono una chiave candidata come determinante. Le chiavi candidate sono insiemi di attributi che potrebbero fungere da chiave primaria.

#### Esempio di violazione della BCNF

Consideriamo una tabella che registra il docente e il corso che insegna in una determinata aula:

| Aula | Docente     | Corso      |
| ---- | ----------- | ---------- |
| A101 | Prof. Rossi | Matematica |
| A102 | Prof. Verdi | Fisica     |
| A101 | Prof. Rossi | Fisica     |

In questa tabella, la chiave candidata potrebbe essere la combinazione di "Aula" e "Corso". Tuttavia, la colonna "Docente" dipende solo dall'"Aula" e non dalla combinazione completa, violando la BCNF.

Per correggere questo, è possibile suddividere i dati in due tabelle:

**Tabella Aule-Docenti:**

| Aula | Docente     |
| ---- | ----------- |
| A101 | Prof. Rossi |
| A102 | Prof. Verdi |

**Tabella Aule-Corsi:**

| Aula | Corso      |
| ---- | ---------- |
| A101 | Matematica |
| A101 | Fisica     |
| A102 | Fisica     |

In questo modo, abbiamo eliminato la dipendenza parziale, portando la struttura in BCNF.

### Quarta Forma Normale (4NF)

La **Quarta Forma Normale (4NF)** si concentra sull'eliminazione delle **dipendenze multi-valore**. Una tabella è in 4NF se:
1. È in BCNF.
2. Non contiene dipendenze multi-valore, ovvero ogni attributo dipende interamente dalla chiave primaria e non esistono insiemi di attributi che possano variare indipendentemente tra loro in una stessa riga.

Una dipendenza multi-valore si verifica quando, per una stessa chiave, esistono più valori indipendenti che potrebbero essere suddivisi in più tabelle.

#### Esempio di violazione della 4NF

Consideriamo una tabella che registra i progetti e le competenze richieste per ciascun dipendente:

| Dipendente | Progetto   | Competenza |
| ---------- | ---------- | ---------- |
| Mario      | Progetto A | Java       |
| Mario      | Progetto A | Python     |
| Mario      | Progetto B | Java       |

In questo esempio, il dipendente Mario è assegnato a più progetti e possiede più competenze. Tuttavia, le competenze e i progetti sono indipendenti tra loro, il che rappresenta una dipendenza multi-valore.

Per risolvere questo, possiamo creare due tabelle separate:

**Tabella Progetti-Dipendenti:**

| Dipendente | Progetto   |
| ---------- | ---------- |
| Mario      | Progetto A |
| Mario      | Progetto B |

**Tabella Competenze-Dipendenti:**

| Dipendente | Competenza |
| ---------- | ---------- |
| Mario      | Java       |
| Mario      | Python     |

In questo modo, abbiamo eliminato le dipendenze multi-valore e portato la struttura in 4NF.

### Quinta Forma Normale (5NF)

La **Quinta Forma Normale (5NF)**, conosciuta anche come **Proiezione-Join Normal Form (PJNF)**, si occupa di eliminare le **dipendenze join**. Una tabella è in 5NF se:
1. È in 4NF.
2. Non contiene dipendenze che possano essere scomposte in più tabelle tramite operazioni di join.

La 5NF si applica in casi rari, in cui una relazione complessa tra attributi può essere scomposta in più tabelle senza perdita di informazioni. Questo accade quando i dati possono essere ricostruiti tramite join senza introdurre inconsistenze o duplicati.

#### Esempio di violazione della 5NF

Consideriamo una tabella che rappresenta le relazioni tra fornitori, parti e progetti:

| Fornitore | Parte | Progetto   |
| --------- | ----- | ---------- |
| F1        | P1    | Progetto X |
| F1        | P2    | Progetto Y |
| F2        | P1    | Progetto X |

In questo caso, esistono dipendenze tra "Fornitore", "Parte" e "Progetto". Tuttavia, è possibile suddividere la tabella in tre relazioni separate senza perdita di informazioni:

**Tabella Fornitori-Parti:**

| Fornitore | Parte |
| --------- | ----- |
| F1        | P1    |
| F1        | P2    |
| F2        | P1    |

**Tabella Fornitori-Progetti:**

| Fornitore | Progetto   |
| --------- | ---------- |
| F1        | Progetto X |
| F1        | Progetto Y |
| F2        | Progetto X |

**Tabella Parti-Progetti:**

| Parte | Progetto   |
| ----- | ---------- |
| P1    | Progetto X |
| P2    | Progetto Y |

Applicando queste suddivisioni, la struttura si trova ora in 5NF, eliminando le dipendenze complesse e garantendo che i dati possano essere ricostruiti tramite join senza perdita o duplicazione.

### Conclusione

Le forme normali avanzate, come la **BCNF**, la **4NF** e la **5NF**, rappresentano passi successivi nella normalizzazione di un database, affrontando problematiche complesse come le dipendenze multi-valore e le dipendenze join. Sebbene in molti casi i database possano funzionare efficientemente applicando solo le prime tre forme normali, in situazioni più avanzate, l'applicazione di queste forme superiori è essenziale per garantire un'organizzazione ottimale e l'integrità dei dati.

> **Nota**: La normalizzazione deve essere bilanciata con le esigenze pratiche di performance, poiché una suddivisione eccessiva delle tabelle potrebbe rallentare le query in sistemi con grandi volumi di dati.
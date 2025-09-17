## Progettazione del Database <!-- omit in toc -->

- [Fasi della Progettazione del Database](#fasi-della-progettazione-del-database)

La **progettazione del database** è il processo di creazione della struttura logica e fisica di un database, assicurando che i dati siano organizzati in modo efficiente e che possano essere gestiti in modo coerente e sicuro. Una corretta progettazione permette di ottimizzare le prestazioni, migliorare l'integrità dei dati e ridurre il rischio di errori o ridondanze.

### Fasi della Progettazione del Database

La progettazione di un database si articola in diverse fasi sequenziali, che trasformano un'idea astratta in un sistema concreto. Questo approccio è spesso chiamato **"design-first"**.

1.  **Analisi dei Requisiti**: Comprendere le necessità del committente e definire quali dati devono essere memorizzati e quali operazioni devono essere eseguite.
2.  **Progettazione Concettuale**: Creare un modello ad alto livello dei dati e delle loro relazioni, indipendentemente dal DBMS specifico. Lo strumento principale di questa fase è il **Diagramma Entità-Relazione (ER)**.
3.  **Progettazione Logica**: Tradurre il modello concettuale (il diagramma ER) in uno schema relazionale, definendo tabelle, colonne, chiavi e vincoli. In questa fase si applica la **normalizzazione**.
4.  **Progettazione Fisica**: Definire come il database sarà effettivamente memorizzato e gestito dal DBMS. Questa fase include la scelta degli indici, l'allocazione dello spazio su disco e altre ottimizzazioni per le performance.

Nelle prossime lezioni, analizzeremo in dettaglio ciascuna di queste fasi.

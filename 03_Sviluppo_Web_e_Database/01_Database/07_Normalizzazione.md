## Normalizzazione del Database <!-- omit in toc -->

- [Perché Normalizzare?](#perché-normalizzare)
- [Prima Forma Normale (1NF)](#prima-forma-normale-1nf)
- [Seconda Forma Normale (2NF)](#seconda-forma-normale-2nf)
- [Terza Forma Normale (3NF)](#terza-forma-normale-3nf)

La **normalizzazione** è un processo sistematico di progettazione che organizza le tabelle in un database relazionale per minimizzare la **ridondanza dei dati** e migliorare l'**integrità dei dati**. Lo scopo è suddividere tabelle grandi e complesse in tabelle più piccole e ben strutturate.

### Perché Normalizzare?

Un database non normalizzato può soffrire di "anomalie" dei dati:

- **Anomalia di Inserimento**: Impossibilità di aggiungere un dato perché ne manca un altro (es. non posso aggiungere un nuovo corso se non ha ancora studenti iscritti).
- **Anomalia di Aggiornamento**: La modifica di un dato richiede l'aggiornamento di più righe, con il rischio di incoerenze (es. se un docente cambia ufficio, devo aggiornare la riga per ogni corso che insegna).
- **Anomalia di Cancellazione**: La rimozione di una riga causa la perdita involontaria di altri dati (es. se cancello l'unico studente iscritto a un corso, perdo anche le informazioni sul corso stesso).

La normalizzazione risolve questi problemi applicando una serie di regole chiamate **Forme Normali**.

### Prima Forma Normale (1NF)

**Regola**: Ogni cella della tabella deve contenere un valore atomico (indivisibile), e ogni riga deve essere unica.

- **Violazione**: Una colonna `telefoni` che contiene `"333111, 333222"`.
- **Soluzione**: Creare una tabella separata `Telefoni_Studente` per memorizzare i numeri di telefono, collegandola alla tabella principale `Studenti` con una chiave esterna.

### Seconda Forma Normale (2NF)

**Regola**: La tabella deve essere in 1NF e ogni attributo non-chiave deve dipendere funzionalmente dall'**intera** chiave primaria. (Questa regola è rilevante solo per tabelle con chiavi primarie composite).

- **Violazione**: Una tabella `Iscrizioni(id_studente, id_corso, nome_corso)`. Qui `nome_corso` dipende solo da `id_corso`, non dall'intera chiave `(id_studente, id_corso)`.
- **Soluzione**: Spostare `nome_corso` nella tabella `Corsi`. La tabella `Iscrizioni` conterrà solo le chiavi esterne.

### Terza Forma Normale (3NF)

**Regola**: La tabella deve essere in 2NF e non devono esistere dipendenze transitive. Un attributo non-chiave non deve dipendere da un altro attributo non-chiave.

- **Violazione**: Una tabella `Studenti(matricola, nome, id_dipartimento, nome_dipartimento)`. Qui `nome_dipartimento` dipende da `id_dipartimento`, che a sua volta dipende dalla chiave primaria `matricola`. Questa è una dipendenza transitiva.
- **Soluzione**: Creare una tabella `Dipartimenti(id_dipartimento, nome_dipartimento)` e mantenere solo `id_dipartimento` come chiave esterna nella tabella `Studenti`.

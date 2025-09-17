## Chiavi: Primaria ed Esterna <!-- omit in toc -->

- [Chiave Primaria (Primary Key)](#chiave-primaria-primary-key)
- [Chiave Esterna (Foreign Key)](#chiave-esterna-foreign-key)

Le **chiavi** sono attributi (o insiemi di attributi) che svolgono un ruolo speciale all'interno di un database relazionale. Servono a identificare univocamente le righe e a stabilire collegamenti logici tra le tabelle.

### Chiave Primaria (Primary Key)

La **chiave primaria (PK)** è un attributo o un insieme di attributi che **identifica univocamente ogni riga** di una tabella.

Una chiave primaria deve rispettare due vincoli fondamentali:

1.  **Unicità**: Il valore della chiave primaria deve essere unico per ogni riga della tabella. Non possono esistere due righe con lo stesso valore di chiave primaria.
2.  **Non Nullità**: Il valore della chiave primaria non può mai essere `NULL`. Ogni riga deve avere un identificatore valido.

_Esempio_: Nella tabella `Studenti`, l'attributo `Matricola` è un candidato perfetto per essere la chiave primaria, poiché ogni studente ha un numero di matricola unico.

### Chiave Esterna (Foreign Key)

La **chiave esterna (FK)** è un attributo o un insieme di attributi in una tabella che crea un **collegamento** a una chiave primaria di un'altra tabella. È il meccanismo che permette di implementare le relazioni tra le entità.

Una chiave esterna garantisce l'**integrità referenziale**: il valore di una chiave esterna deve corrispondere a un valore di chiave primaria esistente nella tabella di riferimento, oppure può essere `NULL`.

_Esempio_: Consideriamo due tabelle, `Studenti` e `Corsi`. Per sapere quale studente è iscritto a quale corso, creiamo una tabella `Iscrizioni`.

**Studenti**
| **Matricola (PK)** | Nome |
|--------------------|---------|
| 101 | Mario |
| 102 | Anna |

**Corsi**
| **ID_Corso (PK)** | Nome_Corso |
|-------------------|------------|
| C01 | Matematica |
| C02 | Fisica |

**Iscrizioni**
| **ID_Iscrizione (PK)** | **Matricola_Studente (FK)** | **ID_Corso_Iscritto (FK)** |
|------------------------|-----------------------------|----------------------------|
| 1 | 101 | C01 |
| 2 | 102 | C01 |
| 3 | 101 | C02 |

Nella tabella `Iscrizioni`:

- `Matricola_Studente` è una chiave esterna che si riferisce alla chiave primaria `Matricola` della tabella `Studenti`.
- `ID_Corso_Iscritto` è una chiave esterna che si riferisce alla chiave primaria `ID_Corso` della tabella `Corsi`.

Questo garantisce che non si possano inserire iscrizioni per studenti o corsi inesistenti.

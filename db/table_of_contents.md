# db
## Fondamenti di Database 
### Definizione di Database
### Sistema di Gestione di Database (DBMS)
### Tipologie di Database
## Modello Relazionale 
### Relazioni e Tabelle
### Caratteristiche del Modello Relazionale
### Operazioni sulle Relazioni
## Chiavi: Primaria, Esterna 
### Chiave Primaria
#### Caratteristiche della Chiave Primaria
#### Esempio di Chiave Primaria
#### Importanza della Chiave Primaria
### Chiave Esterna
#### Caratteristiche della Chiave Esterna
#### Esempio di Chiave Esterna
#### Importanza della Chiave Esterna
## Vincoli di Integrità  
### Tipologie di Vincoli di Integrità
#### Integrità dell'Entità
#### Integrità Referenziale
#### Vincoli di Dominio
#### Vincoli di Unicità
#### Vincoli di Nullità
#### Vincoli di Check
### Applicazione dei Vincoli nel DBMS
## Progettazione del Database 
### Fasi della Progettazione del Database
#### Analisi dei Requisiti
#### Progettazione Concettuale
#### Progettazione Logica
#### Progettazione Fisica
### Considerazioni sulla Scalabilità
### Conclusione
# Analisi dei Requisiti
## 1. Comunicazione con il committente
### Obiettivi dell'analisi dei requisiti
## 2. Identificazione delle entità e relazioni
# Progettazione Concettuale
## 1. Creazione del Diagramma ER
### Componenti principali del diagramma ER:
### Esempio:
## 2. Definizione delle regole di business
### Relazione con altre lezioni
## Schema Concettuale e Diagrammi ER 
### Che Cos'è uno Schema Concettuale?
#### Esempio di Schema Concettuale
### Diagrammi ER (Entity-Relationship)
#### Componenti Principali di un Diagramma ER
##### 1. Entità
##### 2. Attributi
##### 3. Relazioni
##### 4. Cardinalità delle Relazioni
#### Esempio di Diagramma ER
### Vantaggi dell'Uso dei Diagrammi ER
### Processo di Conversione in Modello Relazionale
## Normalizzazione 
### Perché Normalizzare?
### Le Forme Normali
#### Prima Forma Normale (1NF)
##### Requisiti della 1NF
##### Esempio
#### Seconda Forma Normale (2NF)
##### Requisiti della 2NF
##### Esempio
#### Terza Forma Normale (3NF)
##### Requisiti della 3NF
##### Esempio
### Conclusione
## Forme Normali Avanzate 
### Boyce-Codd Normal Form (BCNF)
#### Esempio di violazione della BCNF
### Quarta Forma Normale (4NF)
#### Esempio di violazione della 4NF
### Quinta Forma Normale (5NF)
#### Esempio di violazione della 5NF
### Conclusione
## SQL: Linguaggio per DB Relazionali 
### Caratteristiche Principali di SQL
#### Operazioni Principali
#### Linguaggio di Definizione Dati (DDL)
#### Linguaggio di Manipolazione Dati (DML)
#### Linguaggio di Controllo Dati (DCL)
### Query di Selezione: Il Cuore di SQL
#### Ordinamento e Raggruppamento
### Funzioni Aggregate
### SQL Tutorial Completo
## Uso di SQL in un Linguaggio di Programmazione 
### Connessione al Database
#### Esempio di Connessione in Python con `sqlite3`
### Esecuzione di Query SQL
#### Query di Selezione in Python con `sqlite3`
### Prevenzione delle Iniezioni SQL
#### Query Parametrizzata in Python
### Gestione delle Transazioni
#### Esempio di Transazione in Python
# Nozioni di Sicurezza 
## Tipi di Minacce alla Sicurezza
## Principali Misure di Sicurezza
### Autenticazione
### Autorizzazione e Controllo degli Accessi
### Crittografia
### Audit e Log
### Backup Sicuro
### Minimizzazione delle Superfici di Attacco
## Protezione dalle Minacce Comuni
### SQL Injection
#### Come prevenire l'SQL Injection:
### Gestione degli Utenti e Permessi
### Configurazione e Aggiornamenti di Sicurezza
## Gestione degli Utenti e Permessi 
### Concetti di Base
#### Utenti e Ruoli
#### Permessi
### Assegnazione dei Permessi
#### GRANT: Concessione di Permessi
#### REVOKE: Revoca di Permessi
#### Ruoli Dinamici
### Principi di Sicurezza
#### Privilegi Minimi
#### Controllo degli Accessi Basato sui Ruoli (RBAC)
#### Monitoraggio e Audit
### Esempi Pratici
#### Creazione di un Utente con Permessi Limitati
#### Creazione di un Ruolo e Assegnazione di Permessi
## SQL Injection e Sicurezza nelle Query 
### Che Cos'è la SQL Injection?
#### Esempio di SQL Injection
### Tipi di SQL Injection
#### Iniezione Basata su Errori
#### Iniezione Blind (Blind SQL Injection)
#### Iniezione Basata su Time Delay
### Come Prevenire la SQL Injection
#### Utilizzo di Query Parametrizzate
#### Escaping degli Input
#### Limitare i Permessi del Database
#### Validazione degli Input
#### Uso di ORM (Object-Relational Mapping)
### Esempi di Prevenzione
#### Validazione dell'Input in Python
#### Uso di un ORM in Django

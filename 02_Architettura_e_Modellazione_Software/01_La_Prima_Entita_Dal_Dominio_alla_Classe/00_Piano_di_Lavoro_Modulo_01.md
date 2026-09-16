# Piano di Lavoro: Modulo 01 - La Prima Entità: Dal Dominio alla Classe

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Modulo 00 completato (C4 Model, User Stories) e competenze di 3ª (funzioni, variabili, tipi).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Identificare la prima entità centrale del sistema partendo da una User Story.
- Modellare la singola entità in parallelo:
  - Come **Tabella su disco** nel Diagramma ER (Mermaid `erDiagram`) con definizione di Chiave Primaria (PK).
  - Come **Classe in memoria RAM** nel Diagramma UML (Mermaid `classDiagram`) con attributi e visibilità.
- Tradurre il progetto UML nella sintassi Python fondamentale: `class`, `__init__`, `self` e creazione di istanze.
- Applicare l'incapsulamento mirato: proteggere gli attributi critici (`__`) e convalidare i dati tramite `@property` e setter.
- Rendere l'oggetto espressivo tramite i metodi speciali dunder (`__str__` per gli utenti e `__repr__` per il debug).
- Scrivere i primi test automatici con **Pytest** per verificare lo stato dell'oggetto dopo la creazione e la validazione.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Modulo_01.md`
- **Lezione 02:** `02_Dall_Entita_alla_Classe_UML_ER.md`
  - Il concetto di Entità; il modello ER con Chiave Primaria (PK); la sintassi `class`, `__init__`, `self` e le istanze in Python.
- **Lezione 03:** `03_Proteggere_lo_Stato_Properties_Dunder.md`
  - Perché proteggere i dati; attributi privati (`__`); `@property` e setter con logica di validazione; metodi `__str__` e `__repr__`.

---

## 3. Metodologie di Valutazione
- Capacità di disegnare il modello ER e UML per una singola entità partendo da un testo.
- Corretta implementazione della classe in Python con costruttore valido e setter con controllo dei limiti.
- Suite di test con Pytest che verifica il corretto funzionamento di costruttore e validazioni.
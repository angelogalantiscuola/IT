# Piano di Lavoro: Modulo 02 - Quando le Entità Diventano Due (Relazioni e Sequenza)

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Modulo 01 completato (classe singola, istanze, `self`, `@dataclass` e testing base).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Gestire il ciclo di vita completo di una relazione **Uno-a-Uno (1:1)**:
  - Posizionare la **Foreign Key (FK)** con vincolo `UNIQUE` nel modello ER.
  - Tracciare il **Diagramma di Sequenza** per ricavare i metodi operativi.
  - Implementare l'associazione in Python con riferimento diretto a singolo oggetto.
- Gestire il ciclo di vita completo di una relazione **Uno-a-Molti (1:N)**:
  - Applicare la regola della Foreign Key sul lato "Molti" nel modello ER.
  - Tracciare la sequenza di aggiunta e consultazione di elementi in una collezione.
  - Implementare la relazione in Python gestendo liste di oggetti con `field(default_factory=list)`.
- Scrivere suite di test con **Pytest** per verificare la collaborazione corretta tra oggetti interconnessi.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Modulo_02.md`
- **Lezione 02:** `02_Associazione_1_a_1_ER_Sequenza_Python.md` (L'Eroe e lo Zaino: dalla FK alla sequenza al codice).
- **Lezione 03:** `03_Associazione_1_a_Molti_ER_Sequenza_Python.md` (Lo Zaino e gli Oggetti: collezioni, default_factory e metodi di gestione).

---

## 3. Metodologie di Valutazione
- Esercizio completo: data una User Story (1:1 o 1:N), produrre lo schema ER, il diagramma di sequenza, il codice Python con dataclass e i relativi test Pytest.
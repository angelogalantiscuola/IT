# Piano di Lavoro: Modulo 03 - Espansione del Sistema (Relazioni N:N ed Ereditarietà)

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Moduli 01 e 02 completati (relazioni 1:1 e 1:N, foreign key, dataclass, sequenza e pytest).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Gestire relazioni complesse **Molti-a-Molti (N:N)** applicando la regola univoca della **Tabella/Classe di Raccordo**:
  - Progettare la tabella di raccordo nel modello ER con doppia Foreign Key.
  - Modellare la classe intermedia in UML e Python (`dataclass`), gestendo anche attributi propri del legame (es. data, livello, quantità).
- Comprendere e applicare la relazione **"IS-A" (Ereditarietà a 1 livello)** per specializzare classi base.
- Utilizzare correttamente **`super().__init__()`** per riutilizzare l'inizializzazione della classe genitore.
- Implementare il **Polimorfismo** tramite l'**Override** dei metodi, verificando che oggetti di classi diverse rispondano allo stesso messaggio con comportamenti specializzati.
- Scrivere test automatici con **Pytest** per collaudare ereditarietà, tabelle di raccordo e polimorfismo.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Modulo_03.md`
- **Lezione 02:** `02_Relazioni_Molti_a_Molti_e_Entita_di_Raccordo.md` (La regola univoca N:N -> due 1:N con entità intermedia in ER, UML e Python).
- **Lezione 03:** `03_Ereditarieta_e_Polimorfismo.md` (Relazione IS-A, super(), override dei metodi e polimorfismo in azione).

---

## 3. Metodologie di Valutazione
- Modellazione di uno scenario reale N:N (es. Studenti-Corsi o Ordini-Prodotti) con produzione di schema ER, classi UML e implementazione Python.
- Esercizio di polimorfismo: creazione di una gerarchia di personaggi con metodi sovrascritti e collaudo con Pytest.
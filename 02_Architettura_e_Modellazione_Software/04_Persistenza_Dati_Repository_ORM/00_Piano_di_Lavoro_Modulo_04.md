# Piano di Lavoro: Modulo 04 - Persistenza dei Dati e Visione d'Insieme

## 1. Obiettivi di Apprendimento

### Prerequisiti
- Moduli da 01 a 03 completati (dataclass, relazioni 1:1, 1:N, N:N, schemi ER e Pytest).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
- Comprendere il concetto di **Persistenza** (memoria volatile RAM vs memoria permanente su disco).
- Implementare il salvataggio e il caricamento completo dello stato del gioco/applicazione su file **JSON** usando `dataclasses.asdict`.
- Comprendere a livello teorico i limiti dei file piatti (JSON) per sistemi complessi o multi-utente.
- Spiegare il concetto di **Disallineamento Oggetto-Relazionale** (*Impedance Mismatch*): la differenza concettuale tra il grafo di oggetti in RAM e le tabelle di un database.
- Comprendere il ruolo concettuale di un **ORM (Object-Relational Mapper)** come ponte automatico verso i database.
- Scrivere unit test con **Pytest** per collaudare il ciclo di salvataggio e ricaricamento su JSON.

---

## 2. Contenuti Teorici e Metodologici

- **Lezione 01:** `01_Mappa_Concettuale_Modulo_04.md`
- **Lezione 02:** `02_Persistenza_Pratica_con_JSON.md` (Salvataggio e ripristino di grafi di oggetti: `asdict`, scrittura/lettura JSON e test Pytest).
- **Lezione 03:** `03_Oltre_il_JSON_Database_e_ORM.md` (Teoria e Visione: limiti di JSON, disallineamento oggetti-tabelle e introduzione concettuale agli ORM).

---

## 3. Metodologie di Valutazione
- Realizzazione di un modulo di salvataggio e caricamento dello stato del gioco in JSON.
- Suite di test con Pytest che verifica: Creazione Oggetti $\to$ Salvataggio JSON $\to$ Ricaricamento $\to$ Integrità dello stato.
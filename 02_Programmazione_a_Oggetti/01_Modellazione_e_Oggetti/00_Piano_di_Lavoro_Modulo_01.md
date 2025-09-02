# Piano di Lavoro: Modulo 01 - Modellazione e Oggetti

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Piena padronanza dei concetti di programmazione imperativa (variabili, funzioni, cicli, condizionali).
*   Familiarità con l'ambiente di sviluppo (VS Code, terminale).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Spiegare la differenza fondamentale tra il paradigma imperativo e quello orientato agli oggetti.
*   Definire i concetti di classe, oggetto, attributo e metodo.
*   Leggere e creare diagrammi delle classi UML di base per rappresentare una singola entità.
*   Tradurre un semplice diagramma UML in una classe Python.
*   Tradurre una descrizione testuale di un'entità in un diagramma UML e nel codice Python corrispondente.
*   Distinguere tra attributi/metodi di istanza, di classe e statici.

## 2. Contenuti Teorici
Le lezioni di riferimento per questo modulo sono:

*   **Lezione 01:** `02_Dall_Idea_al_Progetto_UML.md`
    *   **Argomenti:** Cambio di paradigma, concetto di oggetto come entità con stato e comportamento, introduzione a UML come linguaggio di progettazione, come modellare una classe con attributi e metodi.
*   **Lezione 02:** `03_Dal_Progetto_al_Codice_Python.md`
    *   **Argomenti:** La sintassi `class` in Python, la traduzione diretta da UML a codice, il ruolo di `self`, la differenza pratica tra attributi/metodi di istanza, di classe e statici.

## 3. Attività Pratiche / Esercitazioni

L'attività centrale del modulo sarà basata sul concetto di **"progetto fil rouge"**: la creazione di un semplice gioco di ruolo (RPG) testuale. In questo primo modulo, getteremo le fondamenta.

*   **Analisi Guidata:** Analizzeremo insieme i requisiti per la classe base del nostro gioco: il `Personaggio`.
*   **Modellazione (Testo -> UML):** Gli studenti si eserciteranno a tradurre la descrizione del `Personaggio` in un diagramma delle classi UML.
*   **Implementazione (UML -> Codice):** Gli studenti implementeranno la classe `Personaggio` in Python basandosi sul diagramma creato.
*   **Esercizio Individuale:** `Esercizi/01_Il_Nostro_Eroe.md`, dove gli studenti applicheranno lo stesso processo (Testo -> UML -> Codice) per creare la classe `Nemico`.

## 4. Metodologie di Valutazione

*   **Osservazione in Laboratorio:** Valutazione della capacità di partecipare alla discussione di design e di tradurre i concetti in diagrammi e codice.
*   **Correzione Esercizi:** L'esercizio `01_Il_Nostro_Eroe.md` verrà corretto valutando sia la correttezza del diagramma UML prodotto sia la coerenza della classe Python implementata.
*   **Brevi Quiz:** Possibili piccoli quiz formativi per verificare la comprensione dei termini chiave (classe vs. oggetto, attributo vs. metodo).

## 5. Strumenti Necessari

*   Python 3.x.
*   Visual Studio Code.
*   Estensione di VS Code per visualizzare i diagrammi Mermaid (es. "Markdown Preview Mermaid Support").
# Piano di Lavoro: Modulo 03 - Relazioni tra Classi

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Piena padronanza dei concetti del Modulo 02 (costruttori, incapsulamento, properties).
*   Capacità di creare e leggere diagrammi UML per classi singole.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Spiegare la differenza concettuale tra una relazione "IS-A" (ereditarietà) e "HAS-A" (associazione).
*   Modellare in UML una gerarchia di classi utilizzando l'ereditarietà.
*   Implementare l'ereditarietà in Python, utilizzando `super()` per richiamare i costruttori della classe base.
*   Spiegare e implementare il polimorfismo attraverso l'override dei metodi.
*   Modellare in UML le associazioni tra classi, specificando le cardinalità.
*   Implementare la relazione "HAS-A" in Python, creando oggetti che contengono istanze di altre classi come attributi.

## 2. Contenuti Teorici
Le lezioni di riferimento per questo modulo sono:

*   **Lezione 01:** `02_Ereditarieta_e_Polimorfismo.md`
    *   **Argomenti:** La relazione "IS-A". Sintassi dell'ereditarietà, riutilizzo del codice, specializzazione di classi derivate, la funzione `super()`, e il concetto di polimorfismo tramite l'override dei metodi. Notazione UML per l'ereditarietà.
*   **Lezione 02:** `03_Associazioni_e_Collaborazione.md`
    *   **Argomenti:** La relazione "HAS-A". Differenza tra ereditarietà e associazione, implementazione di oggetti che ne contengono altri, collaborazione tra classi. Notazione UML per le associazioni.

## 3. Attività Pratiche / Esercitazioni

Applicheremo i concetti di relazione per espandere il mondo del nostro RPG.

*   **Modellazione ed Ereditarietà:** Progetteremo e implementeremo diverse specializzazioni del nostro `Personaggio`, come `Guerriero` e `Mago`.
*   **Modellazione e Associazione:** Progetteremo e implementeremo un `Inventario` per il nostro `Personaggio`, che a sua volta conterrà degli `Oggetti`.
*   **Esercizio Individuale:** `Esercizi/03_L_Eroe_e_il_Mondo.md`. Un esercizio guidato che unisce tutti i concetti del modulo per costruire una struttura di classi interconnesse.

## 4. Metodologie di Valutazione

*   **Correzione Esercizi:** L'esercizio `03_L_Eroe_e_il_Mondo.md` sarà valutato per la corretta applicazione di ereditarietà e associazione, sia nel diagramma UML che nel codice Python.
*   **Verifica della Comprensione:** Durante le lezioni, si valuterà la capacità degli studenti di scegliere la relazione più appropriata per un dato problema ("qui serve ereditarietà o associazione? E perché?").

## 5. Strumenti Necessari

*   Tutti gli strumenti dei moduli precedenti.
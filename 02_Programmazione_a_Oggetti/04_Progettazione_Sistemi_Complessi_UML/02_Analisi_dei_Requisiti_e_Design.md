# Lezione 1: Analisi dei Requisiti e Strategie di Design

Finora abbiamo modellato e implementato sistemi relativamente semplici, con poche classi. Ma come si affronta un problema complesso, descritto da un lungo testo di requisiti? L'obiettivo di questo modulo è imparare a trasformare quella descrizione in un progetto UML robusto.

## 1. Dall'Italiano all'UML: Una Strategia Pratica

Una tecnica molto efficace per iniziare è analizzare grammaticalmente il testo dei requisiti:

*   **I Sostantivi sono potenziali Classi:** Cerca i nomi e i concetti principali nel testo. `Studente`, `Corso`, `Prenotazione`, `Ordine`, `Prodotto` sono tutti ottimi candidati per diventare delle classi.

*   **Le Caratteristiche sono potenziali Attributi:** Per ogni sostantivo/classe che hai identificato, cerca le sue proprietà. Se hai la classe `Studente`, il testo potrebbe menzionare il suo `nome`, `cognome`, `matricola`. Questi diventeranno gli attributi.

*   **I Verbi sono potenziali Metodi o Relazioni:** Analizza le azioni e le interazioni.
    *   Se il verbo descrive un'azione che una classe **fa**, probabilmente è un **metodo**. "Lo `Studente` **si iscrive** a un corso" -> `studente.iscriviti(corso)`.
    *   Se il verbo descrive un legame statico tra due classi, probabilmente è una **relazione**. "Un `Corso` **è tenuto da** un `Docente`" -> relazione di associazione tra `Corso` e `Docente`.

## 2. Scegliere la Relazione Giusta: Le Domande Chiave

Una volta identificate le classi, la sfida più grande è modellarne le interazioni. Per scegliere la relazione giusta, poniti sempre queste domande:

#### **È una relazione "IS-A" (è un)?**
*   *Domanda:* La classe A è un tipo specializzato della classe B?
*   *Esempio:* Un `Guerriero` **è un** `Personaggio`? Sì.
*   **Soluzione UML:** Ereditarietà (Generalizzazione).

#### **È una relazione di Associazione (interagisce con)?**
*   *Domanda:* Un oggetto di classe A ha bisogno di interagire o è collegato a un oggetto di classe B?
*   *Esempi:* Un'`Automobile` **ha un** `Motore`. Un `Cliente` **usa un** `CarrelloDellaSpesa`.
*   **Soluzione UML:** Associazione (una linea continua).

## 3. Applicare le Cardinalità

Come abbiamo visto nel modulo precedente, per ogni relazione è fondamentale specificare la **cardinalità**, ovvero quanti oggetti possono essere coinvolti nel legame. Riepiloghiamo brevemente i simboli:

*   `1`: Esattamente uno.
*   `*`: Zero o più (molti).
*   `1..*`: Uno o più.
*   `0..1`: Zero o uno (opzionale).

In questa fase di progettazione, l'abilità chiave consiste nel leggere attentamente i requisiti per dedurre le cardinalità corrette.

*Esempio di analisi del requisito:*
> "Un `Cliente` può effettuare **più** `Ordini`. Ogni `Ordine` appartiene a **un solo** `Cliente`."

*Traduzione in UML:*
`Cliente "1" -- "*" Ordine`

Questa si legge: "Un `Cliente` è associato a zero o più `Ordini`, e un `Ordine` è associato a esattamente un `Cliente`."

Applicando sistematicamente questa strategia (identifica classi, attributi, metodi, scegli la relazione, e infine definisci la cardinalità), sarai in grado di trasformare qualsiasi requisito in un diagramma delle classi chiaro e ben strutturato.
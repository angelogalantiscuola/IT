# Lezione 2: Il Processo di Modellazione - Una Guida Pratica

Abbiamo analizzato diversi scenari e creato diagrammi UML. Ora, formalizziamo il processo con due diagrammi di flusso che possono servirvi come una "checklist" o una guida passo-passo quando affrontate un nuovo problema di design, specialmente per il progetto finale.

## 1. Guida al Design: Dai Requisiti al Diagramma UML

Questo flowchart vi aiuta a decidere come trasformare le informazioni di un testo in elementi UML.

```mermaid
flowchart TD
    A[Parti da un'informazione del requisito] --> B{{"È un dato semplice e primitivo?<br/>(es. nome, età, prezzo, un numero, una stringa...)"}};
    B -->|Sì| C[È un <b>Attributo</b> di una classe];
    
    B -->|No| D{{"Ha dati propri e comportamenti?<br/>(È un 'sostantivo' importante con delle sue caratteristiche?)"}};
    D -->|Sì| E{{"È un tipo specializzato di un'altra classe?<br/>(Relazione 'IS-A')"}};
    E -->|Sì| F[È una <b>Classe Derivata</b><br/>Usa l'Ereditarietà];
    E -->|No| G[È una <b>Classe Base</b>];

    D -->|No| H[Probabilmente è una <b>Relazione</b> tra classi<br/>un verbo che le collega];

```

## 2. Guida all'Implementazione: Dal Diagramma UML al Codice Python

Una volta che avete il vostro diagramma UML, questo flowchart vi guida su come tradurre le associazioni in attributi Python.

```mermaid
flowchart TD
    A[Analizza una relazione di Associazione] --> B{{"Che cardinalità ha?"}};
    B -->|Uno-a-Uno 1 -- 1| C{{"La relazione è bidirezionale?"}};
    C -->|Sì| C1[<b>Ogni classe ha un attributo</b><br/>che punta all'altra.<br/>Gestisci la coerenza in entrambi i lati.];
    C -->|No unidirezionale| C2[<b>Solo la classe 'sorgente'</b><br/>ha un attributo che punta a quella di destinazione.];

    B -->|Uno-a-Molti 1 -- *| D{{"La relazione è bidirezionale?"}};
    D -->|Sì| D1[La classe 'Uno' ha una <b>lista di attributi</b>.<br/>La classe 'Molti' ha un <b>singolo attributo</b>.];
    D -->|No unidirezionale| D2[<b>Solo la classe 'Uno'</b><br/>ha una lista di attributi che punta ai 'Molti'.];

    B -->|Molti-a-Molti * -- *| E[<b>Ogni classe ha una lista di attributi</b><br/>che punta all'altra.<br/>Gestisci l'aggiunta da entrambi i lati.];
    
```

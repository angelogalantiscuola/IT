# Lezione 4: Disegnare l'Architettura Modulare con UML

Abbiamo trasformato la nostra applicazione `flask_1` in `flask_2`, una versione molto più robusta e organizzata. Ma se dovessimo spiegare questa nuova struttura a un collega o presentarla in un esame, come potremmo farlo in modo chiaro e professionale?

Una descrizione testuale è utile, ma un **diagramma** è spesso molto più efficace. Useremo il **Diagramma delle Classi UML**, che già conosciamo, per visualizzare l'architettura logica della nostra applicazione.

### 1. UML per l'Architettura Software

Mentre nel modulo di OOP abbiamo usato UML per modellare le entità di dati (come `Personaggio` o `Nemico`), qui lo useremo per rappresentare le **componenti logiche** del nostro software.

Il nostro obiettivo è creare un diagramma che mostri:
1.  I principali **moduli funzionali** della nostra applicazione (i Blueprints).
2.  L'**applicazione principale** che li orchestra.
3.  Le **dipendenze** tra questi moduli (chi usa cosa).

### 2. Rappresentare i Componenti Flask in UML

Per adattare UML al nostro contesto, useremo degli **stereotipi**. Uno stereotipo è un'etichetta, scritta tra `<<` e `>>`, che ci permette di definire un "tipo" speciale di classe o componente.

*   `<<Application>>`: Rappresenterà la nostra istanza principale di Flask, creata dalla factory.
*   `<<Blueprint>>`: Rappresenterà i nostri moduli di route (`auth.py` e `posts.py`).

All'interno di queste "classi" stereotipate, elencheremo i loro metodi più importanti, che nel nostro caso sono le **view function**.

### 3. Esempio di Diagramma di Architettura per `flask_2`

Ecco come appare un diagramma UML che descrive la struttura logica della nostra applicazione appena ristrutturata.

```mermaid
classDiagram
    direction LR

    class FlaskApp {
        <<Application>>
        +config
        +register_blueprint(blueprint)
    }

    class AuthBlueprint {
        <<Blueprint>>
        url_prefix: "/auth"
        +register()
        +login()
        +logout()
        +login_required()
    }
    
    class PostsBlueprint {
        <<Blueprint>>
        url_prefix: "/"
        +home()
        +create()
        +edit(post_id)
        +delete(post_id)
    }

    class Database {
      <<Component>>
      +get_db()
      +close_db()
    }

    ' Relazione di "Composizione": l'app è composta dai suoi blueprints
    FlaskApp o-- AuthBlueprint : registers
    FlaskApp o-- PostsBlueprint : registers

    ' Relazione di "Dipendenza": i blueprints usano il database
    AuthBlueprint ..> Database : uses
    PostsBlueprint ..> Database : uses
```

### 4. Come Leggere e Spiegare il Diagramma

Questo diagramma fornisce una "mappa" chiara della nostra applicazione:

1.  **Componenti Principali:** L'applicazione (`FlaskApp`) è composta da due moduli funzionali principali: `AuthBlueprint` e `PostsBlueprint`.
2.  **Registrazione:** La `FlaskApp` "registra" i due Blueprints. La linea con il rombo vuoto (`o--`) indica una relazione di **aggregazione**: l'applicazione "ha" dei Blueprints, ma questi potrebbero esistere anche indipendentemente.
3.  **Responsabilità:**
    *   `AuthBlueprint` è responsabile di tutte le operazioni legate all'utente (`register`, `login`, `logout`). Il suo prefisso URL è `/auth`.
    *   `PostsBlueprint` è responsabile di tutte le operazioni legate ai post (`home`, `create`, etc.).
4.  **Dipendenze:** Le linee tratteggiate (`..>`) mostrano che **entrambi** i Blueprints dipendono dal componente `Database` per poter eseguire le loro operazioni. Questo evidenzia che la logica del database è centralizzata.

### 5. Preparazione per l'Esame (Task 5)

Quando l'esame ti chiede di "sviluppare il progetto di massima della struttura dell'applicazione web", questo tipo di diagramma è una risposta eccellente.

**Perché?**
*   **È Professionale:** Dimostra che non hai solo scritto codice, ma hai anche **progettato l'architettura** del tuo software.
*   **È Chiaro:** Comunica in modo immediato come è organizzata l'applicazione, quali sono i suoi moduli principali e come interagiscono.
*   **Mostra Comprensione:** Fa vedere che hai capito i principi di modularità e separazione delle responsabilità.

**Consiglio:** Per una risposta completa all'esame, presenta questo diagramma e accompagnalo con una breve descrizione testuale (come quella al punto 4) che ne spiega il significato.

Nella prossima lezione, che aprirà un nuovo capitolo, vedremo come migliorare ulteriormente questa architettura sostituendo il componente `Database` con un ORM, e aggiorneremo di conseguenza questo diagramma.
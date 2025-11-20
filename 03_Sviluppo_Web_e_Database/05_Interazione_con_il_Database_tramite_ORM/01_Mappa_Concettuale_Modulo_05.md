# Mappa Concettuale: Interazione con il Database tramite ORM

Questa mappa illustra il passaggio dal codice di accesso al database manuale e basato su SQL a un approccio moderno e orientato agli oggetti, utilizzando un Object-Relational Mapper (ORM).

```mermaid
graph TD
    A["Applicazione Modulare<br>`flask_2` con SQL grezzo"] --> B["Problema&colon;<br>SQL mescolato a Python&comma; codice verboso"];
    B --> C["Principio Guida&colon;<br>**Astrazione del Livello Dati**"];
    C --> D["Soluzione&colon; **ORM con Peewee**"];

    subgraph "Definire i Dati come Oggetti"
        D --> D1["Creazione dei Modelli<br>`class User&lpar;Model&rpar;` in `models.py`"];
        D1 --> D2["Mappatura Automatica<br>Classe -> Tabella&comma; Attributo -> Colonna"];
    end

    subgraph "Interagire con gli Oggetti"
        D --> E1["Sostituzione delle Query SQL"];
        E1 --> E2["Operazioni CRUD Pythoniche<br>`User.create&lpar;&rpar;`&comma; `Post.select&lpar;&rpar;`"];
        E2 --> E3["Codice più Pulito e Sicuro"];
    end
    
    E3 --> F["Applicazione Finale<br>`flask_2` con ORM"];
    F --> G["Aggiornamento del Diagramma<br>di Architettura UML"];
```
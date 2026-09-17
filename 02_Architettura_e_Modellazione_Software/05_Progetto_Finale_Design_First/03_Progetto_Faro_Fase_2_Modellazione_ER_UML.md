# Progetto Faro - Fase 2: Modellazione dei Dati in Parallelo (ER e UML)

Dalle 4 User Stories emergono le entità del dominio: `Personaggio`, `Guerriero`, `Inventario`, `Oggetto`, `Abilita` e l'entità ponte `AbilitaAppresa`.

Modelliamo la struttura statica nei due linguaggi paralleli.

---

## 1. Il Modello ER Completo (Database su Disco)

Nel database relazionale definiamo le tabelle con le **Primary Key (PK)** e le **Foreign Key (FK)** posizionate secondo le nostre regole univoche:
* Relazione 1:1 $\longrightarrow$ `personaggio_id FK` nella tabella `INVENTARIO` con vincolo `UNIQUE`.
* Relazione 1:N $\longrightarrow$ `inventario_id FK` nella tabella `OGGETTO` (sul lato molti).
* Relazione N:N $\longrightarrow$ Scomposta nella tabella ponte `ABILITA_APPRESA` con due Foreign Key.

```mermaid
erDiagram
    PERSONAGGIO ||--|| INVENTARIO : possiede
    INVENTARIO ||--|{ OGGETTO : contiene
    PERSONAGGIO ||--|{ ABILITA_APPRESA : possiede
    ABILITA ||--|{ ABILITA_APPRESA : inclusa_in

    PERSONAGGIO {
        int id PK "Identificatore univoco eroe"
        string nome "Nome eroe"
        int livello "Livello attuale"
        int punti_vita "Punti ferita correnti"
        int forza "Forza fisica (solo Guerrieri)"
    }
    INVENTARIO {
        int id PK "Identificatore zaino"
        int personaggio_id FK "Punta a PERSONAGGIO.id (UNIQUE)"
        int capacita_slot "Slot massimi"
    }
    OGGETTO {
        int id PK "Identificatore oggetto"
        int inventario_id FK "Punta a INVENTARIO.id"
        string nome "Nome oggetto"
        string tipo "Tipo (es. Cura, Arma)"
        int valore_effetto "Potenza effetto"
    }
    ABILITA_APPRESA {
        int id PK "Identificatore record di legame"
        int personaggio_id FK "Punta a PERSONAGGIO.id"
        int abilita_id FK "Punta a ABILITA.id"
        int livello_maestria "Livello maestria (1-5)"
    }
    ABILITA {
        int id PK "Identificatore abilita"
        string nome_abilita "Nome magia/tecnica"
        int costo_mana "Costo mana"
    }
```

---

## 2. Il Diagramma delle Classi UML Completo (Oggetti in RAM)

Nel programma Python, le entità prendono forma come classi con attributi tipizzati e relazioni strutturate:

```mermaid
classDiagram
    Personaggio <|-- Guerriero : IS-A
    Personaggio "1" -- "1" Inventario : possiede
    Inventario "1" -- "*" Oggetto : contiene
    Personaggio "1" -- "*" AbilitaAppresa : apprende
    Abilita "1" -- "*" AbilitaAppresa : fa_riferimento_a

    class Personaggio {
        +id: int
        +nome: str
        +livello: int
        +punti_vita: int
        +inventario: Inventario
        +subisci_danno(danno: int) void
        +attacca(bersaglio: Personaggio) str
        +raccogli_oggetto(ogg: Oggetto) bool
    }

    class Guerriero {
        +forza: int
        +attacca(bersaglio: Personaggio) str
    }

    class Inventario {
        +id: int
        +capacita_slot: int
        +oggetti: list~Oggetto~
        +aggiungi(ogg: Oggetto) bool
    }

    class Oggetto {
        +id: int
        +nome: str
        +tipo: str
        +valore_effetto: int
    }

    class AbilitaAppresa {
        +id: int
        +personaggio: Personaggio
        +abilita: Abilita
        +livello_maestria: int
        +potenzia() void
    }

    class Abilita {
        +id: int
        +nome_abilita: str
        +costo_mana: int
    }
```
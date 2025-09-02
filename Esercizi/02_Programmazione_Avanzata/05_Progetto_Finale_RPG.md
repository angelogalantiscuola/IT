# Esercizio 05: Progetto Finale - Le Cronache di Pythonia

**Obiettivo:** Progettare e implementare un semplice gioco di ruolo (RPG) testuale, applicando tutti i principi della programmazione orientata agli oggetti e della progettazione software appresi durante l'anno.

---

### Descrizione Generale del Gioco

Il giocatore controllerà un Eroe che deve esplorare una mappa composta da stanze, raccogliere oggetti, combattere nemici e sconfiggere il Boss Finale per vincere. Il gioco si svolge interamente nel terminale.

---

### Requisiti Minimi del Sistema

Il vostro software deve modellare e implementare le seguenti entità e funzionalità:

#### **Classi Fondamentali:**

1.  **`EntitaVivente` (Classe Base Astratta o Generica):**
    *   Attributi: `nome` (str), `punti_vita` (int).
    *   Metodi: `attacca(bersaglio)`, `subisci_danno(danno)`.

2.  **`Personaggio` (Eredita da `EntitaVivente`):**
    *   Attributi: `livello` (int), `inventario` (un oggetto `Inventario`).
    *   Metodi: `raccogli_oggetto(oggetto)`, `usa_oggetto(oggetto)`.

3.  **`Guerriero` e `Mago` (Ereditano da `Personaggio`):**
    *   Specializzazioni con attributi unici (`forza` per il guerriero, `mana` per il mago).
    *   Devono fare l'**override** del metodo `attacca` con un comportamento personalizzato.

4.  **`Nemico` (Eredita da `EntitaVivente`):**
    *   Attributi: `valore_attacco` (int).

5.  **`Oggetto`:**
    *   Attributi: `nome` (str), `descrizione` (str).

6.  **`Inventario`:**
    *   Attributi: `oggetti` (lista di `Oggetto`), `capacita` (int).
    *   Metodi: `aggiungi(oggetto)`, `rimuovi(oggetto)`, `mostra()`.

7.  **`Stanza`:**
    *   Attributi: `nome` (str), `descrizione` (str), `nemici` (lista di `Nemico`), `oggetti` (lista di `Oggetto`), `uscite` (un dizionario es. `{'nord': stanza_vicina, 'sud': altra_stanza}`).

8.  **`Mappa`:**
    *   Deve contenere e gestire la collezione di tutte le `Stanze` e i loro collegamenti.

#### **Logica di Gioco Minima:**

1.  **Setup Iniziale:** Creare una mappa con almeno 3-4 stanze collegate. Creare un personaggio e posizionarlo nella stanza iniziale. Popolare le stanze con nemici e oggetti.

2.  **Ciclo Principale:** Il gioco deve presentare al giocatore un menu di azioni possibili basate sulla stanza corrente (es. "muoviti a nord", "raccogli spada", "attacca goblin").

3.  **Movimento:** Il giocatore deve potersi spostare tra le stanze collegate.

4.  **Interazione:** Il giocatore deve poter raccogliere oggetti e visualizzare il proprio inventario.

5.  **Combattimento:**
    *   Se in una stanza c'è un nemico, il giocatore deve poterlo attaccare.
    *   Il combattimento può essere a turni semplici: prima attacca il giocatore, poi il nemico.
    *   Quando i punti vita di un'entità scendono a 0, questa è sconfitta.

6.  **Condizione di Vittoria/Sconfitta:**
    *   Il giocatore vince se sconfigge un `BossFinale` (un tipo speciale di `Nemico`).
    *   Il giocatore perde se i suoi punti vita scendono a 0.

---

### Fasi e Consegne

Il progetto è diviso in due fasi obbligatorie:

#### **Fase 1: Progettazione (Consegna 1)**
*   **Cosa consegnare:** Un unico file `design.md`.
*   **Contenuto:** Un **diagramma delle classi UML completo** che modelli tutte le classi, i loro attributi/metodi principali e tutte le relazioni (ereditarietà e associazioni con cardinalità).
*   **Scadenza:** Fine della seconda settimana del modulo.

#### **Fase 2: Implementazione (Consegna Finale)**
*   **Cosa consegnare:** L'intero progetto Python funzionante.
*   **Contenuto:** Le classi implementate in Python, coerenti con il diagramma UML, e un file `main.py` che avvii e gestisca il gioco.
*   **Scadenza:** Fine del modulo.

### Requisiti Tecnici Obbligatori

*   Uso corretto dell'**ereditarietà** per `Personaggio` e `Nemico`.
*   Uso corretto della **composizione** per l'`Inventario` del personaggio.
*   Uso corretto dell'**incapsulamento** (attributi privati dove sensato) e delle **properties**.
*   Implementazione del **polimorfismo** (override del metodo `attacca`).

### Espansioni (Bonus)

Se completate i requisiti minimi, potete provare ad aggiungere funzionalità extra per migliorare il vostro voto:
*   Creare sottoclassi di `Oggetto` come `Pozione` (ripristina PV) e `Arma` (aumenta l'attacco).
*   Implementare un sistema di salvataggio/caricamento del gioco su file.
*   Aggiungere stanze bloccate che richiedono `Chiavi` (un tipo di `Oggetto`) per essere aperte.
*   Scrivere una suite di test con `pytest` per le classi `Personaggio` e `Inventario`.
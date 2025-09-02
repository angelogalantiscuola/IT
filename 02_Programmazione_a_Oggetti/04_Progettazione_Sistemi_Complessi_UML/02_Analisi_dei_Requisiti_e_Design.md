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

Una volta stabilito che si tratta di un'associazione, la domanda successiva, fondamentale per l'implementazione, è: **"Quanto è forte questo legame?"**.

*   **Legame Forte (Attributo Permanente - "HAS-A"):** L'oggetto A "possiede" l'oggetto B come parte del suo stato. La relazione è duratura.
    *   *Esempio:* Un `Personaggio` **ha un** `Inventario`. L'inventario è una parte fondamentale e permanente del personaggio.
    *   *Implementazione:* L'oggetto B diventa un **attributo** dell'oggetto A, tipicamente inizializzato nel costruttore.
        ```python
        class Personaggio:
            def __init__(self, nome: str):
                self.nome = nome
                self.inventario = Inventario() # L'inventario è un attributo
        ```

*   **Legame Debole (Interazione Temporanea - "USES-A"):** L'oggetto A "usa" l'oggetto B per compiere un'azione, ma non lo possiede. La relazione esiste solo durante l'esecuzione di un metodo.
    *   *Esempio:* Un `Mago` **usa una** `PergamenaMagica` per lanciare un incantesimo. La pergamena non è parte del mago, è uno strumento esterno.
    *   *Implementazione:* L'oggetto B viene passato come **parametro** a un metodo dell'oggetto A.
        ```python
        class Mago:
            def lancia_incantesimo_da_pergamena(self, pergamena: PergamenaMagica):
                # Il mago 'usa' la pergamena, ma non la salva come attributo
                pergamena.attiva_magia()
        ```

In entrambi i casi, sul diagramma UML disegneremo una semplice linea di associazione. Capire questa differenza concettuale ci aiuterà a scrivere codice più logico e meglio organizzato.

## 3. Definire le Cardinalità

Per ogni relazione, è fondamentale specificare la **cardinalità**, ovvero quanti oggetti possono essere coinvolti.

*   `1`: Esattamente uno.
*   `*`: Zero o più (molti).
*   `1..*`: Uno o più.
*   `0..1`: Zero o uno (opzionale).

*Esempio di lettura:*
`Squadra "1" -- "*" Giocatore` si legge: "Una `Squadra` è associata a zero o più `Giocatori`, e un `Giocatore` è associato a esattamente una `Squadra`."

Applicando sistematicamente questa strategia (identifica classi, attributi, metodi, scegli la relazione, definisci la cardinalità), sarai in grado di trasformare qualsiasi requisito in un diagramma delle classi chiaro e ben strutturato.